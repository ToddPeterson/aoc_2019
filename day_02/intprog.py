
class TerminateProgram(Exception):
    pass


class Program:
    def __init__(self, intcode):
        self.intcode = intcode.copy()
    
    def run(self):
        """Run the program"""
        cursor = 0
        prog_length = len(self.intcode)
        while cursor < prog_length:
            opcode = self.intcode[cursor]

            try:
                handler = self.parse_opcode(opcode)
            except TerminateProgram:
                break

            # Might raise IndexError
            args = self.intcode[cursor+1: cursor+4]

            #call the op handler
            handler(*args)

            cursor += 4
    
    def parse_opcode(self, opcode):
        """Parse the opcode and return the handler function"""
        if 1 == opcode:
            return self.add
        elif 2 == opcode:
            return self.multiply
        elif 99 == opcode:
            raise TerminateProgram
        else:
            raise Exception(f'Unknown opcode: {opcode}')

    def add(self, first, second, dest):
        """Handler for the add opcode (1)
        
        Add the values located in the first two positions, store the result
        in the location specified by dest.
        """
        val = self.intcode[first] + self.intcode[second]
        self.intcode[dest] = val
    
    def multiply(self, first, second, dest):
        """Handler for the multiply opcode (2)

        Multiply the values located in the first two positions, store the result
        in the location specified by dest.
        """
        val = self.intcode[first] * self.intcode[second]
        self.intcode[dest] = val
    