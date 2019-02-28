import unittest
from src.app import sock_merchant


class TestApp(unittest.TestCase):

    def test_sock_merchant(self):
        potential_pairs = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        self.assertEqual(sock_merchant(n=42, ar=potential_pairs), 3)
