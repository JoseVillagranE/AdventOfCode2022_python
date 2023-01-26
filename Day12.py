import numpy as np
import random
#Hill Climbing Algoritm
class HillClimbing:

    def __init__(self, filename):
        self.map = self.__read_map(filename)
        self.current_state_pos = self.__get_initial_state_pos()
        self.current_state = "a"
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __read_map(self, filename: str) -> np.ndarray:
        map_lines = []
        with open(filename) as f:
            map_lines = [list(l) for l in f.read().split("\n")]
        return np.array(map_lines, dtype=str)

    def __get_initial_state_pos(self) -> tuple:
        initial_state_indexs = np.where(self.map=="S")
        return (initial_state_indexs[0][0], initial_state_indexs[1][0])

    def __get_state(self, pos: tuple=None):
        if pos:
            return self.map[pos]
        return self.map[self.current_state_pos]

    def __verify_terminal_state(self, next_state) -> tuple:
        done = False
        message = ""
        if not next_state:
            done = True
            message = "Sink State!"
        elif self.map[self.current_state_pos] == "E":
            done = True
            message = "Goal!"
        return done, message

    def __get_delta_between_states(self, next_state: str) -> int:
        return self.alphabet.find(next_state) - self.alphabet.find(self.current_state)
    
    def __choose_next_state(self, next_states: list):
        next_states_delta = list(map(lambda x: (self.__get_delta_between_states(x[0]), x[1]), next_states))
        # print(next_states_delta)
        next_states_delta = list(filter(lambda x: x[0]<2, next_states_delta))
        # print(f"next_states_delta: {next_states_delta}")
        next_state = None
        if next_states_delta:
            next_state = max(next_states_delta, key= lambda x: x[0])[1]
            # print(next_state_value)
            # next_state = random.choice([next_states[i] for i, s in enumerate(next_states_delta) if s[0] == next_state_value])
            # print(next_state)
            # next_state = (self.map[next_state_pos], next_state_pos)
        return next_state

    def __step(self):
        next_states = []
        up_pos = (self.current_state_pos[0]-1, self.current_state_pos[1])
        down_pos = (self.current_state_pos[0]+1, self.current_state_pos[1])
        left_pos = (self.current_state_pos[0], self.current_state_pos[1]-1)
        right_pos = (self.current_state_pos[0], self.current_state_pos[1]+1)
        
        if up_pos[0] > 0:
            next_states.append((self.map[up_pos], up_pos))
        if down_pos[0] < self.map.shape[0]:
            next_states.append((self.map[down_pos], down_pos))
        if left_pos[1] > 0:
            next_states.append((self.map[left_pos], left_pos))
        if right_pos[1] < self.map.shape[1]:
            next_states.append((self.map[right_pos], right_pos))

        next_state = self.__choose_next_state(next_states)
        if next_state:
            self.current_state = self.map[next_state]
            self.current_state_pos = next_state
        print(self.current_state, self.current_state_pos)
        done, message = self.__verify_terminal_state(next_state)
        return done, message

    def play(self, steps_tol: int):
        done = False
        step = 0
        while not done:
            (done, message) = self.__step()
            if done:
                print(f"Terminal Reason: {message}")
                break
            elif step > steps_tol:
                print("Exceeded the tolerance of steps")
                break
            step += 1
    
if __name__ == "__main__":

    doc = "./Day12_input.txt"
    steps_tol = 50000000
    agent = HillClimbing(doc)
    agent.play(steps_tol)
