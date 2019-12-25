# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(591, 431)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 591, 431))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.tableWidgetCreate = QtWidgets.QTableWidget(self.formLayoutWidget)
        self.tableWidgetCreate.setObjectName("tableWidgetCreate")
        self.tableWidgetCreate.setColumnCount(0)
        self.tableWidgetCreate.setRowCount(0)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.tableWidgetCreate)
        self.btn_create = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_create.setObjectName("btn_create")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.btn_create)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.comboBox)
        self.btn_load = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_load.setObjectName("btn_load")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.btn_load)
        self.tableWidgetEdit = QtWidgets.QTableWidget(self.formLayoutWidget)
        self.tableWidgetEdit.setObjectName("tableWidgetEdit")
        self.tableWidgetEdit.setColumnCount(0)
        self.tableWidgetEdit.setRowCount(0)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.tableWidgetEdit)
        self.btn_edit = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_edit.setObjectName("btn_edit")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.btn_edit)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Создать/Изменить"))
        self.label.setText(_translate("Form", " Создать:"))
        self.btn_create.setText(_translate("Form", "Создать"))
        self.label_2.setText(_translate("Form", "Изменить:"))
        self.btn_load.setText(_translate("Form", "Загрузить элемент"))
        self.btn_edit.setText(_translate("Form", "Изменить"))
        self.pushButton.setText(_translate("Form", "Перейти к просмотру"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
