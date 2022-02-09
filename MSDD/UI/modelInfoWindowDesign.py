from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(635, 683)
        mainWindow.setStyleSheet("background-color: #eaeffa;")
        self.main = QtWidgets.QWidget(mainWindow)
        self.main.setObjectName("main")
        self.main_layout = QtWidgets.QVBoxLayout(self.main)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setObjectName("main_layout")
        self.model_name_value = QtWidgets.QLabel(self.main)
        self.model_name_value.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 14pt;\n"
"    font-weight: bold;\n"
"    margin-bottom: 10px;\n"
"}")
        self.model_name_value.setAlignment(QtCore.Qt.AlignCenter)
        self.model_name_value.setObjectName("model_name_value")
        self.main_layout.addWidget(self.model_name_value)
        self.statistic_layout = QtWidgets.QGridLayout()
        self.statistic_layout.setObjectName("statistic_layout")
        self.train_loss_label = QtWidgets.QLabel(self.main)
        self.train_loss_label.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 10pt;\n"
"}")
        self.train_loss_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.train_loss_label.setObjectName("train_loss_label")
        self.statistic_layout.addWidget(self.train_loss_label, 5, 0, 1, 1)
        self.test_acc_label = QtWidgets.QLabel(self.main)
        self.test_acc_label.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 10pt;\n"
"}")
        self.test_acc_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.test_acc_label.setObjectName("test_acc_label")
        self.statistic_layout.addWidget(self.test_acc_label, 0, 0, 1, 1)
        self.val_acc_label = QtWidgets.QLabel(self.main)
        self.val_acc_label.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 10pt;\n"
"}")
        self.val_acc_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.val_acc_label.setObjectName("val_acc_label")
        self.statistic_layout.addWidget(self.val_acc_label, 2, 0, 1, 1)
        self.val_loss_label = QtWidgets.QLabel(self.main)
        self.val_loss_label.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 10pt;\n"
"}")
        self.val_loss_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.val_loss_label.setObjectName("val_loss_label")
        self.statistic_layout.addWidget(self.val_loss_label, 3, 0, 1, 1)
        self.train_acc_label = QtWidgets.QLabel(self.main)
        self.train_acc_label.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 10pt;\n"
"}")
        self.train_acc_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.train_acc_label.setObjectName("train_acc_label")
        self.statistic_layout.addWidget(self.train_acc_label, 4, 0, 1, 1)
        self.test_loss__label = QtWidgets.QLabel(self.main)
        self.test_loss__label.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 10pt;\n"
"}")
        self.test_loss__label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.test_loss__label.setObjectName("test_loss__label")
        self.statistic_layout.addWidget(self.test_loss__label, 1, 0, 1, 1)
        self.params_label = QtWidgets.QLabel(self.main)
        self.params_label.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 10pt;\n"
"}")
        self.params_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.params_label.setObjectName("params_label")
        self.statistic_layout.addWidget(self.params_label, 6, 0, 1, 1)
        self.test_acc_value = QtWidgets.QLabel(self.main)
        self.test_acc_value.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 10pt;\n"
"}")
        self.test_acc_value.setText("")
        self.test_acc_value.setObjectName("test_acc_value")
        self.statistic_layout.addWidget(self.test_acc_value, 0, 1, 1, 1)
        self.test_loss_value = QtWidgets.QLabel(self.main)
        self.test_loss_value.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 10pt;\n"
"}")
        self.test_loss_value.setText("")
        self.test_loss_value.setObjectName("test_loss_value")
        self.statistic_layout.addWidget(self.test_loss_value, 1, 1, 1, 1)
        self.val_acc_value = QtWidgets.QLabel(self.main)
        self.val_acc_value.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 10pt;\n"
"}")
        self.val_acc_value.setText("")
        self.val_acc_value.setObjectName("val_acc_value")
        self.statistic_layout.addWidget(self.val_acc_value, 2, 1, 1, 1)
        self.val_loss_value = QtWidgets.QLabel(self.main)
        self.val_loss_value.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 10pt;\n"
"}")
        self.val_loss_value.setText("")
        self.val_loss_value.setObjectName("val_loss_value")
        self.statistic_layout.addWidget(self.val_loss_value, 3, 1, 1, 1)
        self.train_acc_value = QtWidgets.QLabel(self.main)
        self.train_acc_value.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 10pt;\n"
