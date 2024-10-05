import random
import time

time1 = time.time()

BLUE = "b"
RED = "r"
WHITE = "w"
YELLOW = "y"
GREEN = "g"
ORANGE = "o"

NUMBER_OF_MOVES = 0


class CustomException(Exception):
    pass


def rotate_clockwise(lst):
    # Rotates a face clockwise
    list_ = []
    n = len(lst)
    for i in range(n):
        temp = []
        for j in range(n):
            temp = list(lst[j][i]) + temp
        list_.append(temp)
    return list_


def rotate_anti_clockwise(lst):
    # Rotates a face anti-clockwise
    n = len(lst)
    list_ = []
    for i in range(n - 1, -1, -1):
        temp = []
        for j in range(n):
            temp = temp + list(lst[j][i])
        list_.append(temp)
    return list_


def splitter(string):
    state = [[], [], [], [], [], []]
    a = len(string)
    b = (a / 6) ** (1 / 2)
    try:
        if b % 1 != 0:
            raise CustomException
        else:
            b = int(b)
    except CustomException:
        print("You have entered an invalid input please check")
        return 0
    for i in range(6):
        state[i] = [list(string[i * b * b + j * b: i * b * b + j * b + b]) for j in range(b)]

    return state, b


def display_cube(state):
    # This function displays the current state of the cube
    color_index = {"r": "🟥", "g": "🟩", "w": "⬜", "b": "🟦", "y": "🟨", "o": "🟧", " ": " "}
    n = len(state[0])
    for i in range(n):
        print(" " * (2 * n + 2), end="")
        for j in state[0][i]:
            print(color_index[j], end="")
        print()
    print()
    for i in range(n):
        for j in state[2][i] + [" "] + state[1][i] + [" "] + state[3][i]:
            print(color_index[j], end="")
        print()
    print()
    for i in range(n):
        print(" " * (2 * n + 2), end="")
        for j in state[4][i]:
            print(color_index[j], end="")
        print()
    print()
    for i in range(n):
        print(" " * (2 * n + 2), end="")
        for j in state[5][i]:
            print(color_index[j], end="")
        print()
    print()


def random_state(n):
    string = ""
    string_ = "rgbwoy"
    for i in range(6 * n * n):
        a = random.randint(0, 5)
        string = string + string_[a]
    return string


def solved_state(n):
    string = ""
    string_ = "brwygo"
    for ch in string_:
        string = string + ch * (n * n)
    print(string)
    return string


