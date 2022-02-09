from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot, Qt, QSize

from Settings.DefaultSettings import DefaultSettings
from UI.modelsListWindowDesign import Ui_mainWindow
from UI.ModelInfoWindow import ModelInfoWindow
from UI.MatplotlibWidget import MatplotlibWidget

from Model.ModelsKeeper import ModelsKeeper


class ModelListWindow(QMainWindow, Ui_mainWindow):

    def __init__(self):
        super(ModelListWindow, self).__init__()
        self.setupUi(self)

        icon = QIcon()
        icon.addFile(DefaultSettings.RESOURCES_PATH + "icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.update_scroll_area_content()

    def update_scroll_area_content(self):
        scroll_bar_value = self.scroll_area.verticalScrollBar().value()

        self.scroll_area_widget_content = QtWidgets.QWidget()
        self.scroll_area_widget_content.setGeometry(QtCore.QRect(0, 0, 850, 625))
        self.scroll_area_widget_content.setObjectName("scroll_area_widget_content")

        self.scroll_area_widget_content_layout = QtWidgets.QVBoxLayout(self.scroll_area_widget_content)
        self.scroll_area_widget_content_layout.setContentsMargins(20, 0, 20, 20)
        self.scroll_area_widget_content_layout.setObjectName("scroll_area_widget_content_layout")

        for name, model in ModelsKeeper().get_models().items():
            q_group_box = QtWidgets.QGroupBox(self.scroll_area_widget_content)
            q_group_box.setTitle(name)
            q_group_box.setStyleSheet("QGroupBox {\n"
                                      "    border: 1px solid #4c5b61;\n"
                                      "    border-radius: 5px;\n"
                                      "    margin-top: 20px;\n"
                                      "    height: 250px;\n"
                                      "    font: 12pt \'Consolas\';\n"
                                      "    font-weight: bold;\n"
                                      "}\n"
                                      "\n"
                                      "QGroupBox::title {\n"
                                      "    subcontrol-origin: margin;\n"
                                      "    left: 10px;\n"
                                      "    padding: 10px 3px 0 3px;\n"
                                      "}")

            q_group_box_layout = QtWidgets.QGridLayout(q_group_box)
            q_group_box_layout.setContentsMargins(10, 10, 10, 10)

            q_group_box_info = QtWidgets.QFormLayout()
            q_group_box_info.setLabelAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
            q_group_box_info.setFormAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

            accuracy_label = QtWidgets.QLabel(q_group_box)
            accuracy_label.setStyleSheet("QLabel {\n"
                                         "    font-family: \'Consolas\';\n"
                                         "    font-size: 10pt;\n"
                                         "}")
            q_group_box_info.setWidget(0, QtWidgets.QFormLayout.LabelRole, accuracy_label)

            accuracy_value = QtWidgets.QLabel(q_group_box)
            accuracy_value.setStyleSheet("QLabel {\n"
                                         "    font-family: \'Consolas\';\n"
                                         "    font-size: 10pt;\n"
                                         "}")
            q_group_box_info.setWidget(0, QtWidgets.QFormLayout.FieldRole, accuracy_value)

            loss_label = QtWidgets.QLabel(q_group_box)
            loss_label.setStyleSheet("QLabel {\n"
                                     "    font-family: \'Consolas\';\n"
                                     "    font-size: 10pt;\n"
                                     "}")
            q_group_box_info.setWidget(1, QtWidgets.QFormLayout.LabelRole, loss_label)

            loss_value = QtWidgets.QLabel(q_group_box)
            loss_value.setStyleSheet("QLabel {\n"
                                     "    font-family: \'Consolas\';\n"
                                     "    font-size: 10pt;\n"
                                     "}")
            q_group_box_info.setWidget(1, QtWidgets.QFormLayout.FieldRole, loss_value)

            q_group_box_layout.addLayout(q_group_box_info, 0, 0, 1, 1)

            matplotlib_plot = MatplotlibWidget(q_group_box)


            q_group_box_layout.addWidget(matplotlib_plot, 0, 1, 1, 3)

            info_b = QtWidgets.QPushButton(q_group_box)
            info_b.setStyleSheet("QPushButton {\n"
                                 "    color: #f7f7f7;\n"
                                 "    background-color: #4c5b61;\n"
                                 "    border-radius: 5px;\n"
                                 "    margin: 5px;\n"
                                 "    height: 20px;\n"
                                 "    font: 10pt \'Consolas\';\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed {\n"
                                 "    background-color: #393e46;\n"
                                 "    font: bold;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover:!pressed\n"
                                 "{\n"
                                 "    background-color: #424b53;\n"
                                 "}")
            q_group_box_layout.addWidget(info_b, 1, 3, 1, 1)

            self.scroll_area_widget_content_layout.addWidget(q_group_box)

            info_b.setText("Детальніше")
            accuracy_label.setText("Точність:")
            loss_label.setText("Витрати:")

            if model.is_saved_fitted_model():
                accuracy_value.setText(f'{model.evaluateResults["accuracy"]:.2f}')
                loss_value.setText(f'{model.evaluateResults["loss"]:.2f}')

                matplotlib_plot.make_plot(range(1, len(model.fitHistory["accuracy"]) + 1),
                                          {"навчання": model.fitHistory["accuracy"],
                                           "валідація": model.fitHistory["val_accuracy"]},
                                          x_label="епоха", title="Точність")
            else:
                accuracy_value.setText("")
                loss_value.setText("")

                matplotlib_plot.make_plot([],
                                          {"навчання": [],
                                           "валідація": []},
                                          x_label="епоха", title="Точність")

            info_b.clicked.connect(lambda state, x=name: self.on_info_b_click(x))

        spacer_item = QtWidgets.QSpacerItem(20, 210, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.scroll_area_widget_content_layout.addItem(spacer_item)

        self.scroll_area.setWidget(self.scroll_area_widget_content)

        self.scroll_area.verticalScrollBar().setValue(scroll_bar_value)

    @pyqtSlot()
    def on_info_b_click(self, name):
        self.modelInfoWindow = ModelInfoWindow(self, name)
        self.modelInfoWindow.setWindowModality(Qt.ApplicationModal)
        self.modelInfoWindow.show()
