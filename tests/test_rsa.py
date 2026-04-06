import unittest

from RSA.rsa import RSA


class TestRSA(unittest.TestCase):
    def test_key_shapes(self):
        rsa = RSA()
        e, n_public = rsa.public_key
        d, n_private = rsa.private_key

        self.assertIsInstance(e, int)
        self.assertIsInstance(d, int)
        self.assertEqual(n_public, n_private)

    def test_encrypt_decrypt_round_trip(self):
        rsa = RSA()
        _, n = rsa.public_key
        message = n - 1

        ciphertext = rsa.encrypt(message)
        decrypted = rsa.decrypt(ciphertext)

        self.assertEqual(decrypted, message)


if __name__ == "__main__":
    unittest.main()