def moves_generator(n):
    functions = []

    def r_move(i):
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1
        if i == 0:
            temp = state[3]
            state[3] = rotate_clockwise(temp)
        for j in range(n):
            state[0][j][n - i - 1], state[5][j][n - i - 1] = state[5][j][n - i - 1], state[0][j][n - i - 1]
            state[1][j][n - i - 1], state[4][j][n - i - 1] = state[4][j][n - i - 1], state[1][j][n - i - 1]
            state[4][j][n - i - 1], state[0][j][n - i - 1] = state[0][j][n - i - 1], state[4][j][n - i - 1]

    functions.append(r_move)

    def r_dash_move(i):
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1
        if i == 0:
            temp = state[3]
            state[3] = rotate_anti_clockwise(temp)
        for j in range(n):
            state[0][j][n - i - 1], state[5][j][n - i - 1] = state[5][j][n - i - 1], state[0][j][n - i - 1]
            state[1][j][n - i - 1], state[4][j][n - i - 1] = state[4][j][n - i - 1], state[1][j][n - i - 1]
            state[1][j][n - i - 1], state[5][j][n - i - 1] = state[5][j][n - i - 1], state[1][j][n - i - 1]

    functions.append(r_dash_move)

    def l_move(i):
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1
        if i == 0:
            temp = state[2]
            state[2] = rotate_clockwise(temp)
        for j in range(n):
            state[0][j][i], state[5][j][i] = state[5][j][i], state[0][j][i]
            state[1][j][i], state[4][j][i] = state[4][j][i], state[1][j][i]
            state[1][j][i], state[5][j][i] = state[5][j][i], state[1][j][i]

    functions.append(l_move)

    def l_dash_move(i):
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1
        if i == 0:
            temp = state[2]
            state[2] = rotate_anti_clockwise(temp)
        for j in range(n):
            state[0][j][i], state[5][j][i] = state[5][j][i], state[0][j][i]
            state[1][j][i], state[4][j][i] = state[4][j][i], state[1][j][i]
            state[4][j][i], state[0][j][i] = state[0][j][i], state[4][j][i]

    functions.append(l_dash_move)

    def f_move(i):
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1
        if i == 0:
            temp = state[4]
            state[4] = rotate_clockwise(temp)
        for j in range(n):
            state[2][n - i - 1][j], state[5][i][n - j - 1] = state[5][i][n - j - 1], state[2][n - i - 1][j]
            state[1][n - i - 1][j], state[3][n - i - 1][j] = state[3][n - i - 1][j], state[1][n - i - 1][j]
            state[1][n - i - 1][j], state[5][i][n - j - 1] = state[5][i][n - j - 1], state[1][n - i - 1][j]

    functions.append(f_move)

    def f_dash_move(i):
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1
        if i == 0:
            temp = state[4]
            state[4] = rotate_anti_clockwise(temp)
        for j in range(n):
            state[2][n - i - 1][j], state[5][i][n - j - 1] = state[5][i][n - j - 1], state[2][n - i - 1][j]
            state[1][n - i - 1][j], state[3][n - i - 1][j] = state[3][n - i - 1][j], state[1][n - i - 1][j]
            state[2][n - i - 1][j], state[3][n - i - 1][j] = state[3][n - i - 1][j], state[2][n - i - 1][j]

    functions.append(f_dash_move)

    def b_move(i):
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1
        if i == 0:
            temp = state[0]
            state[0] = rotate_clockwise(temp)
        for j in range(n):
            state[2][i][j], state[5][n - i - 1][n - j - 1] = state[5][n - i - 1][n - j - 1], state[2][i][j]
            state[1][i][j], state[3][i][j] = state[3][i][j], state[1][i][j]
            state[2][i][j], state[3][i][j] = state[3][i][j], state[2][i][j]

    functions.append(b_move)

    def b_dash_move(i):
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1
        if i == 0:
            temp = state[0]
            state[0] = rotate_anti_clockwise(temp)
        for j in range(n):
            state[2][i][j], state[5][n - i - 1][n - j - 1] = state[5][n - i - 1][n - j - 1], state[2][i][j]
            state[1][i][j], state[3][i][j] = state[3][i][j], state[1][i][j]
            state[1][i][j], state[5][n - i - 1][n - j - 1] = state[5][n - i - 1][n - j - 1], state[1][i][j]

    functions.append(b_dash_move)

    def u_move(i):
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1
        if i == 0:
            temp = state[1]
            state[1] = rotate_clockwise(temp)
        for j in range(n):
            state[0][n - i - 1][j], state[3][j][i] = state[3][j][i], state[0][n - i - 1][j]
            state[4][i][j], state[2][j][n - i - 1] = state[2][j][n - i - 1], state[4][i][j]
            state[0][n - i - 1][j], state[4][i][j] = state[4][i][j], state[0][n - i - 1][j]
        state[4][i].reverse()
        state[0][n - i - 1].reverse()

    functions.append(u_move)

    def u_dash_move(i):
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1
        if i == 0:
            temp = state[1]
            state[1] = rotate_anti_clockwise(temp)
        for j in range(n):
            state[0][n - i - 1][j], state[3][j][i] = state[3][j][i], state[0][n - i - 1][j]
            state[4][i][j], state[2][j][n - i - 1] = state[2][j][n - i - 1], state[4][i][j]
            state[2][j][n - i - 1], state[3][j][i] = state[3][j][i], state[2][j][n - i - 1]
        for j in range(int(n / 2)):
            state[2][j][n - i - 1], state[2][n - j - 1][n - i - 1] = state[2][n - j - 1][n - i - 1], state[2][j][
                n - i - 1]
            state[3][j][i], state[3][n - j - 1][i] = state[3][n - j - 1][i], state[3][j][i]

    functions.append(u_dash_move)

    def d_move(i):
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1
        if i == 0:
            temp = state[5]
            state[5] = rotate_clockwise(temp)
        for j in range(n):
            state[0][i][j], state[3][j][n - i - 1] = state[3][j][n - i - 1], state[0][i][j]
            state[4][n - i - 1][j], state[2][j][i] = state[2][j][i], state[4][n - i - 1][j]
            state[2][j][i], state[3][j][n - i - 1] = state[3][j][n - i - 1], state[2][j][i]
        for j in range(int(n / 2)):
            state[2][j][i], state[2][n - j - 1][i] = state[2][n - j - 1][i], state[2][j][i]
            state[3][j][n - i - 1], state[3][n - j - 1][n - i - 1] = state[3][n - j - 1][n - i - 1], state[3][j][
                n - i - 1]

    functions.append(d_move)

    def d_dash_move(i):
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1
        if i == 0:
            temp = state[5]
            state[5] = rotate_anti_clockwise(temp)
        for j in range(n):
            state[0][i][j], state[3][j][n - i - 1] = state[3][j][n - i - 1], state[0][i][j]
            state[4][n - i - 1][j], state[2][j][i] = state[2][j][i], state[4][n - i - 1][j]
            state[0][i][j], state[4][n - i - 1][j] = state[4][n - i - 1][j], state[0][i][j]
        for j in range(int(n / 2)):
            state[0][i][j], state[0][i][n - j - 1] = state[0][i][n - j - 1], state[0][i][j]
        state[4][n - i - 1].reverse()

    functions.append(d_dash_move)
    return functions


