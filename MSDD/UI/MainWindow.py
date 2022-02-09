from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot, Qt, QSize

from Settings.DefaultSettings import DefaultSettings
from UI.mainWindowDesign import Ui_mainWindow
from UI.ModelListWindow import ModelListWindow
from UI.ClassificationWindow import ClassificationWindow


class MainWindow(QMainWindow, Ui_mainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        icon = QIcon()
        icon.addFile(DefaultSettings.RESOURCES_PATH + "icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.setFixedSize(self.size())
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)

        self.info_logo.setPixmap(QtGui.QPixmap(DefaultSettings.RESOURCES_PATH + "icon.png"))

        self.training_b.clicked.connect(self.on_training_b_click)
        self.classification_b.clicked.connect(self.on_classification_b_click)
        self.about_b.clicked.connect(self.on_about_b_click)
        self.exit_b.clicked.connect(self.on_exit_b_click)

    def closeEvent(self, event):
        close_dialog_result = QMessageBox.question(self, 'Закрити програму', 'Ви дійсно хочете вийти з програми?',
                                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if close_dialog_result == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()
    def on_training_b_click(self):
        self.modelListWindow = ModelListWindow()
        self.modelListWindow.setWindowModality(Qt.ApplicationModal)
        self.modelListWindow.show()

    @pyqtSlot()
    def on_classification_b_click(self):
        self.classificationWindow = ClassificationWindow()
        self.classificationWindow.setWindowModality(Qt.ApplicationModal)
        self.classificationWindow.show()

    @pyqtSlot()
    def on_about_b_click(self):
        QMessageBox.about(self, "Про MSDD", DefaultSettings.ABOUT_PROGRAM)

        # Information about Qt
        # QMessageBox.aboutQt(self)

    @pyqtSlot()
    def on_exit_b_click(self):
        self.close()
