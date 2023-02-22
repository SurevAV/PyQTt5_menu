from PyQt5 import QtCore, QtGui, QtWidgets
from Class_an_approach import *
from Class_commodity_cashiers_arm import *
from Class_technical_condition import *
from Class_wagon_weighing import *
from Class_availability_of_wagons import *
import os
import PyQt5
import sys

dirname = os.path.dirname(PyQt5.__file__)
plugin_path = os.path.join(dirname, "plugins", "platforms")
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = plugin_path


class class_image_widget(QtWidgets.QWidget):
    def __init__(self, name):
        super().__init__()
        self.size = 1.0

        self.setWindowTitle(name)

        self.setWindowIcon(QtGui.QIcon("train.png"))

        self.pixmap = QtGui.QPixmap(name + ".png")

        self.sizeObject = self.pixmap.size()

        self.grid = QtWidgets.QGridLayout()

        self.label = QtWidgets.QLabel()
        self.label.setPixmap(self.pixmap)

        self.pixmap2 = self.pixmap.scaled(
            int(self.sizeObject.width() * self.size),
            int(self.sizeObject.height() * self.size),
        )
        self.label.setPixmap(self.pixmap2)

        self.scalid_in = QtWidgets.QPushButton("масштаб увеличить", self)
        self.scalid_in.clicked.connect(self.scaled_in_event)
        self.scalid_from = QtWidgets.QPushButton("масштаб уменьшить", self)
        self.scalid_from.clicked.connect(self.scalid_from_event)

        self.grid.addWidget(self.scalid_in, 1, 1)
        self.grid.addWidget(self.scalid_from, 1, 2)

        scroll = QtWidgets.QScrollArea()
        scroll.setWidget(self.label)
        scroll.setWidgetResizable(True)
        self.grid.addWidget(scroll, 2, 1, 1, 14)

        self.setLayout(self.grid)

    def scaled_in_event(self):
        self.size += 0.1
        self.scaled_event()

    def scalid_from_event(self):
        if self.size > 0.5:
            self.size -= 0.1
            self.scaled_event()

    def scaled_event(self):
        self.pixmap2 = self.pixmap.scaled(
            int(self.sizeObject.width() * self.size),
            int(self.sizeObject.height() * self.size),
        )
        self.label.setPixmap(self.pixmap2)


class class_immages_in_widget_lvl_2(QtWidgets.QWidget):
    def __init__(self, names):
        super().__init__()
        self.setWindowTitle(names[0])

        self.tab = QtWidgets.QTabWidget()

        for item in names:

            self.menu_widget = class_image_widget(item)

            self.tab.addTab(self.menu_widget, item)

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.tab)
        self.setLayout(self.grid)


class class_immages_in_widget(QtWidgets.QWidget):
    def __init__(self, names):
        super().__init__()
        self.setWindowTitle(names[0])

        self.tab = QtWidgets.QTabWidget()

        for item in names[1:]:
            if type(item) == str:

                self.menu_widget = class_image_widget(item)
                self.tab.addTab(class_image_widget(item), item)
            else:

                self.menu_widget = class_immages_in_widget_lvl_2(item)
                self.tab.addTab(self.menu_widget, item[0])

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.tab)
        self.setLayout(self.grid)


