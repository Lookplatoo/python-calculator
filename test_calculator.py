import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    #Add the following test methods to the TestCalculator class:
    def test_add1(self):
        self.assertEqual(self.calc.add(3, 2), 5)
    def test_add2(self):
        self.assertEqual(self.calc.add(6, 2), 8)

    def test_subtract1(self):
         self.assertEqual(self.calc.subtract(2,3), -1)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(5,3), 2)

    def test_multi1(self):
        self.assertEqual(self.calc.multiply(-4, -3), 12)
    def test_multi2(self):
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(-12,-3), 4)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(9,3), 3)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(10,3), 1)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(4,-3), -2)

if __name__ == '__main__':
    unittest.main()
