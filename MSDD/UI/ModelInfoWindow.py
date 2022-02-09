from datetime import datetime

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot, QTimer, Qt, QSize

from Data.Dataset import Dataset
from Settings.DefaultSettings import DefaultSettings
from UI.modelInfoWindowDesign import Ui_mainWindow

from Model.ModelsKeeper import ModelsKeeper

from Tools.StoppableThread import StoppableThread


class ModelInfoWindow(QMainWindow, Ui_mainWindow):

    def __init__(self, parent_window, model_name):

        self.parentWindow = parent_window
        self.modelName = model_name
        self.model = None
        self.lastInfoChange = datetime.now()
        self.isModelChanged = False

        self.trainThread = None

        super(ModelInfoWindow, self).__init__()
        self.setupUi(self)

        icon = QIcon()
        icon.addFile(DefaultSettings.RESOURCES_PATH + "icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.setFixedSize(self.size())
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)

        self.setWindowTitle(self.windowTitle() + self.modelName)

        self.model = ModelsKeeper().get_model_by_name(self.modelName)

        self.model_name_value.setText(self.modelName)

        self.set_model_info()

        self.stop_b.setEnabled(False)

        self.train_b.clicked.connect(self.on_train_b_click)
        self.retrain_b.clicked.connect(self.on_retrain_b_click)
        self.stop_b.clicked.connect(self.on_stop_b_click)

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_model_for_updates)
        self.timer.start(1000)

    def update_model_info(self):
        self.isModelChanged = True
        self.set_model_info()

    def set_model_info(self):
        self.lastInfoChange = datetime.now()

        if self.model is not None and self.model.is_saved_fitted_model():

            self.test_acc_value.setText(f'{self.model.evaluateResults["accuracy"]:.4f}')
            self.test_loss_value.setText(f'{self.model.evaluateResults["loss"]:.4f}')
            self.val_acc_value.setText(f'{self.model.fitHistory["val_accuracy"][-1]:.4f}')
            self.val_loss_value.setText(f'{self.model.fitHistory["val_loss"][-1]:.4f}')
            self.train_acc_value.setText(f'{self.model.fitHistory["accuracy"][-1]:.4f}')
            self.train_loss_value.setText(f'{self.model.fitHistory["loss"][-1]:.4f}')
            self.params_value.setText('{:,}'.format(self.model.parametersCount).replace(',', ' '))

            self.matplotlib_accuracy_plot.make_plot(range(1, len(self.model.fitHistory["accuracy"]) + 1),
                                                    {"навчання": self.model.fitHistory["accuracy"],
                                                     "валідація": self.model.fitHistory["val_accuracy"]},
                                                    x_label="епоха", title="Точність")

            self.matplotlib_loss_plot.make_plot(range(1, len(self.model.fitHistory["loss"]) + 1),
                                                {"навчання": self.model.fitHistory["loss"],
                                                 "валідація": self.model.fitHistory["val_loss"]},
                                                x_label="епоха", title="Витрати")
        else:
            self.test_acc_value.setText("")
            self.test_loss_value.setText("")
            self.val_acc_value.setText("")
            self.val_loss_value.setText("")
            self.train_acc_value.setText("")
            self.train_loss_value.setText("")
            self.params_value.setText("")

            self.matplotlib_accuracy_plot.make_plot([],
                                                    {"навчання": [],
                                                     "валідація": []},
                                                    x_label="епоха", title="Точність")

            self.matplotlib_loss_plot.make_plot([],
                                                {"навчання": [],
                                                 "валідація": []},
                                                x_label="епоха", title="Витрати")

    @pyqtSlot()
    def on_train_b_click(self):
        self.model_name_value.setText(self.modelName + "* навчання...")
        self.model_name_value.repaint()

        self.stop_b.setEnabled(True)
        self.train_b.setEnabled(False)
        self.retrain_b.setEnabled(False)

        self.trainThread = StoppableThread(target=self.train)
        self.trainThread.start()

    def train(self):
        try:
            if self.model.is_saved_fitted_model():
                dataset = Dataset(DefaultSettings.DATASET_PATH)

                self.model.load_model()
                self.model.fit_model(dataset)
            else:
                self.retrain()
        finally:
            self.on_train_end()

    @pyqtSlot()
    def on_retrain_b_click(self):
        if self.model is not None and self.model.is_saved_fitted_model():
            dialog_result = QMessageBox.question(self, 'Перенавчити модель', 'Ви дійсно хочете перенавчити модель?\n'
                                                                             'Існуюча навчена модель буде видалена...',
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if dialog_result == QMessageBox.No:
                return

        self.model_name_value.setText(self.modelName + "* навчання...")
        self.model_name_value.repaint()

        self.stop_b.setEnabled(True)
        self.train_b.setEnabled(False)
        self.retrain_b.setEnabled(False)

        self.trainThread = StoppableThread(target=self.retrain)
        self.trainThread.start()

    def retrain(self):
        try:
            dataset = Dataset(DefaultSettings.DATASET_PATH)

            self.model.set_new_model_and_compile(dataset.get_num_of_classes())
            self.model.fit_model(dataset)
        finally:
            self.on_train_end()

    def cancel_training(self):
        if self.trainThread is not None and self.trainThread.is_alive():
            self.model_name_value.setText(self.modelName + "* зупинка навчання...")
            self.model_name_value.repaint()
            self.trainThread.kill()
            self.trainThread.join()

    def on_train_end(self):
        self.check_model_for_updates()

        self.model.clear_model_variables()
        if self.model.is_saved_fitted_model():
            self.model.load_model_info()

        self.model_name_value.setText(self.modelName)
        self.model_name_value.repaint()

        self.train_b.setEnabled(True)
        self.retrain_b.setEnabled(True)
        self.stop_b.setEnabled(False)

    @pyqtSlot()
    def on_stop_b_click(self):
        self.cancel_training()

    @pyqtSlot()
    def check_model_for_updates(self):
        if self.lastInfoChange <= self.model.lastChangeTime:
            self.update_model_info()

    def closeEvent(self, event):
        self.timer.stop()
        self.cancel_training()

        if self.isModelChanged:
            self.parentWindow.update_scroll_area_content()
