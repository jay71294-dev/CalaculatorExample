import unittest
from Calculator import  Calculator

class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_results_property_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.result,0)

    def test_add_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_subtract_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(2, 2), 0)
        self.assertEqual(calculator.result, 0)

    def test_multiplication_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(2, 2), 4)
        self.assertEqual(calculator.result, 4)

    def test_division_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.div(4, 2), 2)
        self.assertEqual(calculator.result, 2)

    def test_square_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.square(4), 16)
        self.assertEqual(calculator.result, 16)

    def test_sqrt_method_calculator(self):
        calculator = Calculator()
        self.assertEqual(calculator.sqrt(9), 3)
        self.assertEqual(calculator.result, 3)

if __name__ == '__main__':
    unittest.main()
