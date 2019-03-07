import unittest
from src.warmup import counting_valleys, jump_clouds, sock_merchant


class TestApp(unittest.TestCase):

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

    def test_jump_clouds(self):
        self.assertEqual(jump_clouds([0, 0, 0, 1, 0, 0]), 3)
        self.assertEqual(jump_clouds([0, 1, 0, 0, 0, 1, 0]), 3)
        self.assertEqual(jump_clouds([0, 0, 1, 0, 0, 1, 0]), 4)

    def test_sock_merchant(self):
        potential_pairs = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        self.assertEqual(sock_merchant(ar=potential_pairs), 3)