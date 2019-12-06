import unittest

import part1

class TestMove(unittest.TestCase):
    def test_up(self):
        position = [0,0]
        cmd = 'U5'
        wire_set = set()

        position = part1.move(position, cmd, wire_set)
        self.assertEqual(position, (0, 5))
        self.assertEqual(wire_set,
            {(0,0), (0,1), (0,2), (0,3), (0,4), (0,5)})
        
        position = part1.move(position, 'U11', wire_set)
        self.assertEqual(position, (0, 16))
        self.assertIn((0, 16), wire_set)

    def test_down(self):
        position = [0,0]
        cmd = 'D5'
        wire_set = set()

        position = part1.move(position, cmd, wire_set)
        self.assertEqual(position, (0, -5))
        self.assertEqual(wire_set,
            {(0,0), (0,-1), (0,-2), (0,-3), (0,-4), (0,-5)})
        
        position = part1.move(position, 'D11', wire_set)
        self.assertEqual(position, (0, -16))
        self.assertIn((0, -16), wire_set)

    def test_right(self):
        position = [0,0]
        cmd = 'R5'
        wire_set = set()

        position = part1.move(position, cmd, wire_set)
        self.assertEqual(position, (5, 0))
        self.assertEqual(wire_set,
            {(0,0), (1,0), (2,0), (3,0), (4,0), (5,0)})
        
        position = part1.move(position, 'R11', wire_set)
        self.assertEqual(position, (16, 0))
        self.assertIn((16, 0), wire_set)

    def test_left(self):
        position = [0,0]
        cmd = 'L5'
        wire_set = set()

        position = part1.move(position, cmd, wire_set)
        self.assertEqual(position, (-5, 0))
        self.assertEqual(wire_set,
            {(0,0), (-1,0), (-2,0), (-3,0), (-4,0), (-5,0)})
        
        position = part1.move(position, 'L11', wire_set)
        self.assertEqual(position, (-16, 0))
        self.assertIn((-16, 0), wire_set)


class TestTrace(unittest.TestCase):
    def test_1(self):
        cmd = 'R5,U7'
        wire_set = set()
        part1.trace_wire(cmd, wire_set)

        self.assertIn((5,6), wire_set)


class TestExample(unittest.TestCase):
    def test_1(self):
        cmd1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
        cmd2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
        intersection = part1.closest_intersection(cmd1, cmd2)
        self.assertEqual(part1.manhattan_dist(intersection), 159)

    def test_2(self):
        cmd1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
        cmd2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
        intersection = part1.closest_intersection(cmd1, cmd2)
        self.assertEqual(part1.manhattan_dist(intersection), 135)

if __name__ == '__main__':
    unittest.main()