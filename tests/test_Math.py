import unittest
from Math.math import Math   # sửa path theo project của bạn

class TestGCDMath(unittest.TestCase):



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

class TestIsPrime(unittest.TestCase):

    test_primes = [
        2, 3, 5, 7, 11,
        101, 103, 1009,
        7919,
        104729,
    ]

    test_composites = [
        1, 4, 6, 8, 9, 10,
        15, 21, 25, 27,
        100, 1024,
        9999,
        104730,
    ]

    def test_primes_are_prime(self):
        for n in self.test_primes:
            with self.subTest(n=n):
                self.assertTrue(Math.isPrime(n), f"{n} should be prime")

    def test_composites_are_not_prime(self):
        for n in self.test_composites:
            with self.subTest(n=n):
                self.assertFalse(Math.isPrime(n), f"{n} should not be prime")


if __name__ == "__main__":
    unittest.main()