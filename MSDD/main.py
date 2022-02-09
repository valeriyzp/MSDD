import os
import sys
from PyQt5.QtWidgets import QApplication

from Model.ModelsKeeper import ModelsKeeper

from UI.MainWindow import MainWindow


def main():
    ModelsKeeper()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

    main()
