
import unittest
from coupon import calculate_discount

class TestCoupon(unittest.TestCase):

    def test_normal_discount(self):
        self.assertEqual(calculate_discount(100, 20), 80)

    def test_zero_discount(self):
        self.assertEqual(calculate_discount(100, 0), 100)

    def test_full_discount(self):
        self.assertEqual(calculate_discount(100, 100), 0)

    def test_negative_price(self):
        self.assertEqual(calculate_discount(-10, 20), 0)

    def test_invalid_discount(self):
        self.assertEqual(calculate_discount(100, 120), 100)

if __name__ == "__main__":
    unittest.main()
