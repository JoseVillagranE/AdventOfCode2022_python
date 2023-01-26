from itertools import compress
from math import prod

class monkey:

    def __init__(self, items: list, operation: str, test: str, throw_to_monkey_if_true: str, throw_to_monkey_if_false: str):
        self.items = items
        self.operation = operation
        self.test = test
        self.throw_to_monkey_if_true = throw_to_monkey_if_true
        self.throw_to_monkey_if_false = throw_to_monkey_if_false
        self.number_inspects = 0

    def __apply_test(self, item):
        if self.test[0] == "divisible":
            return item % int(self.test[1]) == 0
    
    def calculate_new_worry_levels(self):
        self.items = [eval(self.operation)//3 for old in self.items]
        self.number_inspects += len(self.items)

    def decide_to_who_throw_item(self):
        testing_results = [self.__apply_test(item) for item in self.items]
        return [(self.throw_to_monkey_if_true, list(compress(self.items, testing_results))),
                (self.throw_to_monkey_if_false, list(compress(self.items, [not e for e in testing_results]))) 
                ]

    def restart_items(self):
        self.items = []

    def debug(self):
        print(self.items)
        print(self.operation)
        print(self.test)
        print(self.throw_to_monkey_if_true)
        print(self.throw_to_monkey_if_false)
        self.calculate_new_worry_levels()
        print(self.items)
    
    def set_items(self, items: list):
        self.items = items
    def set_operation(self, operation: str):
        self.operation = operation
    def set_test(self, test: str):
        self.test = test
    def set_throw_to_monkey_if_true(self, monkey_index: int):
        self.throw_to_monkey_if_true = monkey_index
    def set_throw_to_monkey_if_false(self, monkey_index: int):
        self.throw_to_monkey_if_false = monkey_index

class monkey_business:

    def __init__(self, filename_initial_state: str):

        self.monkeys = []
        self.__read_initial_state(filename_initial_state)

    def __read_initial_state(self, filename: str):
        with open(filename) as f:
            for line in f:
                line = line.strip()
                match line.split(":"):
                    case ["Monkey", index]:
                        actual_monkey = index
                        self.monkeys.append(monkey())
                    case ["Starting items", items]:
                        items = items.replace(" ", "").split(",")
                        items = [int(item) for item in items]
                    case ["Operation", operation]:
                        operation = operation.replace(" ", "").split("=")[1]
                    case ["Test", test]:
                        test = test.replace(" ", "").split("by")
                    case ["If true", cond]:
                        throw_to_monkey_if_true = int(cond.split(" ")[-1]) 
                    case ["If false", cond]:
                        throw_to_monkey_if_false = int(cond.split(" ")[-1])
                        current_monkey = monkey(items, operation, test, throw_to_monkey_if_true, throw_to_monkey_if_false)
                        self.monkeys.append(current_monkey)
    def play(self, n: int):
        for i in range(n):
            for j in range(len(self.monkeys)):
                self.monkeys[j].calculate_new_worry_levels()
                [(monkey_index_1, items1), (monkey_index_2, items2)] = self.monkeys[j].decide_to_who_throw_item()
                self.monkeys[monkey_index_1].items.extend(items1)
                self.monkeys[monkey_index_2].items.extend(items2)
                self.monkeys[j].restart_items()

    def calculate_level_monkey_business(self):
        number_of_inspect_each_monkey = [m.number_inspects for m in self.monkeys]
        return prod(sorted(number_of_inspect_each_monkey, reverse=True)[:2])

if __name__ == "__main__":
    doc = "./Day11_input.txt"
    epochs = 20
    game = monkey_business(doc)
    # for m in game.monkeys:
    #     m.debug()
    game.play(epochs)
    level_of_monkey_business = game.calculate_level_monkey_business()
    print(f"level of monkey business after {level_of_monkey_business} epochs")





