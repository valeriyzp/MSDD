from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(410, 475)
        mainWindow.setStyleSheet("background-color: #eaeffa;")
        self.main = QtWidgets.QWidget(mainWindow)
        self.main.setObjectName("main")
        self.main_layout = QtWidgets.QVBoxLayout(self.main)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setObjectName("main_layout")
        self.info_layout = QtWidgets.QHBoxLayout()
        self.info_layout.setObjectName("info_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.info_layout.addItem(spacerItem)
        self.info_logo = QtWidgets.QLabel(self.main)
        self.info_logo.setText("")
        self.info_logo.setPixmap(QtGui.QPixmap("D:/MSDD/resources/icon.png"))
        self.info_logo.setObjectName("info_logo")
        self.info_layout.addWidget(self.info_logo)
        self.info_text = QtWidgets.QLabel(self.main)
        self.info_text.setStyleSheet("QLabel {\n"
"    color: #393e46;\n"
"    font-family: \'Consolas\';\n"
"    font-size: 24pt;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.info_text.setObjectName("info_text")
        self.info_layout.addWidget(self.info_text)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.info_layout.addItem(spacerItem1)
        self.main_layout.addLayout(self.info_layout)
        self.training_b = QtWidgets.QPushButton(self.main)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.training_b.setFont(font)
        self.training_b.setStyleSheet("QPushButton {\n"
"    color: #f7f7f7;\n"
"    background-color: #4c5b61;\n"
"    border-radius: 10px;\n"
"    margin: 20px 30px 10px 30px;\n"
"    height: 32px;\n"
"    font: 14pt \'Consolas\';\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #393e46;\n"
"    font: bold;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background-color: #424b53;\n"
"}")
        self.training_b.setObjectName("training_b")
        self.main_layout.addWidget(self.training_b)
        self.classification_b = QtWidgets.QPushButton(self.main)
        self.classification_b.setStyleSheet("QPushButton {\n"
"    color: #f7f7f7;\n"
"    background-color: #4c5b61;\n"
"    border-radius: 10px;\n"
"    margin: 10px 30px 10px 30px;\n"
"    height: 32px;\n"
"    font: 14pt \'Consolas\';\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #393e46;\n"
"    font: bold;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background-color: #424b53;\n"
"}")
        self.classification_b.setObjectName("classification_b")
        self.main_layout.addWidget(self.classification_b)
        self.about_b = QtWidgets.QPushButton(self.main)
        self.about_b.setStyleSheet("QPushButton {\n"
"    color: #f7f7f7;\n"
"    background-color: #4c5b61;\n"
"    border-radius: 10px;\n"
"    margin: 20px 30px 10px 30px;\n"
"    height: 32px;\n"
"    font: 14pt \'Consolas\';\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #393e46;\n"
"    font: bold;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background-color: #424b53;\n"
"}")
        self.about_b.setObjectName("about_b")
        self.main_layout.addWidget(self.about_b)
        self.exit_b = QtWidgets.QPushButton(self.main)
        self.exit_b.setStyleSheet("QPushButton {\n"
"    color: #f7f7f7;\n"
"    background-color: #4c5b61;\n"
"    border-radius: 10px;\n"
"    margin: 10px 30px 10px 30px;\n"
"    height: 32px;\n"
"    font: 14pt \'Consolas\';\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #393e46;\n"
"    font: bold;\n"
"}\n"
"\n"
"QPushButton:hover:!pressed {\n"
"    background-color: #424b53;\n"
"}")
        self.exit_b.setObjectName("exit_b")
        self.main_layout.addWidget(self.exit_b)
        mainWindow.setCentralWidget(self.main)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Metal Surfaces Defects Detection"))
        self.info_text.setText(_translate("mainWindow", "Metal\n"
"Surfaces\n"
"Defects\n"
"Detection"))
        self.training_b.setText(_translate("mainWindow", "Навчання"))
        self.classification_b.setText(_translate("mainWindow", "Класифікація"))
        self.about_b.setText(_translate("mainWindow", "Про програму"))
        self.exit_b.setText(_translate("mainWindow", "Вихід"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
