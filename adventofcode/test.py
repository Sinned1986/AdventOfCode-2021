import unittest

import adventofcode.puzzle.day01
import adventofcode.puzzle.day02
import adventofcode.puzzle.day03
import adventofcode.puzzle.day04
import adventofcode.puzzle.day05
import adventofcode.puzzle.day06
import adventofcode.puzzle.day07
import adventofcode.puzzle.day08
import adventofcode.puzzle.day09
import adventofcode.puzzle.day10
import adventofcode.puzzle.day11
import adventofcode.puzzle.day12
import adventofcode.puzzle.day13
import adventofcode.puzzle.day14
import adventofcode.puzzle.day15

import numpy as np


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

    def test_day7_a(self):
        self.assertEqual(adventofcode.puzzle.day07.day07a(), 359648)

    def test_day7_b(self):
        self.assertEqual(adventofcode.puzzle.day07.day07b(), 100727924)

    def test_day8_a(self):
        self.assertEqual(adventofcode.puzzle.day08.day08a(), 476)

    def test_day8_b(self):
        self.assertEqual(adventofcode.puzzle.day08.day08b(), 1011823)

    def test_day9_a(self):
        self.assertEqual(adventofcode.puzzle.day09.day09a()[0], 528)

    def test_day9_b(self):
        self.assertEqual(adventofcode.puzzle.day09.day09b()[0], 920448)

    def test_day10_a(self):
        self.assertEqual(adventofcode.puzzle.day10.day10a(), 394647)

    def test_day10_b(self):
        self.assertEqual(adventofcode.puzzle.day10.day10b(), 2380061249)

    def test_day11_a(self):
        self.assertEqual(adventofcode.puzzle.day11.day11a(), 1700)

    def test_day11_b(self):
        self.assertEqual(adventofcode.puzzle.day11.day11b(), 273)

    def test_day12_a(self):
        self.assertEqual(adventofcode.puzzle.day12.day12a(), 4720)

    def test_day12_b(self):
        self.assertEqual(adventofcode.puzzle.day12.day12b(), 147848)

    def test_day13_a(self):
        self.assertEqual(adventofcode.puzzle.day13.day13a('day/13/input.txt'), 592)

    def test_day13_b(self):
        self.assertEqual(adventofcode.puzzle.day13.day13b('day/13/input.txt'), 'JGAJEFKU')

    def test_day14_a(self):
        self.assertEqual(adventofcode.puzzle.day14.day14a('day/14/example.txt'), 1588)
        self.assertEqual(adventofcode.puzzle.day14.day14a('day/14/input.txt'), 3230)

    def test_day14_b(self):
        self.assertEqual(adventofcode.puzzle.day14.day14b('day/14/input.txt'), 3542388214529)

    def test_day15_a(self):
        self.assertEqual(adventofcode.puzzle.day15.day15a('day/15/example.txt'), 40)
        self.assertEqual(adventofcode.puzzle.day15.day15a('day/15/input.txt'), 472)

    def test_day15_b(self):
        self.assertEqual(adventofcode.puzzle.day15.day15b('day/15/example.txt'), 315)
        self.assertEqual(adventofcode.puzzle.day15.day15b('day/15/input.txt'), 2851)

    def test_day15_generate_map_for_part_2(self):

        generated_array = adventofcode.puzzle.day15.generate_map_for_part_2(np.array([8], dtype=np.uint8), 5, 5)
        reference_array = np.array(
            [
                [8, 9, 1, 2, 3],
                [9, 1, 2, 3, 4],
                [1, 2, 3, 4, 5],
                [2, 3, 4, 5, 6],
                [3, 4, 5, 6, 7]
            ], dtype=np.uint8
        )
        self.assertTrue(np.array_equal(generated_array, reference_array))


if __name__ == '__main__':
    unittest.main()
