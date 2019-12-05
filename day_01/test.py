import unittest

import part1
import part2


class TestPart1(unittest.TestCase):
    def test(self):
        self.assertEqual(part1.calc_fuel(12), 2)
        self.assertEqual(part1.calc_fuel(14), 2)
        self.assertEqual(part1.calc_fuel(1969), 654)
        self.assertEqual(part1.calc_fuel(100756), 33583)


class TestPart2(unittest.TestCase):
    def test(self):
        self.assertEqual(part2.calc_fuel(12), 2)
        self.assertEqual(part2.calc_fuel(14), 2)
        self.assertEqual(part2.calc_fuel(1969), 966)
        self.assertEqual(part2.calc_fuel(100756), 50346)


if __name__ == '__main__':
    unittest.main()
