from PyQt5 import QtCore, QtGui, QtWidgets
from Class_filtr import *
from Class_for_request_directory import *
import os
from openpyxl import Workbook
import csv


class class_technical_condition_widget(QtWidgets.QWidget, stack_level_1, stack_level_2):
    def __init__(self, table):
        super().__init__()
        self.name = "Сведения о перевеске вагонов"

        self.grid = QtWidgets.QGridLayout()

        self.btn_update = QtWidgets.QPushButton("", self)
        self.btn_update.setIcon(QtGui.QIcon("arrows arraund blue.png"))
        self.btn_update.clicked.connect(self.write)
        self.grid.addWidget(self.btn_update, 1, 1)

        self.lens = QtWidgets.QPushButton("", self)
        self.lens.setIcon(QtGui.QIcon("excel.png"))
        self.grid.addWidget(self.lens, 1, 2)

        self.table = table
        self.grid.addWidget(self.table, 2, 1, 34, 30)

        self.table2 = QtWidgets.QTableWidget()
        self.table2.setColumnCount(2)
        self.table2.setRowCount(2)
        self.table2.setHorizontalHeaderLabels(["Дата прибытия", "Дата убытия"])
        self.grid.addWidget(self.table2, 2, 31, 2, 35)

        self.btn_update2 = QtWidgets.QPushButton("", self)
        self.btn_update2.setIcon(QtGui.QIcon("arrows arraund blue.png"))
        self.grid.addWidget(self.btn_update2, 4, 31, 4, 35)

        items = [
            "Собственик:",
            "Дата плановго ремонта:",
            "Груз:",
            "Станц.Наз.:",
            "Станц.соверш.операции:",
            "Дорога:",
            "Дата операции:",
            "Дата ответа:",
            "Вид опрации:",
            "Простой выгрузка(кол-во сут.):",
            "Простой выгрузка(руб.):",
            "Простой погрузка(кол-во сут.):",
            "Дата перед.в аренду:",
        ]

        for i in range(len(items)):

            self.text = QtWidgets.QLabel()
            self.text.setText(items[i])
            self.grid.addWidget(self.text, i + 6, 31, i + 6, 35)

        self.setLayout(self.grid)


class class_technical_condition(
    QtWidgets.QWidget, class_filtr, class_for_request_directory
):
    def __init__(self):
        super().__init__()

        self.setObjectName("button1")

        self.btn_update = QtWidgets.QPushButton("Обновить все", self)
        self.btn_update.clicked.connect(self.write)

        self.dict_class = {
            "Сведения о перевеске вагонов": class_technical_condition_widget
        }

        self.dict_table = {"Сведения о перевеске вагонов": None}

        self.grid = QtWidgets.QGridLayout()
        self.write_table()

        self.grid.addWidget(self.btn_update, 1, 1)

        self.setLayout(self.grid)

    def write_table(self):
        for i in self.dict_table:
            self.dict_table[i] = QtWidgets.QTableWidget(self)
            self.dict_table[i].setColumnCount(0)
            self.dict_table[i].setRowCount(0)

            self.table_of_contents = self.dict_table[i].horizontalHeader()
            self.table_of_contents.sectionClicked.connect(self.click_table_of_contents)

            item = self.dict_class[i](self.dict_table[i])

            self.grid.addWidget(item, 2, 1, 1, 14)

    def write(self):
        self.dict_list = {
            "Сведения о перевеске вагонов": list(
                csv.reader(open("Сведения о перевеске вагонов.csv", "r"), delimiter=";")
            )
        }

        for i in self.dict_list:
            self.write_list(i, self.dict_list[i])
