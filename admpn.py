from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import admin
import psycopg2
from config import host, user, password, db_name

class AdminPanel(QtWidgets.QMainWindow, admin.Ui_Dialog):
    def __init__(self, parent=None):
        super(AdminPanel, self).__init__(parent)
        self.setupUi(self)
        self.send_button.clicked.connect(self.about_prod)

    def about_prod(self):
        name = self.name.text()
        desc = self.description.text()
        price = self.price.text()
        try:
            connection = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                database=db_name
            )
            with connection.cursor() as cursor:
                cursor.execute(f"""INSERT INTO product (name, description, price) VALUES ({name}, {desc}, {price});""")
            connection.commit()
        except Exception as _ex:
            print('[INFO]', _ex)

        finally:
            if psycopg2.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name
            ):
                psycopg2.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=db_name
                ).close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = AdminPanel()
    a.show()
    app.exec_()