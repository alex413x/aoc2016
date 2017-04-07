from math import fabs


instructions = 'R4, R3, L3, L2, L1, R1, L1, R2, R3, L5, L5, R4, L4, R2, R4, L3, R3, L3, R3, R4, R2, L1, R2, L3, L2, L1, R3, R5, L1, L4, R2, L4, R3, R1, R2, L5, R2, L189, R5, L5, R52, R3, L1, R4, R5, R1, R4, L1, L3, R2, L2, L3, R4, R3, L2, L5, R4, R5, L2, R2, L1, L3, R3, L4, R4, R5, L1, L1, R3, L5, L2, R76, R2, R2, L1, L3, R189, L3, L4, L1, L3, R5, R4, L1, R1, L1, L1, R2, L4, R2, L5, L5, L5, R2, L4, L5, R4, R4, R5, L5, R3, L1, L3, L1, L1, L3, L4, R5, L3, R5, R3, R3, L5, L5, R3, R4, L3, R3, R1, R3, R2, R2, L1, R1, L3, L3, L3, L1, R2, L1, R4, R4, L1, L1, R3, R3, R4, R1, L5, L2, R2, R3, R2, L3, R4, L5, R1, R4, R5, R4, L4, R1, L3, R1, R3, L2, L3, R1, L2, R3, L3, L1, L3, R4, L4, L5, R3, R5, R4, R1, L2, R3, R5, L5, L4, L1, L1'

instructions1 = 'R8, R4, R4, R8'

cardinal = ['N', 'E', 'S', 'W']

class Turtle:
    def __init__(self, direction=None, position=None):
        self.direction = direction or 'N'
        self.position = position or [0, 0]
        self.travel_log = [self.position[:]]
        self.first_traveled_to_twice = None

    def move(self, paces):
        print 'Moving %s paces %s' % (paces, self.direction)
        [self.move_once() for pace in range(paces)]

    def move_once(self):
        if self.direction == 'N':
            self.position[1] += 1
        elif self.direction == 'S':
            self.position[1] -= 1
        elif self.direction == 'E':
            self.position[0] += 1
        elif self.direction == 'W':
            self.position[0] -= 1
        else:
            print 'Invalid direction: %s' % self.direction

        if self.position in self.travel_log and self.first_traveled_to_twice is None:

            #  Note the '[:]' syntax - this allows you to make sure to copy by value and not by reference!
            self.first_traveled_to_twice = self.position[:]

        self.travel_log.append(self.position[:])


    def get_blocks_away(self):
        return fabs(self.position[0]) + fabs(self.position[1])

    def follow_instruction(self, instruction):
        print 'Got instruction %s' % instruction
        turn = instruction[0]
        paces = int(instruction[1:])

        #  Assign new direction
        if turn == 'R':
            index = cardinal.index(self.direction)+1
        elif turn == 'L':
            index = cardinal.index(self.direction)-1
        else:
            print 'Invalid turn: %s' % turn

        #  Here we use modulus to enable us to 'wrap around' the cardinal directions list
        self.direction = cardinal[index % len(cardinal)]

        self.move(paces)

        print 'Travel log: %s' % self.travel_log

    def follow_instructions(self, instructions):
        instr = [self.follow_instruction(i.strip()) for i in instructions.split(',')]

        print 'Distance traveled from start is %s blocks in total' % self.get_blocks_away()

    def get_blocks_away_first_visited_twice(self):
        return fabs(self.first_traveled_to_twice[0]) + fabs(self.first_traveled_to_twice[1])

t = Turtle()
t.follow_instructions(instructions)

print t.get_blocks_away_first_visited_twice()
