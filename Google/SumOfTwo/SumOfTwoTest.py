import unittest
import SumOfTwo


class TestSumOfTwo(unittest.TestCase):

    def test_1(self):
        self.assertEqual(SumOfTwo.SumOfTwo(
            a=[0, 0, -5, 30212],
            b=[-10, 40, -3, 9],
            v=-8),
            True)

    def test_2(self):
        self.assertEqual(SumOfTwo.SumOfTwo(
            a=[1, 2, 3],
            b=[10, 20, 30, 40],
            v=42),
            True)

    def test_3(self):
        self.assertEqual(SumOfTwo.SumOfTwo(
            a=[1, 2, 3, 4],
            b=[9, 8, 7, 6],
            v=9999),
            False)

    def test_4(self):
        self.assertEqual(SumOfTwo.SumOfTwo(
            a=[45, 49, 6, 1, 14, 99, 40, 96, 11, 41, 100, 20, 7, 51, 35, 53, 88, 32,
                37, 31, 84, 70, 38, 71, 22, 42, 62, 29, 4, 3, 92, 8, 26, 59, 54, 12],
            b=[50, 95, 55, 68, 2, 24, 28, 91, 23, 34, 83, 58, 30, 89, 87, 17, 79, 78, 5, 44, 61, 18, 16, 73, 57, 90,
                48, 64, 19, 75, 80, 56, 69, 93, 27, 67, 13, 33, 60, 9, 65, 94, 82, 25, 97, 72, 76, 77, 47, 52, 81, 10],
            v=164),
            True)


if __name__ == '__main__':
    unittest.main()
