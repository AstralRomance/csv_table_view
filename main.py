import sys

from MainWindow import *

from csv_parser import CsvReader

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.current_reader = CsvReader()
        self.set_table_labels()

        self.ui.pushButton.clicked.connect(self.file_dialog)

    def set_table_labels(self):
        headers = self.current_reader.get_dataset().keys()
        self.ui.tableWidget.setColumnCount(len(headers))
        self.ui.tableWidget.setRowCount(len(self.current_reader.get_dataset()))
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        for i in range(len(self.current_reader.get_dataset())):
            for j in range(len(self.current_reader.get_dataset().columns)):
                self.ui.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.current_reader.get_dataset().iloc[i, j])))
        self.ui.tableWidget.resizeColumnsToContents()

    def file_dialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]
        self.current_reader.change_file(fname)
        self.set_table_labels()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())