alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_common_item(rucksack):
    number_items = len(rucksack) // 2

    compartment_1 = rucksack[:number_items]
    compartment_2 = rucksack[number_items:]

    common_item = "".join(set(compartment_1).intersection(compartment_2))
    return common_item


def get_priority(item):
    return alphabet.find(item) + 1


def get_sum_priorities(doc):

    total_priorities = 0
    with open(doc) as f:
        for line in f:
            common_item = get_common_item(line.rstrip())
            priority = get_priority(common_item)
            total_priorities += priority

    return total_priorities


if __name__ == "__main__":

    doc = "./Day3_input.txt"
    total_priorities = get_sum_priorities(doc)
    print(f"Sum of priorities: {total_priorities}")
