import unittest

from intprog import Program

class TestIntprog(unittest.TestCase):
    def test_add(self):
        programs = [
            ([1,0,0,3,99], [3,2]),
            ([1,0,5,5,99,-2], [5,-1]),
            ([1,4,3,0,99], [0, 99])
        ]

        for code, solution in programs:
            prog = Program(code)
            prog.run()
            self.assertEqual(prog.intcode[solution[0]], solution[1])
    
    def test_multiply(self):
        programs = [
            ([2,0,0,3,99], [3,4]),
            ([2,0,5,5,99,-2], [5,-4]),
            ([2,4,3,0,99], [0, 0])
        ]

        for code, solution in programs:
            prog = Program(code)
            prog.run()
            self.assertEqual(prog.intcode[solution[0]], solution[1])
    
    def test_example(self):
        code = [1,9,10,3,2,3,11,0,99,30,40,50]
        final = [3500,9,10,70,2,3,11,0,99,30,40,50]
        prog = Program(code)
        prog.run()

        self.assertEqual(prog.intcode, final)


if __name__ == '__main__':
    unittest.main()