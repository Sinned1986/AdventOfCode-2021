import unittest

import adventofcode.puzzle.day01
import adventofcode.puzzle.day02

class RegressionTest(unittest.TestCase):

    def test_day1_a(self):
        self.assertEqual(adventofcode.puzzle.day01.day01a(), 1688)

    def test_day1_b(self):
        self.assertEqual(adventofcode.puzzle.day01.day01b(), 1728)

    def test_day2_a(self):
        self.assertEqual(adventofcode.puzzle.day02.day02a(), 1813801)

    def test_day2_b(self):
        self.assertEqual(adventofcode.puzzle.day02.day02b(), 1960569556)


if __name__ == '__main__':
    unittest.main()
