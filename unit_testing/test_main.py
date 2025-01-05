import unittest
from main import Calculator


class TestCalc(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(10, 5), 15)

    def test_add_failure(self):
        self.assertNotEqual(self.calc.add(10, 5), 20)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_divide_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
