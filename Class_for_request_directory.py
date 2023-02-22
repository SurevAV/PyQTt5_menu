from PyQt5 import QtCore, QtGui, QtWidgets
import csv
from Class_stack import *


class class_for_request_directory(stack_level_1):
    def write_table(self):
        for i in self.dict_table:
            self.dict_table[i] = QtWidgets.QTableWidget(self)
            self.dict_table[i].setColumnCount(0)
            self.dict_table[i].setRowCount(0)

            self.table_of_contents = self.dict_table[i].horizontalHeader()
            self.table_of_contents.sectionClicked.connect(self.click_table_of_contents)

            item = self.dict_class[i](self.dict_table[i])

            self.tab.addTab(item, i)

    def write_list(self, i, insert_list):
        self.dict_table[i].setColumnCount(len(insert_list[0]))
        self.dict_table[i].setRowCount(len(insert_list) - 1)
        for row in range(1, len(insert_list)):
            for column in range(len(insert_list[0])):
                self.dict_table[i].setItem(
                    row - 1,
                    column,
                    QtWidgets.QTableWidgetItem(self.non_none(insert_list[row][column])),
                )

        table_of_contents = []
        for j in range(len(insert_list[0])):
            table_of_contents.append(insert_list[0][j])  
            self.dict_table[i].setColumnWidth(j, len(table_of_contents[-1]) * 10)
        self.dict_table[i].setHorizontalHeaderLabels(table_of_contents)
