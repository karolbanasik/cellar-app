import os
import csv
from cellar_backend.permanency.i_permanency_handler import IPermanencyHandler


class CsvHandler(IPermanencyHandler):

    def __init__(self):
        self._default_path = os.path.expanduser('~')

    def save(self, name, save_path = None, content = None):
        if save_path is None:
            save_path = os.path.join(self._default_path, 'Documents')
        else:
            save_path = os.path.join(self._default_path, save_path)
        self._make_dir_if_dont_exist(save_path)
        with open(os.path.join(save_path, name + '.csv'), 'w', newline= '') as csv_file:
            if content is not None:
                for line in content:
                    self._add_line(csv_file, line)


    def _add_line(self, file, line):
        writer = csv.writer(file)
        writer.writerow(line)

    def _make_dir_if_dont_exist(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)