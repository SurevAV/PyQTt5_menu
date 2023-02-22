from PyQt5 import QtCore, QtGui, QtWidgets


class class_filtr:
    def click_table_of_contents(self, index):
        for i in self.dict_table:
            if self.dict_table[i].isVisible():

                self.for_filtr = self.dict_table[i]
                self.for_filtr_index = index

                cursor_position = QtGui.QCursor.pos()
                menu = QtWidgets.QMenu()
                grid = QtWidgets.QGridLayout()

                self.list_column_filtr = []

                list_items = []
                for j in range(self.dict_table[i].rowCount()):
                    if not self.dict_table[i].isRowHidden(j):
                        item = self.dict_table[i].item(j, index).text()
                        if item not in list_items:
                            list_items.append(item)

                        self.list_column_filtr.append(j)

                list_items = sorted(list_items)

                self.list_check = QtWidgets.QTableWidget(self)
                self.list_check.setColumnCount(2)
                self.list_check.setRowCount(len(list_items))
                for j in range(len(list_items)):
                    self.list_check.setItem(
                        j, 0, QtWidgets.QTableWidgetItem(list_items[j])
                    )
                    item = QtWidgets.QTableWidgetItem()
                    item.setFlags(
                        QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled
                    )
                    item.setCheckState(QtCore.Qt.Unchecked)
                    self.list_check.setItem(j, 1, item)

                btn_ok = QtWidgets.QPushButton("ok", self)
                btn_ok.clicked.connect(self.use_filtr)

                btn_cancel = QtWidgets.QPushButton("cancel", self)
                btn_cancel.clicked.connect(self.cancel_filtr)

                self.btn_select = QtWidgets.QPushButton("select", self)
                self.btn_select.clicked.connect(self.select_in_filtr)

                clear_filtr = QtWidgets.QPushButton("clear_filtr", self)
                clear_filtr.clicked.connect(self.clear_filtr_full)

                self.input_find = QtWidgets.QLineEdit(self)
                self.input_find.setText("")
                self.input_find.textChanged.connect(self.change_string_find)

                self.input_operator = QtWidgets.QLineEdit(self)
                self.input_operator.setText("==")

                grid.addWidget(self.input_find, 1, 0, 1, 3)
                grid.addWidget(self.input_operator, 1, 3)
                grid.addWidget(btn_ok, 0, 0)
                grid.addWidget(btn_cancel, 0, 1)
                grid.addWidget(self.btn_select, 0, 2)
                grid.addWidget(clear_filtr, 0, 3)
                grid.addWidget(self.list_check, 2, 0, 80, 4)

                label_1 = QtWidgets.QLabel("", self)
                grid.addWidget(label_1, 0, 4)
                grid.addWidget(label_1, 81, 0)
                grid.addWidget(label_1, 81, 4)
                menu.setLayout(grid)

                menu.exec_(
                    QtCore.QPoint(self.shift(cursor_position.x()), cursor_position.y())
                )

    def shift(self, i):
        if i < 1500:
            return i
        else:
            return 1500

    def use_filtr(self):
        list_filtr = []
        for i in range(self.list_check.rowCount()):
            if self.list_check.item(i, 1).checkState() == QtCore.Qt.Checked:
                list_filtr.append(self.list_check.item(i, 0).text())

        for i in range(self.for_filtr.rowCount()):
            if self.for_filtr.item(i, self.for_filtr_index).text() not in list_filtr:
                self.for_filtr.setRowHidden(i, True)

    def cancel_filtr(self):
        for i in self.list_column_filtr:
            self.for_filtr.setRowHidden(i, False)

    def select_in_filtr(self):
        if self.btn_select.text() == "select":

            for i in range(self.list_check.rowCount()):
                if not self.list_check.isRowHidden(i):
                    self.list_check.item(i, 1).setCheckState(QtCore.Qt.Checked)
                else:
                    self.list_check.item(i, 1).setCheckState(QtCore.Qt.Unchecked)
            self.btn_select.setText("not_select")
        else:
            for i in range(self.list_check.rowCount()):
                self.list_check.item(i, 1).setCheckState(QtCore.Qt.Unchecked)
            self.btn_select.setText("select")

    def clear_filtr_full(self):
        for i in range(self.for_filtr.rowCount()):
            self.for_filtr.setRowHidden(i, False)

    def change_string_find(self):

        operator_check = ["==", "!=", ">", "<", ">=", "<=", "in", "в"]
        if self.input_operator.text() not in operator_check:
            self.input_operator.setText("==")

        if self.input_operator.text() == "==":
            len_word = len(self.input_find.text())
            for i in range(self.list_check.rowCount()):
                self.list_check.setRowHidden(i, False)
                if (
                    self.list_check.item(i, 0).text()[:len_word]
                    != self.input_find.text()
                ):
                    self.list_check.setRowHidden(i, True)

        if self.input_operator.text() == "!=":
            for i in range(self.list_check.rowCount()):
                self.list_check.setRowHidden(i, False)
                if self.list_check.item(i, 0).text() == self.input_find.text():
                    self.list_check.setRowHidden(i, True)

        if self.input_operator.text() == ">=":
            for i in range(self.list_check.rowCount()):
                self.list_check.setRowHidden(i, False)
                if self.list_check.item(i, 0).text() < self.input_find.text():
                    self.list_check.setRowHidden(i, True)

        if self.input_operator.text() == "<=":
            for i in range(self.list_check.rowCount()):
                self.list_check.setRowHidden(i, False)
                if self.list_check.item(i, 0).text() > self.input_find.text():
                    self.list_check.setRowHidden(i, True)

        if self.input_operator.text() == "<":
            for i in range(self.list_check.rowCount()):
                self.list_check.setRowHidden(i, False)
                if self.list_check.item(i, 0).text() >= self.input_find.text():
                    self.list_check.setRowHidden(i, True)

        if self.input_operator.text() == ">":
            for i in range(self.list_check.rowCount()):
                self.list_check.setRowHidden(i, False)
                if self.list_check.item(i, 0).text() <= self.input_find.text():
                    self.list_check.setRowHidden(i, True)

        if self.input_operator.text() == "in" or self.input_operator.text() == "в":
            for i in range(self.list_check.rowCount()):
                self.list_check.setRowHidden(i, False)
                if self.input_find.text() not in self.list_check.item(i, 0).text():
                    self.list_check.setRowHidden(i, True)