def center_piece_arranger(target, position, color, func):  # here color indicates the color of the centrepiece
    i = target[0]  # I indicate row value of the target
    j = target[1]  # j indicates column value of the target
    a = position[1]  # a indicates row value of the position of the required piece
    b = position[2]  # b indicates the column value of the position of the required piece
    c = position[0]  # c indicates the face on which the required piece
    if state[1][i][j] != color:
        if i + j == N - 1 and c == 0:
            count = "x"
            if a == i and b == N - 1 - i:
                func[7](0)
                count = 0
            elif a == N - 1 - i and b == N - 1 - i:
                func[7](0)
                func[7](0)
                count = 1
            elif a == N - 1 - i and b == i:
                func[6](0)
                count = 2
            condition = state[1][i][N - j - 1] == color
            func[0](j)
            func[6](0)
            func[3](j)
            func[7](0)
            func[1](j)
            func[6](0)
            func[2](j)
            func[7](0)
            if state[1][i][N - j - 1] != color and condition:
                func[0](j)
                func[6](0)
                func[3](j)
                func[7](0)
                func[1](j)
                func[6](0)
                func[2](j)
                func[7](0)

            if count == 0:
                func[6](0)
            elif count == 1:
                func[6](0)
                func[6](0)
            elif count == 2:
                func[7](0)

        elif i + j != N - 1 and c == 0:
            count = "x"
            if a == N - 1 - i and b == N - 1 - j:
                func[7](0)
                count = 0
            elif a == N - 1 - j and b == i:
                func[7](0)
                func[7](0)
                count = 1
            elif a == i and b == j:
                func[6](0)
                count = 2
            condition = state[1][j][N - i - 1] == color
            func[0](i)
            func[7](0)
            func[3](j)
            func[6](0)
            func[1](i)
            func[7](0)
            func[2](j)
            func[6](0)
            if state[1][j][N - i - 1] != color and condition:
                func[0](i)
                func[7](0)
                func[3](j)
                func[6](0)
                func[1](i)
                func[7](0)
                func[2](j)
                func[6](0)

            if count == 0:
                func[6](0)
            elif count == 1:
                func[6](0)
                func[6](0)
            elif count == 2:
                func[7](0)

        elif i + j != N - 1 and c == 2:
            count = "x"
            if a == N - 1 - i and b == N - 1 - j:
                func[2](0)
                count = 0
            elif a == j and b == N - 1 - i:
                func[2](0)
                func[2](0)
                count = 1
            elif a == i and b == j:
                func[3](0)
                count = 2

            condition = state[1][N - j - 1][i] == color
            func[5](j)
            func[2](0)
            func[6](i)
            func[3](0)
            func[4](j)
            func[2](0)
            func[7](i)
            func[3](0)
            if state[1][N - j - 1][i] != color and condition:
                func[5](j)
                func[2](0)
                func[6](i)
                func[3](0)
                func[4](j)
                func[2](0)
                func[7](i)
                func[3](0)

            if count == 0:
                func[3](0)
            elif count == 1:
                func[3](0)
                func[3](0)
            elif count == 2:
                func[2](0)

        elif i + j == N - 1 and c == 2:
            count = "x"
            if a == j and b == N - 1 - j:
                func[3](0)
                count = 0
            elif a == N - 1 - j and b == N - 1 - j:
                func[3](0)
                func[3](0)
                count = 1
            elif a == N - 1 - j and b == j:
                func[2](0)
                count = 2

            condition = state[1][j][j] == color
            func[5](i)
            func[3](0)
            func[6](i)
            func[2](0)
            func[4](i)
            func[3](0)
            func[7](i)
            func[2](0)
            if state[1][j][j] != color and condition:
                func[5](i)
                func[3](0)
                func[6](i)
                func[2](0)
                func[4](i)
                func[3](0)
                func[7](i)
                func[2](0)

            if count == 0:
                func[2](0)
            elif count == 1:
                func[2](0)
                func[2](0)
            elif count == 2:
                func[3](0)

        elif i + j != N - 1 and c == 3:
            count = "x"
            if a == N - 1 - i and b == N - 1 - j:
                func[0](0)
                count = 0
            elif a == j and b == N - 1 - i:
                func[0](0)
                func[0](0)
                count = 1
            elif a == i and b == j:
                func[1](0)
                count = 2

            condition = state[1][N - j - 1][i] == color
            func[4](j)
            func[0](0)
            func[7](i)
            func[1](0)
            func[5](j)
            func[0](0)
            func[6](i)
            func[1](0)
            if state[1][N - j - 1][i] != color and condition:
                func[4](j)
                func[0](0)
                func[7](i)
                func[1](0)
                func[5](j)
                func[0](0)
                func[6](i)
                func[1](0)

            if count == 0:
                func[1](0)
            elif count == 1:
                func[1](0)
                func[1](0)
            elif count == 2:
                func[0](0)

        elif i + j == N - 1 and c == 3:
            count = "x"
            if a == N - 1 - i and b == N - 1 - j:
                func[1](0)
                count = 0
            elif a == i and b == N - 1 - j:
                func[1](0)
                func[1](0)
                count = 1
            elif a == i and b == j:
                func[0](0)
                count = 2

            condition = state[1][j][j] == color
            func[4](i)
            func[1](0)
            func[7](i)
            func[0](0)
            func[5](i)
            func[1](0)
            func[6](i)
            func[0](0)
            if state[1][j][j] != color and condition:
                func[4](i)
                func[1](0)
                func[7](i)
                func[0](0)
                func[5](i)
                func[1](0)
                func[6](i)
                func[0](0)

            if count == 0:
                func[0](0)
            elif count == 1:
                func[0](0)
                func[0](0)
            elif count == 2:
                func[1](0)

        elif i + j != N - 1 and c == 4:
            count = "x"
            if a == N - 1 - i and b == N - 1 - j:
                func[5](0)
                count = 0
            elif a == N - 1 - j and b == i:
                func[5](0)
                func[5](0)
                count = 1
            elif a == i and b == j:
                func[4](0)
                count = 2

            condition = state[1][j][N - 1 - i] == color
            func[1](i)
            func[5](0)
            func[2](j)
            func[4](0)
            func[0](i)
            func[5](0)
            func[3](j)
            func[4](0)
            if state[1][j][N - 1 - i] != color and condition:
                func[1](i)
                func[5](0)
                func[2](j)
                func[4](0)
                func[0](i)
                func[5](0)
                func[3](j)
                func[4](0)

            if count == 0:
                func[4](0)
            elif count == 1:
                func[4](0)
                func[4](0)
            elif count == 2:
                func[5](0)

        elif i + j == N - 1 and c == 4:
            count = "x"
            if a == N - 1 - i and b == N - 1 - j:
                func[4](0)
                count = 0
            elif a == j and b == N - 1 - i:
                func[4](0)
                func[4](0)
                count = 1
            elif a == i and b == j:
                func[5](0)
                count = 2

            condition = state[1][i][i] == color
            func[2](i)
            func[4](0)
            func[1](i)
            func[5](0)
            func[3](i)
            func[4](0)
            func[0](i)
            func[5](0)
            if state[1][i][i] != color and condition:
                func[2](i)
                func[4](0)
                func[1](i)
                func[5](0)
                func[3](i)
                func[4](0)
                func[0](i)
                func[5](0)

            if count == 0:
                func[5](0)
            elif count == 1:
                func[5](0)
                func[5](0)
            elif count == 2:
                func[4](0)

        else:
            if a + b != N - 1:
                func[3](b)
                func[10](0)
                func[0](a)
                func[11](0)
                func[2](b)
                func[10](0)
                func[1](a)
                func[11](0)
                center_piece_arranger(target, (0, b, N - 1 - a), color, func)

            else:
                func[0](a)
                func[11](0)
                func[3](a)
                func[10](0)
                func[1](a)
                func[11](0)
                func[2](a)
                func[10](0)
                center_piece_arranger(target, (0, a, a), color, func)


