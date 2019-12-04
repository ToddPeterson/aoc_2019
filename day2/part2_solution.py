from intprog import Program

input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0]

noun = 0
verb = 0

target = 19690720
found = False

# I *think* the output must increase as the noun/verb increases, so let's use that to make this a little less brute force
while noun <= 99:
    while verb <= 99:
        assert(input[0] == 1) # sanity check
        input[1] = noun
        input[2] = verb
        prog = Program(input)
        prog.run()
        output = prog.intcode[0]
        if output == target:
            found = True
            print(f'noun: {noun} verb: {verb}')
            break
        elif output < target:
            verb += 1
        else:
            break
    if found:
        break
    else:
        noun += 1
        verb = 0
        

print(prog.intcode)