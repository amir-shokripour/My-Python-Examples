from random import sample


def make_matrix():
    matrix = []
    for _ in range(5):
        row = []
        for _ in range(5):
            row.append(0)
        matrix.append(row)
    return matrix


def the_indices():
    indices = sample(range(25), 10)
    return indices


def insert_the_indices(matrix, indices):
    for index in indices:
        row = index // 5
        col = index % 5
        matrix[row][col] = 1
    return matrix


def print_matrix(matrix):
    for i in range(5):
        for j in range(5):
            print(f"{matrix[i][j]:3}", end='')
        print()


def run():
    matrix = make_matrix()
    indices = the_indices()
    print(indices)
    matrix = insert_the_indices(matrix, indices)
    print_matrix(matrix)


run()

# ٍExample

# [8, 17, 13, 9, 16, 10, 22, 24, 1, 7] --> indices

#   0  1  0  0  0
#   0  0  1  1  1
#   1  0  0  1  0
#   0  1  1  0  0
#   0  0  1  0  1
