import numpy as np

CYCLES = 1
SINGLE_REGISTER = 1


def calculate_signal_strength(cycles_to_register, signals):
    cycles_to_register = np.array(cycles_to_register)
    signals = np.array(signals)
    return cycles_to_register * signals


def read_instructions(doc, cycles_to_register):
    global CYCLES, SINGLE_REGISTER
    interest_signals = []
    with open(doc) as f:
        for line in f:
            inst = line.rstrip()
            if len(inst.split(" ")) == 1:  # noop
                CYCLES += 1
                if CYCLES in cycles_to_register:
                    interest_signals.append(SINGLE_REGISTER)
            else:
                for cycle in range(2):
                    CYCLES += 1
                    if cycle == 1:
                        SINGLE_REGISTER += int(inst.split(" ")[-1])
                    if CYCLES in cycles_to_register:
                        interest_signals.append(SINGLE_REGISTER)
    return interest_signals


if __name__ == "__main__":

    doc = "./Day10_input.txt"
    cycles_to_calculate_signal_strength = [20, 60, 100, 140, 180, 220]
    signals_register_to_that_cycles = read_instructions(
        doc, cycles_to_calculate_signal_strength
    )
    signal_strength = calculate_signal_strength(
        cycles_to_calculate_signal_strength, signals_register_to_that_cycles
    )
    print(f"sum_signals_strengths: {signal_strength.sum()}")
