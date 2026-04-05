import unittest
from Math.math import Math   # sửa path theo project của bạn

class TestMath(unittest.TestCase):



# Test GCD MODULE:



    # Test cơ bản
    def test_gcd_basic(self):
        self.assertEqual(Math.gcd(48, 18), 6)
        self.assertEqual(Math.gcd(7, 3), 1)

    # Test với số 0
    def test_gcd_with_zero(self):
        self.assertEqual(Math.gcd(0, 5), 5)
        self.assertEqual(Math.gcd(5, 0), 5)

    # Test số giống nhau
    def test_gcd_same_numbers(self):
        self.assertEqual(Math.gcd(10, 10), 10)

    # Test số lớn
    def test_gcd_large_numbers(self):
        self.assertEqual(Math.gcd(1000000, 2), 2)

    # Test tính giao hoán
    def test_gcd_commutative(self):
        self.assertEqual(Math.gcd(48, 18), Math.gcd(18, 48))

    # Test nhiều case random
    def test_gcd_random(self):
        import random
        for _ in range(100):
            a = random.randint(1, 1000)
            b = random.randint(1, 1000)
            self.assertEqual(Math.gcd(a, b), Math.gcd(b, a))


if __name__ == "__main__":
    unittest.main()