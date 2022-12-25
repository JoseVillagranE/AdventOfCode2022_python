def verify_fully_contain(assigment_1: list, assigment_2: list) -> int:

    assigment_1 = list(map(int, assigment_1))
    assigment_2 = list(map(int, assigment_2))

    if (
        assigment_1[0] - assigment_2[0] >= 0
        and assigment_2[1] - assigment_1[1] >= 0
    ):
        return 1
    elif (
        assigment_2[0] - assigment_1[0] >= 0
        and assigment_1[1] - assigment_2[1] >= 0
    ):
        return 1
    else:
        return 0


def count_fully_contains_assigments(doc: str) -> int:

    total_fully_contains_assigments = 0
    with open(doc) as f:
        for line in f:
            as1, as2 = line.rstrip().split(",")
            is_fully_contain = verify_fully_contain(as1.split("-"), as2.split("-"))
            total_fully_contains_assigments += is_fully_contain

    return total_fully_contains_assigments


if __name__ == "__main__":

    doc = "./Day4_input.txt"
    response = count_fully_contains_assigments(doc)
    print(f"total_fully_contains: {response}")
