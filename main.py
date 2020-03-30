import sys
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore

from MainWindow import *
from csv_parser import CsvReader


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.file_dialog)

        self.thread = QtCore.QThread()
        self.current_reader = CsvReader()
        self.current_reader.moveToThread(self.thread)
        self.current_reader.dataframe_table.connect(self.set_table_labels)
        self.thread.started.connect(self.current_reader.run)
        self.thread.start()

    @QtCore.pyqtSlot(object)
    def set_table_labels(self, dataframe):
        try:
            headers = dataframe.keys()
        except ValueError:
            QMessageBox.about(self, 'Exception', 'Value error raised while file reading')
            return
        self.ui.label.setText(self.current_reader.get_filepath())
        self.ui.tableWidget.setColumnCount(len(headers))
        self.ui.tableWidget.setRowCount(len(dataframe))
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        for i in range(len(dataframe)):
            for j in range(len(dataframe.columns)):
                self.ui.tableWidget.setItem(
                    i, j,
                    QtWidgets.QTableWidgetItem(str(dataframe.iloc[i, j]))
                                           )
        self.ui.tableWidget.resizeColumnsToContents()

    def file_dialog(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', '')[0]
        try:
            self.current_reader.change_file(fname)
            self.current_reader.run()
        except Exception as e:
            print(f'{e} Some exception')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
