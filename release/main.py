import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QWidget, QMessageBox
from UI.main_ui import Ui_MainWindow
from UI.addEditCoffeeForm import Ui_Form


class Coffee(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("data/coffee.db")
        cur = self.con.cursor()
        result = list(cur.execute("Select * from Coffee").fetchall())
        for i in range(len(result)):
            result[i] = list(result[i])
            result[i][2] = cur.execute(f'select degree from roasting_degrees '
                                       f'where id = {result[i][2]}').fetchone()[0]
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(7)
        self.titles = 'ID', 'Название сорта', 'Степень обжарки', \
                      'Молотый/В зёрнах', 'Описание вкуса', 'Цена', 'Объём упаковки'
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.resizeColumnsToContents()
        self.pushButton.clicked.connect(self.edit_show)

    def edit_show(self):
        self.xx = AddEdit(self.con)
        self.xx.show()
        self.hide()


class AddEdit(QWidget, Ui_Form):
    def __init__(self, con):
        super().__init__()
        self.setupUi(self)
        self.con = con
        self.cur = con.cursor()
        self.btn_create.clicked.connect(self.create_n)
        self.btn_load.clicked.connect(self.load)
        self.btn_edit.clicked.connect(self.edit)
        self.pushButton.clicked.connect(self.back)
        self.names = [i[0] for i in self.cur.execute('select name from Coffee').fetchall()]
        self.tableWidgetEdit.setRowCount(1)
        self.tableWidgetCreate.setRowCount(1)
        self.tableWidgetEdit.setColumnCount(6)
        self.tableWidgetCreate.setColumnCount(6)
        self.nodes = 'name', 'degree', 'grind', 'taste', 'price', 'size'
        self.titles = 'Название сорта', 'Степень обжарки(от 1 до 9)', \
                      'Молотый/В зёрнах', 'Описание вкуса', 'Цена', 'Объём упаковки(в кг)'
        self.tableWidgetEdit.setHorizontalHeaderLabels(self.titles)
        self.tableWidgetCreate.setHorizontalHeaderLabels(self.titles)
        for name in self.names:
            self.comboBox.addItem(name)

    def back(self):
        self.coffee = Coffee()
        self.coffee.show()
        self.hide()

    def load(self):
        self.name = self.comboBox.currentText()
        if self.comboBox.currentText():
            table = self.cur.execute(f'select * from Coffee where name = "{self.name}"').fetchone()
            self.id = table[0]
            for j, val in enumerate(table[1::]):
                self.tableWidgetEdit.setItem(0, j, QTableWidgetItem(str(val)))
            self.tableWidgetEdit.resizeColumnsToContents()

    def is_completed(self, table):
        return all(list(map(lambda a: a is not None, table)))

    def warn(self):
        return QMessageBox.critical(self, 'Ошибка', 'Не все поля заполнены. Повторите попытку.',
                                    buttons=QMessageBox.Ok)

    def ok(self):
        return QMessageBox.information(self, 'Успех', f'Действие выполнено удачно',
                                       buttons=QMessageBox.Ok)

    def edit(self):
        row = []
        for j in range(6):
            item = self.tableWidgetEdit.item(0, j)
            if item:
                row.append(item.text())
            else:
                row.append(None)
        if self.is_completed(row):
            row = list(map(lambda a: "'" + a + "'", row))
            for i in range(len(row)):
                self.cur.execute(f'update Coffee \n'
                                 f'SET {self.nodes[i]} = {row[i]} where id = "{self.id}"')
            self.con.commit()
            self.comboBox.addItem(row[0][1:-1])
            self.comboBox.removeItem(self.comboBox.findText(self.name))
            self.comboBox.setCurrentIndex(len(self.comboBox) - 1)
            self.ok()
        else:
            self.warn()

    def create_n(self):
        row = []
        for j in range(6):
            item = self.tableWidgetCreate.item(0, j)
            if item:
                row.append(item.text())
            else:
                row.append(None)
        if self.is_completed(row):
            row = list(map(lambda a: "'" + a + "'", row))
            self.cur.execute(f'insert into Coffee({", ".join(self.nodes)}) values({", ".join(row)})')
            self.comboBox.addItem(row[0][1:-1])
            self.con.commit()
            self.ok()
        else:
            self.warn()

        def error(self):
            raise Exception('Неожиданная ошибкочка')


def my_excepthook(type, value, tback):
    a = QMessageBox.critical(ex, "Ошибка", str(value),
                             QMessageBox.Cancel)
    sys.__excepthook__(type, value, tback)


sys.excepthook = my_excepthook


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())