import unittest
import ProductOfArrayExceptSelf


class TestSumOfTwo(unittest.TestCase):

    def test_1(self):
        self.assertEqual(
            ProductOfArrayExceptSelf.ProductOfArrayExceptSelf(
                [1, 2, 3, 4]),
            [24, 12, 8, 6])

    def test_2(self):
        self.assertEqual(
            ProductOfArrayExceptSelf.ProductOfArrayExceptSelf(
                [-1, 1, 0, -3, 3]),
            [0, 0, 9, 0, 0])

    def test_3(self):
        self.assertEqual(
            ProductOfArrayExceptSelf.ProductOfArrayExceptSelf(
                [32, 2, 1, 6, 4]),
            [48, 768, 1536, 256, 384])

    def test_4(self):
        self.assertEqual(
            ProductOfArrayExceptSelf.ProductOfArrayExceptSelf(
                [1, 2, 3, 4, 5]),
            [120, 60, 40, 30, 24])


if __name__ == '__main__':
    unittest.main()