def test_string_generator(n):
    if n % 2 != 0:
        string = (6 * n * n) * ["w"]
        string[n * n + int(n / 2) * n + int(n / 2)] = "r"
        string[0:n * n] = (n * n) * ["r"]
        string[int(n / 2) * n + int(n / 2)] = "w"
    else:
        string = (6 * n * n) * ["w"]
        string[5 * n * n: 6 * n * n] = (n * n) * ["r"]
    return string


def mid_pieces_locator(piece_map):
    mid_pieces = [[[[0, 0, 0] for _ in range(N)] for _ in range(N)] for _ in range(6)]
    mid_pieces_reverse = [[[[0, 0, 0] for _ in range(N)] for _ in range(N)] for _ in range(6)]

    for c in range(6):
        for x in range(1, N - 1):
            for y in range(1, N - 1):
                # Skip unnecessary checks
                if N % 2 != 0 and x / 2 == y / 2 and 2 * x == N - 1:
                    continue

                destination_face = piece_map[state[c][x][y]]
                if c != destination_face:
                    if mid_pieces[destination_face][x][y] == [0, 0, 0] and state[destination_face][x][y] != state[c][x][
                        y]:
                        mid_pieces[destination_face][x][y] = [c, x, y]
                        if mid_pieces_reverse[c][x][y] == [0, 0, 0]:
                            mid_pieces_reverse[c][x][y] = [destination_face, y, N - 1 - x]

                    elif mid_pieces[destination_face][y][N - 1 - x] == [0, 0, 0] and state[destination_face][y][
                        N - 1 - x] != state[c][x][y]:
                        mid_pieces[destination_face][y][N - 1 - x] = [c, x, y]
                        if mid_pieces_reverse[c][y][N - 1 - x] == [0, 0, 0]:
                            mid_pieces_reverse[c][y][N - 1 - x] = [destination_face, y, N - 1 - x]

                    elif mid_pieces[destination_face][N - 1 - y][x] == [0, 0, 0] and state[destination_face][N - 1 - y][
                        x] != state[c][x][y]:
                        mid_pieces[destination_face][N - 1 - y][x] = [c, x, y]
                        if mid_pieces_reverse[c][N - 1 - y][x] == [0, 0, 0]:
                            mid_pieces_reverse[c][N - 1 - y][x] = [destination_face, y, N - 1 - x]

                    elif mid_pieces[destination_face][N - 1 - x][N - 1 - y] == [0, 0, 0] and \
                            state[destination_face][N - 1 - x][N - 1 - y] != state[c][x][y]:
                        mid_pieces[destination_face][N - 1 - x][N - 1 - y] = [c, x, y]
                        if mid_pieces_reverse[c][N - 1 - x][N - 1 - y] == [0, 0, 0]:
                            mid_pieces_reverse[c][N - 1 - x][N - 1 - y] = [destination_face, y, N - 1 - x]

    return mid_pieces, mid_pieces_reverse


def scrambler(n):
    no_of_moves = random.randint(100, 500)
    print(no_of_moves)
    for i in range(no_of_moves):
        a = random.randint(0, 11)
        b = random.randint(0, int(n / 2) - 1)
        x[a](b)
    return state


def flips_generator():
    flips = []

    def flip_top_to_front():
        state[3] = rotate_anti_clockwise(state[3])
        state[2] = rotate_clockwise(state[2])
        state[0], state[1] = state[1], state[0]
        state[5], state[4] = state[4], state[5]
        state[0], state[4] = state[4], state[0]
        return state

    flips.append(flip_top_to_front)

    def flip_top_to_back():
        state[3] = rotate_clockwise(state[3])
        state[2] = rotate_anti_clockwise(state[2])
        state[0], state[1] = state[1], state[0]
        state[5], state[4] = state[4], state[5]
        state[1], state[5] = state[5], state[1]
        return state

    flips.append(flip_top_to_back)

    def flip_top_to_right():
        state[0] = rotate_anti_clockwise(state[0])
        state[4] = rotate_clockwise(state[4])
        state[2], state[1] = state[1], state[2]
        state[5], state[3] = rotate_clockwise(rotate_clockwise(state[3])), rotate_clockwise(rotate_clockwise(state[5]))
        state[2], state[3] = state[3], state[2]
        return state

    flips.append(flip_top_to_right)

    def flip_top_to_left():
        state[0] = rotate_clockwise(state[0])
        state[4] = rotate_anti_clockwise(state[4])
        state[2], state[1] = state[1], state[2]
        state[5], state[3] = rotate_clockwise(rotate_clockwise(state[3])), rotate_clockwise(rotate_clockwise(state[5]))
        state[1], state[5] = rotate_clockwise(rotate_clockwise(state[5])), rotate_clockwise(rotate_clockwise(state[1]))
        return state

    flips.append(flip_top_to_left)

    return flips


