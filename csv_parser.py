import sys

import pandas as pd


class CsvReader:
    def __init__(self, filepath='pred_intervals.csv'):
        self.filepath = filepath

    def get_dataset(self):
        return pd.read_csv(self.filepath)

    def change_file(self, filepath):
        self.filepath = filepath

    def get_filepath(self):
        return str(self.filepath)