"}")
        self.train_acc_value.setText("")
        self.train_acc_value.setObjectName("train_acc_value")
        self.statistic_layout.addWidget(self.train_acc_value, 4, 1, 1, 1)
        self.train_loss_value = QtWidgets.QLabel(self.main)
        self.train_loss_value.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 10pt;\n"
"}")
        self.train_loss_value.setText("")
        self.train_loss_value.setObjectName("train_loss_value")
        self.statistic_layout.addWidget(self.train_loss_value, 5, 1, 1, 1)
        self.params_value = QtWidgets.QLabel(self.main)
        self.params_value.setStyleSheet("QLabel {\n"
"    font-family: \'Consolas\';\n"
"    font-size: 10pt;\n"
"}")
        self.params_value.setText("")
        self.params_value.setObjectName("params_value")
        self.statistic_layout.addWidget(self.params_value, 6, 1, 1, 1)
        self.main_layout.addLayout(self.statistic_layout)
        self.matplotlib_accuracy_plot = MatplotlibWidget(self.main)
        self.matplotlib_accuracy_plot.setMinimumSize(QtCore.QSize(0, 200))
        self.matplotlib_accuracy_plot.setMaximumSize(QtCore.QSize(16777215, 200))
        self.matplotlib_accuracy_plot.setStyleSheet("margin-top: 10px;\n"
"margin-bottom: 10px;")
        self.matplotlib_accuracy_plot.setObjectName("matplotlib_accuracy_plot")
        self.main_layout.addWidget(self.matplotlib_accuracy_plot)
        self.matplotlib_loss_plot = MatplotlibWidget(self.main)
        self.matplotlib_loss_plot.setMinimumSize(QtCore.QSize(0, 200))
        self.matplotlib_loss_plot.setMaximumSize(QtCore.QSize(16777215, 200))
        self.matplotlib_loss_plot.setStyleSheet("margin-top: 10px;\n"
"margin-bottom: 10px;")
        self.matplotlib_loss_plot.setObjectName("matplotlib_loss_plot")
        self.main_layout.addWidget(self.matplotlib_loss_plot)
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        self.train_b = QtWidgets.QPushButton(self.main)
        self.train_b.setStyleSheet("QPushButton {\n"
"    color: #f7f7f7;\n"
"    background-color: #4c5b61;\n"
"    border-radius: 10px;\n"
"    margin: 10px 10px 0px 10px;\n"
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
        self.train_b.setObjectName("train_b")
        self.buttons_layout.addWidget(self.train_b)
        self.retrain_b = QtWidgets.QPushButton(self.main)
        self.retrain_b.setStyleSheet("QPushButton {\n"
"    color: #f7f7f7;\n"
"    background-color: #4c5b61;\n"
"    border-radius: 10px;\n"
"    margin: 10px 10px 0px 10px;\n"
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
        self.retrain_b.setObjectName("retrain_b")
        self.buttons_layout.addWidget(self.retrain_b)
        self.stop_b = QtWidgets.QPushButton(self.main)
        self.stop_b.setStyleSheet("QPushButton {\n"
"    color: #f7f7f7;\n"
"    background-color: #4c5b61;\n"
"    border-radius: 10px;\n"
"    margin: 10px 10px 0px 10px;\n"
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
        self.stop_b.setObjectName("stop_b")
        self.buttons_layout.addWidget(self.stop_b)
        self.main_layout.addLayout(self.buttons_layout)
        mainWindow.setCentralWidget(self.main)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MSDD | "))
        self.model_name_value.setText(_translate("mainWindow", "Назва моделі"))
        self.train_loss_label.setText(_translate("mainWindow", "Витрати на навчальному наборі: "))
        self.test_acc_label.setText(_translate("mainWindow", "Точність на тестовому наборі: "))
        self.val_acc_label.setText(_translate("mainWindow", "Точність на валідаційному наборі: "))
        self.val_loss_label.setText(_translate("mainWindow", "Витрати на валідаційному наборі: "))
        self.train_acc_label.setText(_translate("mainWindow", "Точність на навчальному наборі: "))
        self.test_loss__label.setText(_translate("mainWindow", "Витрати на тестовому наборі: "))
        self.params_label.setText(_translate("mainWindow", "Кількість параметрів: "))
        self.train_b.setText(_translate("mainWindow", "Донавчити"))
        self.retrain_b.setText(_translate("mainWindow", "Навчити"))
        self.stop_b.setText(_translate("mainWindow", "Зупинити навчання"))
from UI.MatplotlibWidget import MatplotlibWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
