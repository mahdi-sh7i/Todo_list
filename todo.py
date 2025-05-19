from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QListWidget, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5 import uic
import sqlite3
import sys
from sub import Ui_Dialog  # Adjust the import based on your file structure

# Create a datebase or connect to one
conn = sqlite3.connect('t_list.db')
c = conn.cursor()
c.execute("""CREATE TABLE if not exists todo_list(
          list_item text)
          """)
conn.commit()
conn.close()


class UI(QMainWindow):
    def __init__(self):  # Corrected method name to __init__
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("todo.ui", self)
        # --------------------------------------------
        self.button_add = self.findChild(QPushButton, "but_additem")
        self.button_delete = self.findChild(QPushButton, "but_deleteitem")
        self.button_clear = self.findChild(QPushButton, "but_clearall")
        self.button_save = self.findChild(QPushButton, "but_save")

        self.line = self.findChild(QLineEdit, "lineEdit_additem")
        self.list = self.findChild(QListWidget, "listWidget_mylist")

        # Connect button clicks to methods
        self.button_add.clicked.connect(self.clicker_add)
        self.button_delete.clicked.connect(self.clicker_delete)
        self.button_clear.clicked.connect(self.clicker_clear)
        self.button_save.clicked.connect(self.clicker_save)

        # Grab all the items from the database
        self.grab_all()

        # Show The App
        self.show()

    # --------------------------------------------

    # Grab items from datebase
    def grab_all(self):
        # Create a datebase or connect to one
        conn = sqlite3.connect('t_list.db')
        c = conn.cursor()
        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()
        conn.commit()
        conn.close()

        # Loop thru records and add to screen
        for record in records:
            self.list.addItem(str(record[0]))  # Add the record to the list

    def clicker_add(self):
        item_text = self.line.text()  # Get text from the line edit
        if item_text:  # Check if the input is not empty
            self.list.addItem(item_text)  # Add the item to the list
            self.line.clear()  # Clear the input field after adding

    def clicker_delete(self):
        list_items = self.list.selectedItems()  # Get selected items
        if not list_items:  # If no item is selected, return
            return
        for item in list_items:  # Remove selected items from the list
            self.list.takeItem(self.list.row(item))

    def clicker_clear(self):
        self.list.clear()  # Clear all items from the list

    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.exec_()  # Use exec_() to open as a modal dialog

    # Save To the Datebase
    def clicker_save(self):
        # Create a datebase or connect to one
        conn = sqlite3.connect('t_list.db')
        c = conn.cursor()

        # Delete everything in the database table
        c.execute('DELETE FROM todo_list;', )

        list_item = []
        for index in range(self.list.count()):
            list_item.append(self.list.item(index))

        for item_i in list_item:
            # print(item_i.text())
            # Add stuff to the table
            c.execute("INSERT INTO todo_list VALUES (:item)",
                      {
                          'item': item_i.text(),

                      })

        conn.commit()
        conn.close()

        # Pop Up Box
        self.openWindow()


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
