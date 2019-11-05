import unittest
from Calculator import Calculator
from CsvReader import CsvReader
import math
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        test_data = CsvReader('src/addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CsvReader('src/subtraction.csv').data
        for row in test_data:
            print(row)
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiply_method_calculator(self):
        test_data = CsvReader('src/multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division_method_calculator(self):
        test_data = CsvReader('src/division.csv').data
        for row in test_data:
            result =self.calculator.div(int(row['Value 1']), int(row['Value 2']))
            result = round(result,5)
            self.assertEqual(result, round(float(row['Result']),5))
            #self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_method_calculator(self):
        test_data = CsvReader('src/square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(int(row['Value 1'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_sqrt_method_calculator(self):
        test_data = CsvReader('src/squareroot.csv').data
        for row in test_data:
            result = self.calculator.sqrt(int(row['Value 1']))
            result = round(result)
            self.assertEqual(result, round(float(row['Result'])))
        # self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()