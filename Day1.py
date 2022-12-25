def read_doc(file: str) -> dict:
    """
    Read the input and parse the information into chunks that represents how many calories is carrying
    each elf
    """
    doc = {}
    counter = 0
    acc_calories = 0
    with open(file, "r") as f:
        for line in f:
            if line == "\n":
                doc[f"elf_{counter}"] = acc_calories
                counter += 1
                acc_calories = 0
            else:
                acc_calories += int(line)

    return doc


if __name__ == "__main__":

    input = "./Day1_input.txt"
    doc = read_doc(input)
    elf_w_max_calories = max(doc, key=doc.get)
    max_calories = doc[elf_w_max_calories]

    print(f"Elf {elf_w_max_calories} is carrying {max_calories} calories")