class Menu_list:
    def menu_list(self):
        menulist = self.menuBar()
        self.setWindowIcon(QtGui.QIcon("train.png"))

        file = QtWidgets.QMenu("Файл", self)
        exit_buttom = QtWidgets.QAction("Выход", self)
        exit_buttom.triggered.connect(self.exit_event)
        file.addAction(exit_buttom)

        ARM = QtWidgets.QMenu("АРМ", self)

        moving_car = QtWidgets.QAction("Движение вагонов(обр.)", self)
        moving_car.triggered.connect(self.moving_car_event)
        ARM.addAction(moving_car)

        ARM_of_a_commodity_cashier = QtWidgets.QAction(
            "АРМ товарного кассира(обр.)", self
        )
        ARM_of_a_commodity_cashier.triggered.connect(
            self.ARM_of_a_commodity_cashier_event
        )
        ARM.addAction(ARM_of_a_commodity_cashier)

        ARM_of_a_commodity_cashier2 = QtWidgets.QAction("АРМ товарного кассира", self)
        ARM_of_a_commodity_cashier2.triggered.connect(
            lambda: self.images_wdiget(
                [
                    "АРМ товарного кассира",
                    [
                        "АРМ товарного кассира",
                        "Форма редактирования информации по вагону",
                    ],
                ]
            )
        )
        ARM.addAction(ARM_of_a_commodity_cashier2)

        wagon_weighing = QtWidgets.QAction("Сведения о перевеске вагонов(обр.)", self)
        wagon_weighing.triggered.connect(self.wagon_weighing_event)
        ARM.addAction(wagon_weighing)

        technical_condition = QtWidgets.QAction(
            "Техническое состояние вагонов и их дислокация(обр.)", self
        )
        technical_condition.triggered.connect(self.technical_condition_event)
        ARM.addAction(technical_condition)

        windows = QtWidgets.QMenu("Окна", self)

        menulist.addMenu(file)
        menulist.addMenu(ARM)

        menulist.addMenu(windows)

    def images_wdiget(self, names):
        self.menu_widget = class_immages_in_widget(names)
        self.mdiArea.addSubWindow(self.menu_widget)
        self.menu_widget.show()

    def image_wdiget(self, name):
        self.menu_widget = class_image_widget(name)
        self.mdiArea.addSubWindow(self.menu_widget)
        self.menu_widget.show()

    def moving_car_event(self):

        self.menu_widget = class_an_approach()
        self.menu_widget.setWindowTitle("Движене вагонов")
        self.menu_widget.setWindowIcon(QtGui.QIcon("train.png"))
        self.mdiArea.addSubWindow(self.menu_widget)
        self.menu_widget.show()

    def ARM_of_a_commodity_cashier_event(self):
        self.menu_widget = class_commodity_cashiers_arm()
        self.menu_widget.setWindowTitle("АРМ товарного кассира")
        self.menu_widget.setWindowIcon(QtGui.QIcon("train.png"))
        self.mdiArea.addSubWindow(self.menu_widget)
        self.menu_widget.show()

    def wagon_weighing_event(self):
        self.menu_widget = class_wagon_weighing()
        self.menu_widget.setWindowTitle("Сведения о перевеске вагонов")
        self.menu_widget.setWindowIcon(QtGui.QIcon("train.png"))
        self.mdiArea.addSubWindow(self.menu_widget)
        self.menu_widget.show()

    def technical_condition_event(self):
        self.menu_widget = class_technical_condition()
        self.menu_widget.setWindowTitle("Техническое состояние вагонов и их дислокация")
        self.menu_widget.setWindowIcon(QtGui.QIcon("train.png"))
        self.mdiArea.addSubWindow(self.menu_widget)
        self.menu_widget.show()

    def vagon_report_event(self):
        self.menu_widget = class_availability_of_wagons()
        self.menu_widget.setWindowTitle("Наличие вагонов")
        self.menu_widget.setWindowIcon(QtGui.QIcon("train.png"))
        self.mdiArea.addSubWindow(self.menu_widget)
        self.menu_widget.show()

    def exit_event(self):
        print("Приложение закрыто.")
        sys.exit(app.exec_())


class MainWindow(QtWidgets.QMainWindow, Menu_list):
    def __init__(self):
        super().__init__()

        app.setStyle("fusion")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(222, 225, 230))  
        palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(255, 255, 255))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Text, QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(230, 225, 230))
        palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(0, 0, 0))
        palette.setColor(QtGui.QPalette.BrightText, QtGui.QColor(255, 0, 0))
        palette.setColor(
            QtGui.QPalette.Highlight, QtGui.QColor(192, 195, 200)
        )  
        palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
        app.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setLayout(QtWidgets.QVBoxLayout(self.centralwidget))

        self.mdiArea = QtWidgets.QMdiArea()

        self.centralwidget.layout().addWidget(self.mdiArea)
        self.menu_list()




app = QtWidgets.QApplication(sys.argv)
app.setApplicationName("СРПВ")
w = MainWindow()
w.show()
sys.exit(app.exec_())
