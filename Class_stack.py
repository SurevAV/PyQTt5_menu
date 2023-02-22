from PyQt5 import QtCore, QtGui, QtWidgets
import csv


class stack_level_1:
    def non_none(self, item):
        if item == None:
            return ""
        else:
            return item

    def len_string(self, x):
        for i in range(20 - len(x)):
            x += " "
        return x


class stack_level_2:
    def write(self):
        dict_list = list(csv.reader(open(self.name + ".csv"), delimiter=";"))

        self.write_list(dict_list)

    def write_list(self, insert_list):

        self.table.setColumnCount(len(insert_list[0]))
        self.table.setRowCount(len(insert_list) - 1)
        for row in range(1, len(insert_list)):
            for column in range(len(insert_list[0])):
                self.table.setItem(
                    row - 1,
                    column,
                    QtWidgets.QTableWidgetItem(self.non_none(insert_list[row][column])),
                )

        table_of_contents = []
        for j in range(len(insert_list[0])):
            table_of_contents.append(insert_list[0][j])  
            self.table.setColumnWidth(j, len(table_of_contents[-1]) * 10)
        self.table.setHorizontalHeaderLabels(table_of_contents)
