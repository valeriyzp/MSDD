from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(850, 625)
        mainWindow.setStyleSheet("background-color: #eaeffa;")
        self.main = QtWidgets.QWidget(mainWindow)
        self.main.setObjectName("main")
        self.main_layout = QtWidgets.QVBoxLayout(self.main)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setObjectName("main_layout")
        self.scroll_area = QtWidgets.QScrollArea(self.main)
        self.scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.scroll_area_widget_content = QtWidgets.QWidget()
        self.scroll_area_widget_content.setGeometry(QtCore.QRect(0, 0, 850, 625))
        self.scroll_area_widget_content.setObjectName("scroll_area_widget_content")
        self.scroll_area_widget_content_layout = QtWidgets.QVBoxLayout(self.scroll_area_widget_content)
        self.scroll_area_widget_content_layout.setContentsMargins(20, 0, 20, 20)
        self.scroll_area_widget_content_layout.setObjectName("scroll_area_widget_content_layout")
        self.scroll_area.setWidget(self.scroll_area_widget_content)
        self.main_layout.addWidget(self.scroll_area)
        mainWindow.setCentralWidget(self.main)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MSDD | Навчання"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
