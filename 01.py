import turtle


class BlockPointer():
    def __init__(self):
        self.facing = 0 # 0 up, 1 east, 2 sout, 3 west
        self.pos = [0, 0]
        self.history = [[self.pos[0], self.pos[1]]]

    def parse(self, value):
        if value[0].lower() == "r":
            self.facing += 1
        elif value[0].lower() == "l":
            self.facing -= 1
        else:
            raise Exception("Rotation Argument Error:", value[0])
        self.facing %= 4
        n = int(value[1:]) # move n steps in new direction
        if self.facing is 0:
            self.pos[1] += n
        elif self.facing is 1:
            self.pos[0] += n
        elif self.facing is 2:
            self.pos[1] -= n
        elif self.facing is 3:
            self.pos[0] -= n
        else:
            raise Exception("Rotation State Error:", self.facing)
        if self.pos in self.history:
            print("Duplicate:", self.pos)
        else:
            self.history.append([self.pos[0], self.pos[1]])
        
        def length(self):
            y, x = [abs(self.pos[0]), abs(self.pos[1]]
            return x + y

if __name__ == "__main__":
    real_string = "R4, R5, L5, L5, L3, R2, R1, R1, L5, R5, R2, L1, L3, L4, R3, L1, L1, R2, R3, R3, R1, L3, L5, R3, R1, L1, R1, R2, L1, L4, L5, R4, R2, L192, R5, L2, R53, R1, L5, R73, R5, L5, R186, L3, L2, R1, R3, L3, L3, R1, L4, L2, R3, L5, R4, R3, R1, L1, R5, R2, R1, R1, R1, R3, R2, L1, R5, R1, L5, R2, L2, L4, R3, L1, R4, L5, R4, R3, L5, L3, R4, R2, L5, L5, R2, R3, R5, R4, R2, R1, L1, L5, L2, L3, L4, L5, L4, L5, L1, R3, R4, R5, R3, L5, L4, L3, L1, L4, R2, R5, R5, R4, L2, L4, R3, R1, L2, R5, L5, R1, R1, L1, L5, L5, L2, L1, R5, R2, L4, L1, R4, R3, L3, R1, R5, L1, L4, R2, L3, R5, R3, R1, L3"
    segment = real_string.split(", ")
    pointer = BlockPointer()
    for val in segment:
        pointer.parse(val)
    print("Length:", pointer.length)
    
    # for part two:
    turtle = turtle.Turtle()
    turtle.down()
    turtle.setpos(0, 0)
    turtle.clear()
    for pos in pointer.history:
        turtle.goto(pos[0] * 2, pos[1] * 2)
    # and now you measure it, because I was too lazy to look up any intersection variant.
    # It most likely would've been for any pair of tuples with [0, N] -> (0, 1), (1, 2) ... (N-1, N)
    # and then search for an intersection by any tuple being [[x0, y0], [x1, y1]] | [[x2, y2], [x3, y3]]
    # and then doing the standard raycasting variant (?)
