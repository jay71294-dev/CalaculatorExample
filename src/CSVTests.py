import unittest
from CsvReader import CsvReader
from Calculator import Calculator



class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('')



if __name__ == '__main__':
    unittest.main()