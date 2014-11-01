#!/usr/bin/python

import json

__author__ = 'dustise'


def get_row(matrix, row):
    line = matrix[row]
    result = []
    for digit in line:
        if digit != 0:
            result.append(digit)
    return set(result)


def get_col(matrix, col):
    result = []
    for row in matrix:
        if row[col] != 0:
            result.append(row[col])
    return set(result)


def get_block(matrix, row, col):
    result = []
    min_row = row // 3 * 3
    max_row = (row // 3 + 1) * 3
    min_col = col // 3 * 3
    max_col = (col // 3 + 1) * 3

    for x in range(min_row, max_row):
        for y in range(min_col, max_col):
            if matrix[x][y] != 0:
                result.append(matrix[x][y])
    return set(result)


def print_matrix(matrix):
    for line in matrix:
        print line


def get_possible_answer(matrix):
    full_line = set(range(1, 10))
    # test every cell
    min_possible = [0, 0, 9, range(1, 10)]
    settled = True
    count = 0
    for x in range(0, 9):
        for y in range(0, 9):
            if matrix[x][y] != 0:
                count += 1
                continue
            settled = False
            row_data = get_row(matrix, x)
            col_data = get_col(matrix, y)
            block = get_block(matrix, x, y)
            possible_values = full_line - row_data - col_data - block
            possible_count = len(possible_values)
            if possible_count < min_possible[2]:
                min_possible = [x, y, possible_count, possible_values]

    # print "None-Zero count is %d" % count
    return settled, min_possible[0], min_possible[1], min_possible[2], min_possible[3]


def test_matrix(matrix):
    stack = [json.dumps(matrix)]
    steps = 0
    max_depth = 0
    current_matrix = []
    while len(stack) > 0:
        # print "current stack depth is %d \n" % len(stack)
        steps += 1
        if len(stack) > max_depth:
            max_depth = len(stack)
        current_matrix = json.loads(stack.pop())
        (settled, x, y, count, values) = get_possible_answer(current_matrix)
        if settled:
            print_matrix(current_matrix)
            print 'total steps %d, max stack depth: %d' % (steps, max_depth)
            return
        for value in values:
            current_matrix[x][y] = value
            # print json.dumps(current_matrix)
            stack.append(json.dumps(current_matrix))
        if steps % 100 == 0:
            print "steps: %d  stack: %d" % (steps, len(stack))

    print_matrix(current_matrix)

# quiz = [
# [6, 0, 0, 0, 0, 0, 0, 9, 7],
#     [3, 9, 0, 0, 0, 8, 0, 2, 0],
#     [0, 0, 0, 0, 2, 0, 0, 0, 0],
#     [0, 8, 0, 5, 0, 9, 0, 0, 0],
#     [0, 0, 9, 0, 0, 0, 8, 0, 0],
#     [0, 0, 0, 6, 0, 0, 0, 4, 0],
#     [0, 0, 0, 0, 4, 0, 0, 0, 0],
#     [0, 1, 0, 7, 0, 0, 0, 6, 5],
#     [4, 5, 0, 0, 0, 0, 0, 0, 3],
# ]

# so hard??
quiz = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
]

# quiz = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

test_matrix(quiz)