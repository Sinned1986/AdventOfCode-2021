import unittest

import adventofcode.puzzle.day01
import adventofcode.puzzle.day02
import adventofcode.puzzle.day03
import adventofcode.puzzle.day04
import adventofcode.puzzle.day05
import adventofcode.puzzle.day06


class RegressionTest(unittest.TestCase):

    def test_day1_a(self):
        self.assertEqual(adventofcode.puzzle.day01.day01a(), 1688)

    def test_day1_b(self):
        self.assertEqual(adventofcode.puzzle.day01.day01b(), 1728)

    def test_day2_a(self):
        self.assertEqual(adventofcode.puzzle.day02.day02a(), 1813801)

    def test_day2_b(self):
        self.assertEqual(adventofcode.puzzle.day02.day02b(), 1960569556)

    def test_day3_a(self):
        self.assertEqual(adventofcode.puzzle.day03.day03a(), 3985686)

    def test_day3_b(self):
        self.assertEqual(adventofcode.puzzle.day03.day03b(), 2555739)

    def test_day4_a(self):
        self.assertEqual(adventofcode.puzzle.day04.day04a(), 65325)

    def test_day4_b(self):
        self.assertEqual(adventofcode.puzzle.day04.day04b(), 4624)

    def test_day5_a(self):
        self.assertEqual(adventofcode.puzzle.day05.day05a(), 6311)

    def test_day5_b(self):
        self.assertEqual(adventofcode.puzzle.day05.day05b(), 19929)

    def test_day6_a(self):
        self.assertEqual(adventofcode.puzzle.day06.day06a(), 380758)

    def test_day6_b(self):
        self.assertEqual(adventofcode.puzzle.day06.day06b(), 1710623015163)


if __name__ == '__main__':
    unittest.main()
