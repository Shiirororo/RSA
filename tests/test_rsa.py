import unittest
from unittest.mock import patch
from RSA.rsa import RSA


def make_rsa_auto():
    with patch("builtins.input", return_value="n"):
        return RSA()


class TestRSA(unittest.TestCase):
    def test_key_shapes(self):
        rsa = make_rsa_auto()
        e, n_public = rsa.public_key
        d, n_private = rsa.private_key

        self.assertIsInstance(e, int)
        self.assertIsInstance(d, int)
        self.assertEqual(n_public, n_private)

    def test_encrypt_decrypt_round_trip(self):
        rsa = make_rsa_auto()
        _, n = rsa.public_key
        message = n - 1

        ciphertext = rsa.encrypt(message)
        decrypted = rsa.decrypt(ciphertext)

        self.assertEqual(decrypted, message)

    def test_manual_input(self):
        # Small known primes for fast testing
        p, q, e = 61, 53, 17
        inputs = iter(["y", str(p), str(q), str(e)])
        with patch("builtins.input", lambda _: next(inputs)):
            rsa = RSA()

        self.assertEqual(rsa.public_key[0], e)
        self.assertEqual(rsa.public_key[1], p * q)

        message = 42
        self.assertEqual(rsa.decrypt(rsa.encrypt(message)), message)


if __name__ == "__main__":
    unittest.main()
