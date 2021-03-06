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
import adventofcode.puzzle.day16 as day16

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

    def test_day16_read_file(self):
        queue_0_content = [1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]
        queue_1_content = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        queue = day16.read_file('day/16/example.txt')

        self.assertGreaterEqual(len(queue), 3)
        self.assertCountEqual(queue[0], queue_0_content)
        self.assertListEqual(queue[0], queue_0_content)
        self.assertCountEqual(queue[1], queue_1_content)
        self.assertListEqual(queue[1], queue_1_content)

    def test_day16_ValuePaket(self):
        queue = day16.read_file('day/16/example.txt')
        objects = day16.parse_queue(queue[0])
        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0].version, 6)
        self.assertEqual(objects[0].value, 2021)

    def test_day16_OperatorPaket(self):
        queue = day16.read_file('day/16/example.txt')
        objects = day16.parse_queue(queue[1])

        self.assertEqual(len(objects), 1)
        self.assertEqual(objects[0].version, 1)
        self.assertEqual(objects[0].type_id, 6)
        self.assertEqual(len(objects[0].packets), 2)
        self.assertEqual(objects[0].packets[0].value, 10)
        self.assertEqual(objects[0].packets[1].value, 20)

        objects = day16.parse_queue(queue[2])
        self.assertEqual(objects[0].version, 7)
        self.assertEqual(objects[0].type_id, 3)
        self.assertEqual(len(objects), 1)
        self.assertEqual(len(objects[0].packets), 3)
        self.assertEqual(objects[0].packets[0].value, 1)
        self.assertEqual(objects[0].packets[1].value, 2)
        self.assertEqual(objects[0].packets[2].value, 3)

    def test_day16_VersionSum(self):
        queue = day16.read_file('day/16/example.txt')
        lines_and_version_sums = {3: 16, 4: 12, 5: 23, 6: 31}

        for k, v in lines_and_version_sums.items():
            objects = day16.parse_queue(queue[k])
            version_sum = day16.calc_version_sum(objects)
            self.assertEqual(v, version_sum)

    def test_day16_a(self):
        self.assertEqual(day16.day16a('day/16/input.txt'), 934)

    def test_day16_arithmetics(self):
        excepted_results = {7: 3, 8: 54, 9: 7, 10: 9, 11: 1, 12: 0, 13: 0, 14: 1}
        queue = day16.read_file('day/16/example.txt')
        for k, v in excepted_results.items():
            objects = day16.parse_queue(queue[k])
            result = objects[0].result()
            self.assertEqual(v, result)

    def test_day16_a(self):
        self.assertEqual(day16.day16b('day/16/input.txt'), 912901337844)

if __name__ == '__main__':
    unittest.main()
