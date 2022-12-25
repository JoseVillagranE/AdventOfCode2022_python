def represent_initial_configuration(lines: list) -> list:

    stacks_index = [4 * i + 1 for i in range(9)]

    initial_config = [[] for _ in range(9)]

    for line in lines:
        for i, stack_index in enumerate(stacks_index):
            crate = line[stack_index]
            if crate != " ":
                initial_config[i].append(crate)

    initial_config = [
        list(reversed(initial_config[i])) for i in range(len(initial_config))
    ]
    return initial_config


def execute_action(crates_config, instruction):

    n_crates_to_move = int(instruction[1])
    stack_from = int(instruction[3]) - 1
    stack_to = int(instruction[5]) - 1
    crates = crates_config[stack_from][-n_crates_to_move:]
    del crates_config[stack_from][-n_crates_to_move:]
    crates_config[stack_to].extend(list(reversed(crates)))


def get_top_crates(crates_config: list) -> str:
    return "".join([stack[-1] for stack in crates_config])


def rearrange_crates(doc) -> str:

    crates_config_raw_data = []
    config_switch = 0
    with open(doc) as f:
        for i, line in enumerate(f):
            if line.rstrip() == "":
                crates_config = represent_initial_configuration(
                    crates_config_raw_data[:-1]
                )
                config_switch = 1
            else:
                if not config_switch:
                    crates_config_raw_data.append(line)
                else:
                    execute_action(crates_config, line.split(" "))

    return get_top_crates(crates_config)


if __name__ == "__main__":

    doc = "./Day5_input.txt"
    top_crates = rearrange_crates(doc)
    print(f"top_crates: {top_crates}")
