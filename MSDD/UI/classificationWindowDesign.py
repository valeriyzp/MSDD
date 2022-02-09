from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(346, 500)
        mainWindow.setStyleSheet("background-color: #eaeffa;")
        self.main = QtWidgets.QWidget(mainWindow)
        self.main.setObjectName("main")
        self.main_layout = QtWidgets.QVBoxLayout(self.main)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setObjectName("main_layout")
        self.model_select = QtWidgets.QComboBox(self.main)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.model_select.setFont(font)
        self.model_select.setStyleSheet("QComboBox {\n"
"    color: #4c5b61;\n"
"    background-color: #f7f7f7;\n"
"    border-radius: 10px;\n"
"    border: 2px solid;\n"
"    border-color: #4c5b61;\n"
"    spacing: 40px;\n"
"    padding-left: 5px;\n"
"    height: 28px;\n"
"    margin-bottom: 10px;\n"
"}\n"
"\n"
"QComboBox:hover:!pressed {\n"
"    background-color: #f0f0f0;\n"
"}\n"
"\n"
"QComboBox::drop-down:hover:!pressed {\n"
"    background-color: #424b53;\n"
"}\n"
"\n"
"QComboBox::drop-down:pressed {\n"
"    background-color: #393e46;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"    border-left: 2px solid #4c5b61;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    background-color: #4c5b61;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"    background-color: #f7f7f7;\n"
"    border: 2px solid #4c5b61;\n"
"    border-radius: 1px;\n"
"\n"
"\n"
"    selection-background-color: lightgray;\n"
"    selection-color: #4c5b61;\n"
"    selection-padding-left: 5px;\n"
"\n"
"    outline: none;\n"
"}\n"
"\n"
"lightgray\n"
"4c5b61")
        self.model_select.setObjectName("model_select")
        self.main_layout.addWidget(self.model_select)
        self.classify_b = QtWidgets.QPushButton(self.main)
        self.classify_b.setStyleSheet("QPushButton {\n"
"    color: #f7f7f7;\n"
"    background-color: #4c5b61;\n"
"    border-radius: 10px;\n"
"    margin: 10px 0px 20px 0px;\n"
"    height: 32px;\n"
"    font: 10pt \'Consolas\';\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #393e46;\n"
"    font: bold;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background-color: #424b53;\n"
"}\n"
"")
        self.classify_b.setObjectName("classify_b")
        self.main_layout.addWidget(self.classify_b)
        self.image = QtWidgets.QLabel(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setScaledContents(True)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.main_layout.addWidget(self.image)
        self.prediction = QtWidgets.QLabel(self.main)
        self.prediction.setMinimumSize(QtCore.QSize(0, 32))
        self.prediction.setMaximumSize(QtCore.QSize(16777215, 32))
        self.prediction.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 12pt;\n"
"    font-weight: bold;\n"
"}")
        self.prediction.setAlignment(QtCore.Qt.AlignCenter)
        self.prediction.setObjectName("prediction")
        self.main_layout.addWidget(self.prediction)
        mainWindow.setCentralWidget(self.main)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MSDD | Класифікація"))
        self.model_select.setPlaceholderText(_translate("mainWindow", "Виберіть модель"))
        self.classify_b.setText(_translate("mainWindow", "Завантажити та класифікувати зображення"))
        self.prediction.setText(_translate("mainWindow", "передбачення"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
