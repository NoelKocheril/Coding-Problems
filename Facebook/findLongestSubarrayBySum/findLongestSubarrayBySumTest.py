import unittest
from findLongestSubarrayBySum import findLongestSubarrayBySum


class TestSumOfTwo(unittest.TestCase):

    def test_1(self):
        self.assertEqual(
            findLongestSubarrayBySum(
                arr=[1, 2, 3, 7, 5],
                s=12
            ),
            [2, 4])

    def test_2(self):
        self.assertEqual(
            findLongestSubarrayBySum(
                arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                s=15
            ),
            [1, 5])

    def test_3(self):
        self.assertEqual(
            findLongestSubarrayBySum(
                arr=[5, 3, 5, 6, 7],
                s=4
            ),
            [-1])

    def test_4(self):
        self.assertEqual(
            findLongestSubarrayBySum(
                arr=[5, 3, 5, 6, 7],
                s=13
            ),
            [1, 3])


if __name__ == '__main__':
    unittest.main()
