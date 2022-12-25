import numpy as np


def read_map(doc):
    tree_map = []
    with open(doc) as f:
        for line in f:
            line = list(line.rstrip())
            tree_map.append([int(t) for t in line])
    return np.array(tree_map)


def get_visibles_trees(tree_map):
    n_visibles_trees = 0
    nrows, ncols = tree_map.shape
    # col_maxs = np.amax(tree_map, axis=0)
    # row_maxs = np.amax(tree_map, axis=1)
    # col_maxs_index = np.argmax(tree_map, axis=0)
    # row_maxs_index = np.argmax(tree_map, axis=1)

    for i in range(tree_map.shape[0]):
        for j in range(tree_map.shape[1]):
            current_tree = tree_map[i, j]
            if i == 0 or i == nrows - 1 or j == 0 or j == ncols - 1:
                n_visibles_trees += 1
            else:
                left_trees = tree_map[i, :j]
                right_trees = tree_map[i, j + 1 :]
                upper_trees = tree_map[:i, j]
                bottom_trees = tree_map[i + 1 :, j]
                if (
                    (current_tree > left_trees).all()
                    or (current_tree > right_trees).all()
                    or (current_tree > upper_trees).all()
                    or (current_tree > bottom_trees).all()
                ):
                    n_visibles_trees += 1

    return n_visibles_trees


if __name__ == "__main__":

    doc = "./Day8_input.txt"
    tree_map = read_map(doc)
    n_visibles_trees = get_visibles_trees(tree_map)
    print(f"response: {n_visibles_trees}")
