def get_score(game):

    score = 0

    if game[0] == "A":  # Rock
        if game[1] == "X":  # Rock
            score = 1 + 3
        elif game[1] == "Y":  # Paper
            score = 2 + 6
        elif game[1] == "Z":
            score = 3 + 0
    elif game[0] == "B":  # Paper
        if game[1] == "X":
            score = 1 + 0
        elif game[1] == "Y":
            score = 2 + 3
        elif game[1] == "Z":
            score = 3 + 6
    elif game[0] == "C":  # Scissors
        if game[1] == "X":
            score = 1 + 6
        elif game[1] == "Y":
            score = 2 + 0
        elif game[1] == "Z":
            score = 3 + 3

    return score


def get_total_score(doc):

    total_score = 0
    with open(doc) as f:
        for line in f:
            game = line.rstrip().split(" ")
            score = get_score(game)
            total_score += score
    return total_score


if __name__ == "__main__":

    doc = "./Day2_input.txt"
    total_score = get_total_score(doc)
    print(f"total_score: {total_score}")
