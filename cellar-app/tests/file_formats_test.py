import unittest
from parameterized import parameterized
from cellar_backend.permanency.csv_handler import CsvHandler
import os
import csv

class FileFormatsTests(unittest.TestCase):

    def test_should_create_a_csv_file_in_default_location(self):
        filename = 'a'
        handler = CsvHandler()
        handler.save(filename)
        path_to_file = os.path.join(os.path.expanduser('~'),'Documents',filename+'.csv' )
        assert os.path.exists(path_to_file)
        os.remove(path_to_file)

    def test_should_create_a_csv_file_any_user_location(self):
        filename = 'a'
        folder = 'any'
        handler = CsvHandler()
        handler.save(filename, folder)
        path_to_file = os.path.join(os.path.expanduser('~'), folder, filename+'.csv' )
        assert os.path.exists(path_to_file)
        os.remove(path_to_file)

    def test_should_create_a_file_given_name(self):
        filename = 'given'
        handler = CsvHandler()
        handler.save(filename)
        path_to_file = os.path.join(os.path.expanduser('~'), 'Documents', filename+'.csv' )
        assert os.path.exists(path_to_file)
        os.remove(path_to_file)

    def test_should_save_line(self):
        filename = 'a'
        content = [['test', 'content']]
        handler = CsvHandler()
        handler.save(filename, content = content)
        path_to_file = os.path.join(os.path.expanduser('~'),'Documents',filename+'.csv' )
        rows_no = self.count_rows_in_csv(path_to_file)
        assert rows_no==1
        os.remove(path_to_file)

    def test_should_save_multiple_rows(self):
        filename = 'a'
        content = [['test', 'content'], ['second', 'line']]
        handler = CsvHandler()
        handler.save(filename, content=content)
        path_to_file = os.path.join(os.path.expanduser('~'), 'Documents', filename + '.csv')
        rows_no = self.count_rows_in_csv(path_to_file)
        assert rows_no==2
        os.remove(path_to_file)

    def test_should_save_accurate_content(self):
        filename = 'a'
        content = [['test']]
        handler = CsvHandler()
        handler.save(filename, content=content)
        path_to_file = os.path.join(os.path.expanduser('~'), 'Documents', filename + '.csv')
        with open(path_to_file, newline= '') as csv_file:
            read_content = csv.reader(csv_file)
            counter = 0
            for row in read_content:
                assert content[counter] == row
                counter += 1
        os.remove(path_to_file)


    def count_rows_in_csv(self, path_to_file):
        with open(path_to_file, newline= '') as csv_file:
            read_content = csv.reader(csv_file)
            counter = 0
            for row in read_content:
                counter += 1
            return counter
