import numpy as np


class Rope:
    def __init__(self):
        self.n = 1000
        self.map = np.chararray((self.n, self.n), unicode=True)
        self.map[:] = "."
        self.H_pos = np.array([self.n // 2 - 1, self.n // 2 - 1])
        self.T_pos = np.array([self.n // 2 - 1, self.n // 2 - 1])

    def __move_tail(self, pre=False):
        mark = "#"
        if pre:
            mark = "#"
        self.map[self.T_pos[0], self.T_pos[1]] = mark

    def __move_head(self, pre=False):
        mark = "H"
        if pre:
            mark = "."
        self.map[self.H_pos[0], self.H_pos[1]] = mark

    def tail_movement(self):
        delta = self.H_pos - self.T_pos
        if np.isin(delta, [2, -2]).any():
            self.__move_tail(pre=True)
            if delta[0] in [2, -2]:
                self.T_pos[0] += delta[0] // 2
                if delta[1] in [1, -1]:
                    self.T_pos[1] += delta[1]
            else:
                self.T_pos[1] += delta[1] // 2
                if delta[0] in [1, -1]:
                    self.T_pos[0] += delta[0]
            self.__move_tail()

    def move_1_step(self, direction):

        # self.__move_head(pre=True)

        if direction == "U":
            self.H_pos[0] -= 1

        elif direction == "D":
            self.H_pos[0] += 1

        elif direction == "L":
            self.H_pos[1] -= 1

        elif direction == "R":
            self.H_pos[1] += 1

        else:
            print(f"direction {direction} dont allowed")

        # self.__move_head()
        self.tail_movement()

    def move(self, direction, steps):
        for _ in range(steps):
            self.move_1_step(direction)


def read_sequential_movements(doc, rope):
    with open(doc) as f:
        for line in f:
            line = line.rstrip()
            direction, steps = line.split(" ")
            rope.move(direction, int(steps))


if __name__ == "__main__":

    doc = "./Day9_input.txt"
    rope = Rope()
    read_sequential_movements(doc, rope)
    print(f"Number of #: {(rope.map == '#').sum()}")
