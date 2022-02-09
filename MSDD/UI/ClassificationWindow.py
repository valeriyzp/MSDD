from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot, Qt, QSize

from Model.ModelsKeeper import ModelsKeeper
from Settings.DefaultSettings import DefaultSettings
from UI.classificationWindowDesign import Ui_mainWindow

from Tools.StoppableThread import StoppableThread


class ClassificationWindow(QMainWindow, Ui_mainWindow):

    def __init__(self):
        self.model = None
        self.loadModelThread = None
        self.predictionThread = None

        super(ClassificationWindow, self).__init__()
        self.setupUi(self)

        icon = QIcon()
        icon.addFile(DefaultSettings.RESOURCES_PATH + "icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.setFixedSize(self.size())
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)

        self.image.setPixmap(QtGui.QPixmap(DefaultSettings.RESOURCES_PATH + "placeholder.png"))

        models_keeper = ModelsKeeper()
        for name, model in models_keeper.get_models().items():
            if model.is_saved_fitted_model():
                self.model_select.addItem(name)

        if self.model_select.count() > 0:
            self.model_select.setCurrentIndex(self.model_select.count() - 1)

        self.classify_b.clicked.connect(self.on_classify_b_click)
        self.model_select.currentIndexChanged.connect(self.on_model_select_current_index_changed)
        self.on_model_select_current_index_changed()

    @pyqtSlot()
    def on_model_select_current_index_changed(self):
        if self.loadModelThread is not None and self.loadModelThread.is_alive():
            self.loadModelThread.kill()
            self.loadModelThread.join()

        if self.model is not None:
            self.model.model = None

        self.model = ModelsKeeper().get_model_by_name(self.model_select.currentText())

        if self.model is not None:
            self.loadModelThread = StoppableThread(target=self.load_model)
            self.loadModelThread.start()

    @pyqtSlot()
    def on_classify_b_click(self):
        if self.model is not None:

            self.image.setPixmap(QtGui.QPixmap(DefaultSettings.RESOURCES_PATH + "placeholder.png"))
            self.image.repaint()

            self.prediction.setText("передбачення")
            self.prediction.repaint()

            image_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Завантажити зображення', "", "Images (*.png *.jpg *.bmp)")
            if image_path != "":
                self.image.setPixmap(QtGui.QPixmap(image_path))
                self.image.repaint()

                self.prediction.setText("* передбачення...")
                self.prediction.repaint()

                self.classify_b.setEnabled(False)

                self.predictionThread = StoppableThread(self.classify(image_path))
                self.predictionThread.start()

    def load_model(self):
        self.model.load_model()

    def classify(self, image_path):
        if self.loadModelThread is not None and self.loadModelThread.is_alive():
            self.loadModelThread.join()

        res_class = self.model.predict(image_path)
        self.prediction.setText(res_class)
        self.prediction.repaint()

        self.classify_b.setEnabled(True)

    def closeEvent(self, event):
        if self.predictionThread is not None and self.predictionThread.is_alive():
            self.predictionThread.kill()
            self.predictionThread.join()

        if self.loadModelThread is not None and self.loadModelThread.is_alive():
            self.loadModelThread.kill()
            self.loadModelThread.join()

        if self.model is not None:
            self.model.clear_model_variable()
