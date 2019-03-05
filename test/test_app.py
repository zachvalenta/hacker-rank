import unittest
from src.app import sock_merchant, counting_valleys


class TestApp(unittest.TestCase):

    def test_sock_merchant(self):
        potential_pairs = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        self.assertEqual(sock_merchant(ar=potential_pairs), 3)

    def test_counting_valleys(self):
        """
        _/\_______
           \    /
            \/\/
        """
        valleys1 = 'UDDDUDUU'
        self.assertEqual(counting_valleys(s=valleys1), 1)

        """
        __________
        \/\      /
           \  /\/
            \/        
        """
        valleys2 = 'DDUUDDUDUUUD'
        self.assertEqual(counting_valleys(s=valleys2), 2)

        """
        UDUUUDUDDD

             /\/\
            /    \
        _/\/______\
        """
        valleys3 = 'UDUUUDUDDD'
        self.assertEqual(counting_valleys(s=valleys3), 0)

        """
        __________________
        \/\      /
           \  /\/
            \/
        """
        valleys4 = 'DUDDDUUDUU'
        self.assertEqual(counting_valleys(s=valleys4), 2)
