import sys

from PyQt5.QtCore import QObject, pyqtSignal
import pandas as pd


class CsvReader(QObject):
    dataframe_table = pyqtSignal(object)

    def __init__(self, filepath=''):
        super().__init__()
        self.filepath = filepath

    def run(self):
        try:
            table_dataframe = pd.read_csv(self.filepath)
            self.dataframe_table.emit(table_dataframe)
        except FileNotFoundError:
            return

    def change_file(self, filepath):
        self.filepath = filepath

    def get_filepath(self):
        return str(self.filepath)
