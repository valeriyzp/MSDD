from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5 import QtWidgets


class MatplotlibWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.vbl = QtWidgets.QVBoxLayout()
        self.setLayout(self.vbl)

        self.fig = Figure()
        self.plot = self.fig.add_subplot()
        self.canvas = FigureCanvasQTAgg(self.fig)
        FigureCanvasQTAgg.setSizePolicy(self.canvas, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self.canvas)
        self.vbl.addWidget(self.canvas)

    def make_plot(self, ox, oy, x_label="", y_label="", title=""):
        self.fig.clear()
        self.plot = self.fig.add_subplot(111)
        self.fig.subplots_adjust(bottom=0.3, top=0.8)
        self.plot.grid(True)

        for key, value in oy.items():
            self.plot.plot(ox, value, label=key)

        self.plot.set_title(title, fontsize=12)
        self.plot.set_xlabel(x_label, fontsize=10)
        self.plot.set_ylabel(y_label, fontsize=10)

        if len(ox) > 1:
            self.plot.set_xlim(1, ox[-1])
            self.plot.set_xticks([i for i in range(1, ox[-1]+1)])

        if title == "Точність":
            self.plot.legend(loc='lower center', fontsize=10)
            self.plot.set_ylim(0.0, 1.0)
            self.plot.set_yticks([i / 10.0 for i in range(0, 11, 2)])
            self.plot.set_yticks([i / 10.0 for i in range(0, 11, 1)], minor=True)
            self.plot.grid(True, which='both')
        elif title == "Витрати":
            self.plot.legend(loc='upper center', fontsize=10)
        else:
            self.plot.legend(fontsize=10)

        self.canvas.draw()


# Another approach to create MatplotlibWidget
#
#
# class MplCanvas(FigureCanvasQTAgg):
#     def __init__(self):
#         self.fig = Figure()
#         self.ax = self.fig.add_subplot(111)
#         FigureCanvasQTAgg.__init__(self, self.fig)
#         FigureCanvasQTAgg.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
#         FigureCanvasQTAgg.updateGeometry(self)
#
#
# class MplWidget(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)
#         self.canvas = MplCanvas()
#         self.vbl = QtWidgets.QVBoxLayout()
#         self.vbl.addWidget(self.canvas)
#         self.setLayout(self.vbl)
