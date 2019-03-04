import unittest
from src.app import sock_merchant, counting_valleys


class TestApp(unittest.TestCase):

    def test_sock_merchant(self):
        potential_pairs = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        self.assertEqual(sock_merchant(ar=potential_pairs), 3)

    def test_counting_valleys(self):
        """
        UDDDUDUU

        _/\      _
           \    /
            \/\/
        """
        valleys1 = 'UDDDUDUU'
        self.assertEqual(counting_valleys(s=valleys1), 1)
        valleys2 = 'DDUUDDUDUUUD'
        self.assertEqual(counting_valleys(s=valleys2), 2)


        """
        UDUUUDUDDD
             /\/\
            /    \
        _/\/      \
        """
        # hills_valleys2 = 'UDUUUDUDDD'
        # self.assertEqual(counting_valleys(n=42, s=hills_valleys2), 0)