def center_piece_solver():
    mid, mid_rev = mid_pieces_locator({"b": 0, "r": 1, "w": 2, "y": 3, "g": 4, "o": 5})
    temporary = {}
    for i in range(N):
        for j in range(N):
            if mid[1][i][j] != [0, 0, 0]:
                if mid[1][i][j][0] == 5:
                    temporary[(i, j)] = mid[1][i][j]
                    continue
                center_piece_arranger([i, j], mid[1][i][j], "r", x)
    for i in temporary:
        center_piece_arranger(i, mid[1][i[0]][i[1]], "r", x)

    y[0]()
    mid, mid_rev = mid_pieces_locator({"b": 1, "r": 4, "w": 2, "y": 3, "g": 5, "o": 0})
    temporary = {}
    for i in range(N):
        for j in range(N):
            if mid[1][i][j] != [0, 0, 0]:
                if mid[1][i][j][0] == 5:
                    temporary[(i, j)] = mid[1][i][j]
                    continue
                center_piece_arranger([i, j], mid[1][i][j], "b", x)
    for i in temporary:
        center_piece_arranger(i, mid[1][i[0]][i[1]], "b", x)

    y[2]()
    mid, mid_rev = mid_pieces_locator({"b": 3, "r": 4, "w": 1, "y": 5, "g": 2, "o": 0})
    temporary = {}
    for i in range(N):
        for j in range(N):
            if mid[1][i][j] != [0, 0, 0]:
                if mid[1][i][j][0] == 5:
                    temporary[(i, j)] = mid[1][i][j]
                    continue
                center_piece_arranger([i, j], mid[1][i][j], "w", x)
    for i in temporary:
        center_piece_arranger(i, mid[1][i[0]][i[1]], "w", x)

    y[0]()
    mid, mid_rev = mid_pieces_locator({"b": 3, "r": 5, "w": 4, "y": 0, "g": 2, "o": 1})
    temporary = {}
    for i in range(N):
        for j in range(N):
            if mid[1][i][j] != [0, 0, 0]:
                if mid[1][i][j][0] == 5:
                    temporary[(i, j)] = mid[1][i][j]
                    continue
                center_piece_arranger([i, j], mid[1][i][j], "o", x)
    for i in temporary:
        center_piece_arranger(i, mid[1][i[0]][i[1]], "o", x)

    y[2]()
    mid, mid_rev = mid_pieces_locator({"b": 5, "r": 2, "w": 4, "y": 0, "g": 1, "o": 3})
    temporary = {}
    for i in range(N):
        for j in range(N):
            if mid[1][i][j] != [0, 0, 0]:
                if mid[1][i][j][0] == 5:
                    temporary[(i, j)] = mid[1][i][j]
                    continue
                center_piece_arranger([i, j], mid[1][i][j], "g", x)
    for i in temporary:
        center_piece_arranger(i, mid[1][i[0]][i[1]], "g", x)

    y[0]()
    y[2]()


def edge_locator(a, b):
    flip_count = 0
    edge_location = list([0, 0] for i in range(N))
    while flip_count < 4:
        for i in range(1, N - 1):
            if state[1][i][0] + state[2][i][N - 1] == a + b or state[1][i][0] + state[2][i][N - 1] == b + a:
                if state[4][i][0] + state[2][-1][N - 1 - i] == a + b or \
                        state[4][i][0] + state[2][-1][N - 1 - i] == b + a:
                    if flip_count != 1:
                        edge_location[i] = [i, flip_count * 3 + 1]

                elif state[4][N - i - 1][0] + state[2][-1][i] == a + b or \
                        state[4][N - i - 1][0] + state[2][-1][i] == b + a:
                    if flip_count != 1:
                        edge_location[N - i - 1] = [i, flip_count * 3 + 1]

                else:
                    if flip_count != 1:
                        if edge_location[i] == [0, 0]:
                            edge_location[i] = [i, flip_count * 3 + 1]

                        else:
                            edge_location[N - i - 1] = [i, flip_count * 3 + 1]

            if state[1][i][N - 1] + state[3][i][0] == a + b or state[1][i][N - 1] + state[3][i][0] == b + a:
                if state[4][i][0] + state[2][-1][N - 1 - i] == a + b or \
                        state[4][i][0] + state[2][-1][N - 1 - i] == b + a:
                    edge_location[i] = [i, flip_count * 3 + 3]

                elif state[4][N - i - 1][0] + state[2][-1][i] == a + b or \
                        state[4][N - i - 1][0] + state[2][-1][i] == b + a:
                    edge_location[N - i - 1] = [i, flip_count * 3 + 3]

                else:
                    if edge_location[i] == [0, 0]:
                        edge_location[i] = [i, flip_count * 3 + 3]

                    else:
                        edge_location[N - i - 1] = [i, flip_count * 3 + 3]

        for i in range(1, N - 1):
            if state[1][N - 1][i] + state[4][0][i] == a + b or state[1][N - 1][i] + state[4][0][i] == b + a:
                if state[4][i][0] + state[2][-1][N - 1 - i] == a + b or \
                        state[4][i][0] + state[2][-1][N - 1 - i] == b + a:
                    edge_location[i] = [i, flip_count * 3 + 2]

                elif state[4][N - i - 1][0] + state[2][-1][i] == a + b or \
                        state[4][N - i - 1][0] + state[2][-1][i] == b + a:
                    edge_location[N - i - 1] = [i, flip_count * 3 + 2]

                else:
                    if edge_location[i] == [0, 0]:
                        edge_location[i] = [i, flip_count * 3 + 2]

                    else:
                        edge_location[N - i - 1] = [i, flip_count * 3 + 2]

        y[1]()
        flip_count = flip_count + 1
    return edge_location


def edge_arranger(i, func):
    func[8](i)
    func[3](0)
    func[4](0)
    func[9](0)
    func[2](0)
    func[5](0)
    func[9](i)
    func[4](0)
    func[3](0)
    func[8](0)
    func[5](0)
    func[2](0)


