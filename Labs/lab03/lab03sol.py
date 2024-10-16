def is_solvable(puzzle):  
    inv_count = 0
    flattened = [num for row in puzzle for num in row if num != 0]
    for i in range(len(flattened)):
        for j in range(i + 1, len(flattened)):
            if flattened[i] > flattened[j]:
                inv_count += 1
    return inv_count % 2 == 0
# flattened = [num for row in puzzle for num in row if num != 0]
# it means
# flattened = []
# for row in puzzle:
#     for num in row:
#         if num != 0:
#             flattened.append(num)


def find_blank(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                return i, j


def get_moves(puzzle):
    blank_pos = find_blank(puzzle)
    i, j = blank_pos
    moves = []
    if i > 0:  # Move blank up(upward movement)
        moves.append((i-1, j))
    if i < 2:  # Move blank down(downward movement)
        moves.append((i+1, j))
    if j > 0:  # Move blank left(left move)
        moves.append((i, j-1))
    if j < 2:  # Move blank right(right move)
        moves.append((i, j+1))
    return moves


def apply_move(puzzle, move):
    i, j = find_blank(puzzle)
    new_puzzle = [row[:] for row in puzzle]
    new_i, new_j = move
    new_puzzle[i][j], new_puzzle[new_i][new_j] = new_puzzle[new_i][new_j], new_puzzle[i][j]
    return new_puzzle



def is_goal(puzzle):
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return puzzle == goal


def dls(puzzle, depth):
    if is_goal(puzzle):  # yha p goal wala argument...
        return True, [puzzle]
    if depth == 0:
        return False, []
    for move in get_moves(puzzle):
        new_puzzle = apply_move(puzzle, move)
        solved, path = dls(new_puzzle, depth - 1)
        if solved:
            return True, [puzzle] + path
    return False, []


def iddfs(puzzle, max_depth):
    if not is_solvable(puzzle):
        return "The puzzle is unsolvable."
    for depth in range(max_depth):
        solved, path = dls(puzzle, depth)
        if solved:
            return path
    return "Solution not found within the depth limit."


def print_puzzle(puzzle):
    for row in puzzle:
        print(row)
    print()


def main():
    initial_puzzle = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    solution = iddfs(initial_puzzle, 5)
# Goal will be find at max depth 3 in this case
    if isinstance(solution, str):
        # if the solution is of type str then isinstance()
        # evaluates to True then code inside the if block executes
        print(solution)
    else:
        print("Solution steps:")
        for step in solution:
            print_puzzle(step)


if __name__ == '__main__':
    main()
