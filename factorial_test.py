import unittest
from factorial import factorial

class TestSum(unittest.TestCase):

    def test_factorial_1(self):
        self.assertEqual(factorial(3), 6, "3! should be 6")
        self.assertEqual(factorial(4), 24, "4! should be 24")
        self.assertEqual(factorial(5), 120, "5! should be 120")

if __name__ == '__main__':
    unittest.main()