def edge_solver(func):
    pieces = [["r", "w"], ["r", "g"], ["r", "y"], ["g", "w"], ["g", "o"], ["g", "y"], ["o", "w"], ["o", "b"],
              ["o", "y"], ["b", "w"], ["b", "r"], ["b", "y"]]

    if N % 2 != 0:
        for i in pieces:
            a = edge_locator(i[0], i[1])
            b = a[int(N / 2)][1]
            c = a[int(N / 2)][0]
            if b == 1:
                if state[1][c][0] == i[0]:
                    func[2](0)
                else:
                    func[9](0)
                    func[5](0)

            elif b == 2:
                if state[1][N - 1][c] == i[0]:
                    func[8](0)
                    func[2](0)
                else:
                    func[5](0)

            elif b == 3:
                if state[1][c][N - 1] == i[0]:
                    func[8](0)
                    func[8](0)
                    func[2](0)

                else:
                    func[8](0)
                    func[5](0)

            elif b == 0:
                if state[4][c][0] != i[0]:
                    func[3](0)
                    func[9](0)
                    func[5](0)

            elif b == 5:
                if state[4][N - 1][c] == i[0]:
                    func[4](0)
                else:
                    func[11](0)
                    func[3](0)

            elif b == 6:
                if state[4][c][N - 1] == i[0]:
                    func[4](0)
                    func[4](0)
                else:
                    func[1](0)
                    func[11](0)
                    func[4](0)

            elif b == 7:
                if state[5][c][0] == i[0]:
                    func[3](0)
                else:
                    func[10](0)
                    func[4](0)

            elif b == 8:
                if state[5][N - 1][c] == i[0]:
                    func[10](0)
                    func[3](0)
                else:
                    func[7](0)
                    func[2](0)
                    func[2](0)

            elif b == 9:
                if state[5][c][N - 1] == i[0]:
                    func[10](0)
                    func[10](0)
                    func[3](0)
                else:
                    func[10](0)
                    func[7](0)
                    func[2](0)
                    func[2](0)

            elif b == 10:
                if state[0][c][0] == i[0]:
                    func[2](0)
                    func[2](0)
                else:
                    func[7](0)
                    func[9](0)
                    func[2](0)

            elif b == 11:
                if state[0][N - 1][c] == i[0]:
                    func[6](0)
                    func[2](0)
                    func[2](0)
                else:
                    func[9](0)
                    func[2](0)

            elif b == 12:
                if state[0][c][N - 1] == i[0]:
                    func[0](0)
                    func[0](0)
                    func[4](0)
                    func[4](0)
                else:
                    func[6](0)
                    func[9](0)
                    func[2](0)

            a = edge_locator(i[0], i[1])
            print(a)
            for j in range(int(N / 2)):
                b = a[j][1]
                if b == 1:
                    if state[1][c][0] == i[0]:
                        func[2](0)
                    else:
                        func[9](0)
                        func[5](0)

                elif b == 2:
                    if state[1][N - 1][c] == i[0]:
                        func[8](0)
                        func[2](0)
                    else:
                        func[5](0)

                elif b == 3:
                    if state[1][c][N - 1] == i[0]:
                        func[8](0)
                        func[8](0)
                        func[2](0)

                    else:
                        func[8](0)
                        func[5](0)

                elif b == 0:
                    if state[4][c][0] != i[0]:
                        func[3](0)
                        func[9](0)
                        func[5](0)

                elif b == 5:
                    if state[4][N - 1][c] == i[0]:
                        func[4](0)
                    else:
                        func[11](0)
                        func[3](0)

                elif b == 6:
                    if state[4][c][N - 1] == i[0]:
                        func[4](0)
                        func[4](0)
                    else:
                        func[1](0)
                        func[11](0)
                        func[4](0)

                elif b == 7:
                    if state[5][c][0] == i[0]:
                        func[3](0)
                    else:
                        func[10](0)
                        func[4](0)

                elif b == 8:
                    if state[5][N - 1][c] == i[0]:
                        func[10](0)
                        func[3](0)
                    else:
                        func[7](0)
                        func[2](0)
                        func[2](0)

                elif b == 9:
                    if state[5][c][N - 1] == i[0]:
                        func[10](0)
                        func[10](0)
                        func[3](0)
                    else:
                        func[10](0)
                        func[7](0)
                        func[2](0)
                        func[2](0)

                elif b == 10:
                    if state[0][c][0] == i[0]:
                        func[2](0)
                        func[2](0)
                    else:
                        func[7](0)
                        func[9](0)
                        func[2](0)

                elif b == 11:
                    if state[0][N - 1][c] == i[0]:
                        func[6](0)
                        func[2](0)
                        func[2](0)
                    else:
                        func[9](0)
                        func[2](0)

                elif b == 12:
                    if state[0][c][N - 1] == i[0]:
                        func[0](0)
                        func[0](0)
                        func[4](0)
                        func[4](0)
                    else:
                        func[6](0)
                        func[9](0)
                        func[2](0)


state, N = splitter("oyrywwbrryrgogyrygbyorrroygrwbgrggwwggooyowbrwrwygbbyyroyrrwwroygoywrwrbryggbgwbyoybygbgoooowyrgwyrrygrybwwwyorobgoogrbwgbgbbrbwgowyrgbogorgbgrywywwryggoyggwgwyygryyyrwrgywwroorbybowrgwbywrwggbrggorgwogbbggwgbgowoorbygwoboobyogwyorwbgbbyrwbgggogybgyggobywoogowyygbobgwowggbyorroooyboowgobygoooyoyogyggoorrggwybrgyogowrrrgyobborwgygoybrbgbgbwwgbogbyroybwbwgwwywroyygobrgboyrbgobybbborrggwbrbwbwgyobwgoggwgoygggywwbgrwgorrgryygorggggrrwryogrgobroygwogyrorgogbyywgbryboyoworrbwbrboygogbygyyoooyrwowywyogrgwwbyrowroggbwrbboowgoowwrwwygyryyowbwwoywgbgrbwwrgrbgrboowggbybyywwwbyryoogwgbbyybygorrroywoorowrorbboyrybwoybbowboobgrwoybobrowworbwgywwwogrrworwwbroywoobyobboyrroyrygrgoowybyoboooorroobygwbrwbryyrgoyowrbbrbrrygwwbwgrrbgogrwrgwgbrrowbwybogwowrryobrywywbbgyyoryrwyoyoywggogorbrgggyyborgoooywgbywgrrwgwbbogboyybbrgryobbrrbyoyoywyygoybrbgoyygwryyrogbrworowoworooboorywyrrbgwrwbgggbrrywrbgbybobyorgbgybgrgyyobwwwgbrwbgbwrryrbyrgbrrgwoyorygbwgyywyybybgybywborbbggrwgywggyywwrroroogbybwgwwbborboggogggowroorgoyyboyogrwggwbywrbryoyowywyooorbbgyrywyorwgowogrbgwgrbbygwrygyybryrworwwyrboboyyoggwrgrooyyrbbwbrogbyggywwobowroywbgrgwwwbbgyrrgbrogygrbwrgwgworbogobygwyywyooobrbowbrroorbgyoobwrrwroroogrgwrbbbbowywygwwwoobbbworgbygrbgowryyogwwwygbggrroroygwwoobwoygobyrbgywybogggyyyyrgowwbbggrwrbowrygbryyobwboyowbrwbgrgbbrgbgyyrooogrbowbrbbbwbobwwwgwwryrorygggowbbrgowwbwwyybggybwbrboywwowoywyobgwbrgrrwwyrobwyybwogygggrggooybygobyyrgoowrwwgwooggwyogwoywgbyygbwbygowwybwowwgwbrobbwyogowbgygoowwggwoowrroggbgrowwgoooooorrogowgybwrowobrogrowgwrrgrooyoryrbbygyoygrrrybwbwbwoobowwryrbwbwyrwgygrgryworggbyrywgwwoybggyyoygbgoggwygbbwroywgrbrrrwyrrggyggywyogwbywygrggooybrwogrwwwggbbwworybwgrrggyrggbryrrbryrboyobbgbybwgggbrgwwrwgryywgoywoooggwbrbbbwrgrwgogwygwgoogyoorbwwoybbwgogrbgboywryowggwwbryowooryorobrgbrwgyrywygbrgwgygbbbgygboororbobygyrwrwbgggwrgbobroroorrbgrgwgwggggrrbbybwygowryyobowbywrrgwggyywrwwgbwrwgboroyyyrrwbbyyrybrbrwoywwwgbwwbybrggrgywywogwwryowwwrybrrgogrgwowbwybrgbwwrywbwgwbwybgrwwwryrroyobbgrgybygoryrwroyoywygwgowwwybggoybbygyyrwboyyyrbygyoggyyowyogwogyroowrgbwbogwwbybygrbbgogwowworygrygooywgrywywyborwyryoygoobwrwgorygrogbrgwygwyorbbbowgoworrgwoogwrbbbbwogorrrwbyooobrwoybbrygyrgogoyrbwryyobywwgoyygyorrwbgwooowrrbgryybybgrgoborbyyygyrywybbgwowooobyoroorgoyrbywyyybyogbobbowrwbrbwwrbrbyoryygyooygoowbwrbrbgyrowrbobowwwywrgyroywogybogwwbybgyyowwowrobwbwgybgoyowoywrrrgowrrwbrygoggyywrobgrbbrggbygyrrrrowogbgboywryrrrborgrobrborrrrgybwybybgyyrygwbbooybowrrbogbbrobwbborrybgyyyywygbwygobgrrbogywoyoryybrorgobgorrbrwgrbbwboywwwborrgbygrbwyrrgrboyoryroogyyobgggbwgwrrwbyyowrogrrrrrwbyrowywrrgwgoowgyoywoywwwooygyyworryoobywogywyyggygbborworbwyrgyygrooooorgbybrgwbwowwbgrwboowgbgrryygbowrgoroywggwogybbgyoorgwworowbgrrwrorbyggrboogorywygbwwyyrowyoybbwryogbwowbbwogwwbwybbyobborbwgbowbggbworrryobbwrwbbwgwowrbgoywwroorggyowoyrbgwbrgwoyggbwwrowgbwbwrooowgoybgyoorwgyybggorwowyobwbbrgoryrrgoywrgyorwryogogwyowbbwwgrwgobrorgyyoywyyrwogbroooyroooyorgbryggrybrwbbyrworwowywowbworgbbyyworobggorrbgobbwybwrrwbggrwywrwrrbbobryrygborwwybworrrwrobwbrgygryybbryygoyyyyywborrggyryrbrwyyrbyyboryoyygybgoyybyowwwwwywgobwggyooyogbwrrgbyrorgwwrggrooryoygrbybgrbgyyorbyobogowbogobyowwwyyrrybyobrgbwwyogbwyrgyrrggwybywgyrgooggyygbgooyrgowywbwgwwgogrwwwbrrogyybyrgborywbyoworbrgrrwoygrrbgbowwrgoggggowywgyybroybwwrgwbowggobwwbbrgrwbygobywrgwwrroogrgygwwyygrwrrgrrryyorbgrbyyrrrgbbwgwogggrgrwrwwbybywgogwyygbwwboygoogrgyyryrwrwgwrrbwrbgogwbogobwgrygwrrwooboyybrbroborwyrgbogyrrywyoybgoowworogwgybbgwrggybbgbybbrgobbrggygwogrbbowoyrggroggwwrbbyryrbywwyryggwwbowwbwrobrbwwgbbywyobgoywgrbrwbwgobrwggboogbobwoygygrwbwwyyowwrbrbrbygrrgyygbbbbggyrroybbwrrwwygobbgyoggywwbwrrrwwrgryrybgrobywyrwywworboorrrybgboyogbwrwggbgbobrgrwwrworwgoyyobgwywoorrgyobgroroogwgbgrwgbbyrbrgwwrwwogwbyogrgbwyboywwogyywogoooywrbgoybgrboryrboyrwwwgyrgbggbyrgoggorrwgwooobobbbowoogoyyooborgywbrrobgrbogwrrwwyobyrbyogyorybryobyogowbyyogogrgwobooygobrbyooogrobrybywrwwwbgrrorrrwrgooowyryowoyoybrgwgryywyobrwybowboowwgwgwgwggroorrywgyoygggoogbwoygrbbbrywoywbygogrybwwbryrgwyggwbgrrwbrrobbrywwogowggrgrryroyobrgooowrorowwwgygybbbrygbbrgwwwboooyobwggryoyrrorbgyybwyogbybrogrgoybggrrbobwyggrwwwrborrrbggrywbbggwyowbygoywbggoryrrrgggywrbrogowyrbwrbrbyyobrgrgoorbgygbgrgobogbywwgbyyboyyyygrogowroggoboryboowobrybwyybwybbwwwroybwwbybgrrbrwyyoygoyrbbbrrywbyyrgbwgwbybobywybbooggrggorbrgwrgbywrbgrgwywworbgywrbgrwoyoywgrrgrbrwoygbbwrbgbrrwoyboroyowrbwgroroygyggygwbbgrgrywowboyrgogrwwoybbrwwwogrwowbbboywogrwrworrrgyorwwgwroyrryyyoggorbwbybbwrbbbrbwwwbbbwrbbrbgybrbobygrgggyrwwygwbrwbygrogbygorgbowbowyybgoybbbgrgoggogrwwooogyyyybygrobrywoobrrrrrrrbrgrwbwrborrwogbywwgwywwybwbgwogbryogbgygygbyobgwywwoowgrbywyoogoryobgrwyyoboyyooorboowwbwwywrywgrbboobobrwgrwygybybbbboroygbgyoborrgrorywoyywbrbgbrrbgwwyborgyrgwgggyybooogywwgrrgogbbwrgyrywbbgwrrbowroogbwgbrwgygrgoogrgowbrygyrgbrbywwoogywgyrbbgrbwobwowobgbgbywbgbwrygrwyoorgywbyrgrrrwbwooybywgyrwwwrwoywbyywoygobwgybgyyyoygygybwwyyrooggogrrgbrgggrbbwwogryyyrwwgybrygyybwrbgoybobbbwrgrgoyrobroybwowgbyyyyrggrybrwrogywrbrogoowwgbobygggooobwbgyoyrbrogyogrboowowgwroyrwrogrbgbywwyybbobgywybyrbrgoryrwowgybwogryybybbggwyoboobybwowyrwbygbyyrgbryrorgwoygyowoggywowgwobbgbbgwggrggwobowygbobgoowgybbyggrwgbgbgroygoygybyyybgooggbrowyoggbywwbyoorwgyryrbrobyrooryywogyyobboygobywbborooygwrwbgowrwogwrowwgbwgrwoyrgrobrooowwwogbrwoyrgryywyboyyrybgrbbwrwgrygobwbybowywrbbbrobbogbworoybygorrgyogooorbgwgyroorgywybrywoggbboybwrorogyboywyrwbwwggyyrrbogyoywyyygbywybbbgryorggwyyyoyorbbobwbywgybyrobbygygrrgybwrorowwyyogbyyogrggobgwybyrgogrobgoooowbrwyogbgyryygowwbgbrbrwybrrbbyggorygoyygrbwwgrrwwobbogggwgwwrgyywogbybbwoyoybgogwgyoyybybwbyygyoywwwgyywgwbrwwyyborwoorrrywyoboobgroogyroygyrogrrwwwwbbobbwgwowwbygogwgwoobbwrrgbryyobgywbbggggggobbywyogybobyrgwbyrbgowywywyyrwyrwwyyybbybyrywrywoybrywwogrooboorobyyyyrwwwggggyyoywowrbrrgrrrgoggyowbgyowbwobbgggrgroowyrbboggrorrwgyyobowggbowbywworrybogrbwybrgwyyoroboorgbgyowyggygogybwbyyyoygrywoobgbrywyybrwyyorrroryywgoowbrggrggrgrwywbggybwbywbrwogroroybgrrbogowrrgrwyrbrgryyywwrgyroowyoyrwrwbyogbbrbgwgrbgwbbrbgyrbgwwobwrbobbyybrgbygooygrwwbwgooggywyygwwwbwbgwgrgrwroboowywrroowbbwoororbgggrobyrbygyywywbwgrrbwywgywgwgwgbwyrybwwgywoybbgorrgogbooybborgwrgogyrowyyrrbybgwogwggryrobrrbrrbrwbgwwyoyogbbbwrgrwrrgyrboogorryrywwboowrwyorbbbrwygrobrbwwoborrwwybogbyowgobrrrbgyrowybbrybbgoorryogrrbwbgbbgborgbbbwywogrywbwbbyobwyoyywgyyrowgwywbrrwbowgbrwbgrorbybrbwwyygbryoyygoyowgbwbroobywywygbbrrwrwygrgryobbgryyowbogbooobgorgoogbrbroybryooooybybbywobbrobyorwgoboywwowrbwroobbyboowbbbgyyrbbrwbygyoobbywrwbwogbgwyrrgrbgwrybywogwybrrwggwyrgbrywrooyygrbwbwwyorbborwgrwobgybyowyoybbyborgwowbgobowrbygggrrywoybwyowwbrwgyyggwborrbgbbgyoggobwwrowgrrgwgoboygryygywwoybbbrobgowobwwrwybbowowowryggygbwyrgbowwwyggowywoowbywywyyrgboyrbwobrwbwobwwgowgwogbbbyrrgyggywgrybgwryygggyygwoogyorwgrywrrywgyrryrwyogbbrobrwyorowwowrwbbyoyrrwygowywwygwyroyoogbgrwrygyrbgywyrgbrogorgwygowrgrwbbowbrogybgwwrrrbbrrgyrggwyoogowwobrwworgggbyywwrwgyobwbyyyybwbygwrrrbobwrwboyyoorbbrobboygroryrrowryogwgyggbbyrrygwggwroryogoorooryoooggrbrrwwbowyyogbgbyroorbogooooyobbbyoborbyoobgowbywgbygogwbwwgwbgrbgowbbbwyyrrwwbyyoobgbgbwywbbrorowrroyrbwbyyrwbgbrrgwbwrrbwrggbrogowbrobbrggwrryyyowyyogwrowwywybbbwwbogbyrbgroroobygwbyrywoybwwoybywooybworrwgwrgorrbyrgybwbyyrwbyoroygoorbrororwwobryggrwryyygygwyywbgbyywyrgogwyggyobrgbowwrrbbywbwwowbbworgybyggoyrryborgwwygbowbgrwwowb")
x = moves_generator(N)
y = flips_generator()
center_piece_solver()
print(NUMBER_OF_MOVES)
display_cube(state)
print(time.time() - time1)
