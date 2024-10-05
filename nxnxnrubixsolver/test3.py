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
        print(f"R{i}")

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
        print(f"Rdash{i}")

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
        print(f"L{i}")

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
        print(f"Ldash{i}")

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
        print(f"F{i}")

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
        print(f"Fdash{i}")

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
        print(f"B{i}")

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
        print(f"Bdash{i}")

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
        print(f"U{i}")

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
        print(f"Udash{i}")

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
        print(f"D{i}")

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
        print(f"Ddash{i}")

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
        print("flip top to front")
        return state

    flips.append(flip_top_to_front)

    def flip_top_to_back():
        state[3] = rotate_clockwise(state[3])
        state[2] = rotate_anti_clockwise(state[2])
        state[0], state[1] = state[1], state[0]
        state[5], state[4] = state[4], state[5]
        state[1], state[5] = state[5], state[1]
        print("flip top to back")
        return state

    flips.append(flip_top_to_back)

    def flip_top_to_right():
        state[0] = rotate_anti_clockwise(state[0])
        state[4] = rotate_clockwise(state[4])
        state[2], state[1] = state[1], state[2]
        state[5], state[3] = rotate_clockwise(rotate_clockwise(state[3])), rotate_clockwise(rotate_clockwise(state[5]))
        state[2], state[3] = state[3], state[2]
        print("flip top to right")
        return state

    flips.append(flip_top_to_right)

    def flip_top_to_left():
        state[0] = rotate_clockwise(state[0])
        state[4] = rotate_anti_clockwise(state[4])
        state[2], state[1] = state[1], state[2]
        state[5], state[3] = rotate_clockwise(rotate_clockwise(state[3])), rotate_clockwise(rotate_clockwise(state[5]))
        state[1], state[5] = rotate_clockwise(rotate_clockwise(state[5])), rotate_clockwise(rotate_clockwise(state[1]))
        print("flip top to left")
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
    p = [4, 1, 0, 5]
    while flip_count < 4:
        for i in range(1, N - 1):
            q = [state[2][-1][N - 1 - i], state[2][i][N - 1], state[2][0][i], state[2][N - 1 - i][0]]
            r = [state[2][-1][i], state[2][N - 1 - i][N - 1], state[2][0][N - 1 - i], state[2][i][0]]
            if state[1][i][0] + state[2][i][N - 1] == a + b or state[1][i][0] + state[2][i][N - 1] == b + a:
                if state[p[flip_count]][i][0] + q[flip_count] == a + b or \
                        state[p[flip_count]][i][0] + q[flip_count] == b + a:
                    if flip_count != 1:
                        edge_location[i] = [i, flip_count * 3 + 1]
                elif state[p[flip_count]][N - i - 1][0] + r[flip_count] == a + b or \
                        state[p[flip_count]][N - i - 1][0] + r[flip_count] == b + a:
                    if flip_count != 1:
                        edge_location[N - i - 1] = [i, flip_count * 3 + 1]

                else:
                    if flip_count != 1:
                        if state[1][i][0] + state[2][i][N - 1] == a + b:
                            edge_location[N - i - 1] = [i, flip_count * 3 + 1]
                        else:
                            edge_location[i] = [i, flip_count * 3 + 1]

            if state[1][i][N - 1] + state[3][i][0] == a + b or state[1][i][N - 1] + state[3][i][0] == b + a:
                if state[p[flip_count]][i][0] + q[flip_count] == a + b or \
                        state[p[flip_count]][i][0] + q[flip_count] == b + a:
                    edge_location[i] = [i, flip_count * 3 + 3]

                elif state[p[flip_count]][N - i - 1][0] + r[flip_count] == a + b or \
                        state[p[flip_count]][N - i - 1][0] + r[flip_count] == b + a:
                    edge_location[N - i - 1] = [i, flip_count * 3 + 3]

                else:
                    if state[1][i][N - 1] + state[3][i][0] == a + b:
                        edge_location[i] = [i, flip_count * 3 + 3]
                    else:
                        edge_location[N - i - 1] = [i, flip_count * 3 + 3]

        for i in range(1, N - 1):
            q = [state[2][-1][N - 1 - i], state[2][i][N - 1], state[2][0][i], state[2][N - 1 - i][0]]
            r = [state[2][-1][i], state[2][N - 1 - i][N - 1], state[2][0][N - 1 - i], state[2][i][0]]
            if state[1][N - 1][i] + state[4][0][i] == a + b or state[1][N - 1][i] + state[4][0][i] == b + a:
                if state[p[flip_count]][i][0] + q[flip_count] == a + b or \
                        state[p[flip_count]][i][0] + q[flip_count] == b + a:
                    edge_location[i] = [i, flip_count * 3 + 2]

                elif state[p[flip_count]][N - i - 1][0] + r[flip_count] == a + b or \
                        state[p[flip_count]][N - i - 1][0] + r[flip_count] == b + a:
                    edge_location[N - i - 1] = [i, flip_count * 3 + 2]

                else:
                    if state[1][N - 1][i] + state[4][0][i] == a + b:
                        edge_location[N - i - 1] = [i, flip_count * 3 + 2]
                    else:
                        edge_location[i] = [i, flip_count * 3 + 2]

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


def parity(func, i):
    func[1](i)
    func[8](0)
    func[8](0)
    func[2](i)
    func[4](0)
    func[4](0)
    func[3](i)
    func[4](0)
    func[4](0)
    func[0](i)
    func[0](i)
    func[8](0)
    func[8](0)
    func[0](i)
    func[8](0)
    func[8](0)
    func[1](i)
    func[8](0)
    func[8](0)
    func[4](0)
    func[4](0)
    func[0](i)
    func[0](i)
    func[4](0)
    func[4](0)


def edge_solver(func):
    pieces = [["r", "w"], ["r", "g"], ["r", "y"], ["g", "w"], ["g", "o"], ["g", "y"], ["o", "w"], ["o", "b"],
              ["o", "y"], ["b", "w"], ["b", "r"], ["b", "y"]]
    for i in pieces:
        if N % 2 != 0:
            a = edge_locator(i[0], i[1])
            b = a[int(N / 2)][1]
            c = int(N / 2)
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

        else:
            v1 = pieces.index(i) % 4
            if v1 == 0:
                y[0]()
            elif v1 == 1:
                y[2]()
            elif v1 == 2:
                y[1]()
            else:
                y[3]()
        a = edge_locator(i[0], i[1])
        for j in range(1, int(N / 2)):
            b = a[j][1]
            if b == 1:
                if j == a[j][0]:
                    func[9](0)
                    func[4](0)
                    func[0](0)
                    func[5](0)
                    func[1](0)
                else:
                    func[9](0)
                    func[9](0)
                    func[1](0)
            elif b == 2:
                if j == a[j][0]:
                    func[4](0)
                    func[0](0)
                    func[5](0)
                    func[1](0)
                else:
                    func[9](0)
                    func[1](0)
            elif b == 3:
                if j == a[j][0]:
                    func[1](0)
                else:
                    func[8](0)
                    func[4](0)
                    func[0](0)
                    func[5](0)
                    func[1](0)
            elif b == 5:
                if j == a[j][0]:
                    func[10](0)
                    func[0](0)
                else:
                    func[5](0)
                    func[0](0)
                    func[4](0)
                    func[1](0)
            elif b == 6:
                if j != a[j][0]:
                    func[4](0)
                    func[10](0)
                    func[5](0)
                    func[0](0)
            elif b == 7:
                if j == a[j][0]:
                    func[10](0)
                    func[5](0)
                    func[0](0)
                    func[4](0)
                    func[1](0)
                else:
                    func[10](0)
                    func[10](0)
                    func[0](0)
            elif b == 8:
                if j == a[j][0]:
                    func[6](0)
                    func[0](0)
                    func[0](0)
                else:
                    func[11](0)
                    func[0](0)
            elif b == 9:
                if j == a[j][0]:
                    func[0](0)
                else:
                    func[11](0)
                    func[5](0)
                    func[0](0)
                    func[4](0)
                    func[1](0)
            elif b == 10:
                if j == a[j][0]:
                    func[7](0)
                    func[8](0)
                    func[1](0)
                else:
                    func[6](0)
                    func[6](0)
                    func[0](0)
                    func[0](0)
            elif b == 11:
                if j == a[j][0]:
                    func[8](0)
                    func[1](0)
                else:
                    func[7](0)
                    func[0](0)
                    func[0](0)
            elif b == 12:
                if j == a[j][0]:
                    func[0](0)
                    func[0](0)
                else:
                    func[6](0)
                    func[8](0)
                    func[1](0)
            if a[j] != [0, 0]:
                edge_arranger(j, func)

            if b == 1:
                if j == a[j][0]:
                    func[0](0)
                    func[4](0)
                    func[1](0)
                    func[5](0)
                    func[8](0)
                else:
                    func[0](0)
                    func[8](0)
                    func[8](0)
            elif b == 2:
                if j == a[j][0]:
                    func[0](0)
                    func[4](0)
                    func[1](0)
                    func[5](0)
                else:
                    func[0](0)
                    func[8](0)
            elif b == 3:
                if j == a[j][0]:
                    func[0](0)
                else:
                    func[0](0)
                    func[4](0)
                    func[1](0)
                    func[5](0)
                    func[9](0)
            elif b == 5:
                if j == a[j][0]:
                    func[1](0)
                    func[11](0)
                else:
                    func[0](0)
                    func[5](0)
                    func[1](0)
                    func[4](0)
            elif b == 6:
                if j != a[j][0]:
                    func[1](0)
                    func[4](0)
                    func[11](0)
                    func[5](0)
            elif b == 7:
                if j == a[j][0]:
                    func[0](0)
                    func[5](0)
                    func[1](0)
                    func[4](0)
                    func[11](0)
                else:
                    func[1](0)
                    func[11](0)
                    func[11](0)
            elif b == 8:
                if j == a[j][0]:
                    func[1](0)
                    func[1](0)
                    func[7](0)
                else:
                    func[1](0)
                    func[10](0)
            elif b == 9:
                if j == a[j][0]:
                    func[1](0)
                else:
                    func[0](0)
                    func[5](0)
                    func[1](0)
                    func[4](0)
                    func[10](0)
            elif b == 10:
                if j == a[j][0]:
                    func[0](0)
                    func[9](0)
                    func[6](0)
                else:
                    func[1](0)
                    func[1](0)
                    func[7](0)
                    func[7](0)
            elif b == 11:
                if j == a[j][0]:
                    func[0](0)
                    func[9](0)
                else:
                    func[1](0)
                    func[1](0)
                    func[6](0)
            elif b == 12:
                if j == a[j][0]:
                    func[1](0)
                    func[1](0)
                else:
                    func[0](0)
                    func[9](0)
                    func[7](0)

        a = edge_locator(i[0], i[1])
        for j in range(1, N):
            b = a[j][1]
            if b == 1:
                if j == a[j][0]:
                    func[9](0)
                    func[4](0)
                    func[0](0)
                    func[5](0)
                    func[1](0)
                else:
                    func[9](0)
                    func[9](0)
                    func[1](0)
            elif b == 2:
                if j == a[j][0]:
                    func[4](0)
                    func[0](0)
                    func[5](0)
                    func[1](0)
                else:
                    func[9](0)
                    func[1](0)
            elif b == 3:
                if j == a[j][0]:
                    func[1](0)
                else:
                    func[8](0)
                    func[4](0)
                    func[0](0)
                    func[5](0)
                    func[1](0)
            elif b == 5:
                if j == a[j][0]:
                    func[10](0)
                    func[0](0)
                else:
                    func[5](0)
                    func[0](0)
                    func[4](0)
                    func[1](0)
            elif b == 6:
                if j != a[j][0]:
                    func[4](0)
                    func[10](0)
                    func[5](0)
                    func[0](0)
            elif b == 7:
                if j == a[j][0]:
                    func[10](0)
                    func[5](0)
                    func[0](0)
                    func[4](0)
                    func[1](0)
                else:
                    func[10](0)
                    func[10](0)
                    func[0](0)
            elif b == 8:
                if j == a[j][0]:
                    func[6](0)
                    func[0](0)
                    func[0](0)
                else:
                    func[11](0)
                    func[0](0)
            elif b == 9:
                if j == a[j][0]:
                    func[0](0)
                else:
                    func[11](0)
                    func[5](0)
                    func[0](0)
                    func[4](0)
                    func[1](0)
            elif b == 10:
                if j == a[j][0]:
                    func[7](0)
                    func[8](0)
                    func[1](0)
                else:
                    func[6](0)
                    func[6](0)
                    func[0](0)
                    func[0](0)
            elif b == 11:
                if j == a[j][0]:
                    func[8](0)
                    func[1](0)
                else:
                    func[7](0)
                    func[0](0)
                    func[0](0)
            elif b == 12:
                if j == a[j][0]:
                    func[0](0)
                    func[0](0)
                else:
                    func[6](0)
                    func[8](0)
                    func[1](0)
            if a[j] != [0, 0]:
                edge_arranger(j, func)
            if b == 1:
                if j == a[j][0]:
                    func[0](0)
                    func[4](0)
                    func[1](0)
                    func[5](0)
                    func[8](0)
                else:
                    func[0](0)
                    func[8](0)
                    func[8](0)
            elif b == 2:
                if j == a[j][0]:
                    func[0](0)
                    func[4](0)
                    func[1](0)
                    func[5](0)
                else:
                    func[0](0)
                    func[8](0)
            elif b == 3:
                if j == a[j][0]:
                    func[0](0)
                else:
                    func[0](0)
                    func[4](0)
                    func[1](0)
                    func[5](0)
                    func[9](0)
            elif b == 5:
                if j == a[j][0]:
                    func[1](0)
                    func[11](0)
                else:
                    func[0](0)
                    func[5](0)
                    func[1](0)
                    func[4](0)
            elif b == 6:
                if j != a[j][0]:
                    func[1](0)
                    func[4](0)
                    func[11](0)
                    func[5](0)
            elif b == 7:
                if j == a[j][0]:
                    func[0](0)
                    func[5](0)
                    func[1](0)
                    func[4](0)
                    func[11](0)
                else:
                    func[1](0)
                    func[11](0)
                    func[11](0)
            elif b == 8:
                if j == a[j][0]:
                    func[1](0)
                    func[1](0)
                    func[7](0)
                else:
                    func[1](0)
                    func[10](0)
            elif b == 9:
                if j == a[j][0]:
                    func[1](0)
                else:
                    func[0](0)
                    func[5](0)
                    func[1](0)
                    func[4](0)
                    func[10](0)
            elif b == 10:
                if j == a[j][0]:
                    func[0](0)
                    func[9](0)
                    func[6](0)
                else:
                    func[1](0)
                    func[1](0)
                    func[7](0)
                    func[7](0)
            elif b == 11:
                if j == a[j][0]:
                    func[0](0)
                    func[9](0)
                else:
                    func[1](0)
                    func[1](0)
                    func[6](0)
            elif b == 12:
                if j == a[j][0]:
                    func[1](0)
                    func[1](0)
                else:
                    func[0](0)
                    func[9](0)
                    func[7](0)
        func[4](0)
        if N % 2 == 0:
            var = state[1][N - 1][1]
            l1 = []
            l2 = []
            for val in range(1, int(N / 2)):
                if state[1][N - 1][val] == var:
                    l1.append(val)
                else:
                    l2.append(val)
            if len(l1) > len(l2):
                for var_ in l2:
                    parity(func, N - 1 - var_)
            else:
                for var_ in l1:
                    parity(func, N - 1 - var_)
        else:
            var = state[1][N - 1][int(N / 2)]
            for val in range(1, int(N / 2)):
                if state[1][N - 1][val] != var:
                    parity(func, N - 1 - val)
        func[5](0)


def turn_generator():
    turns = []

    def turn_cube_right():
        state[1] = rotate_clockwise(state[1])
        state[5] = rotate_anti_clockwise(state[5])
        state[0], state[2], state[4], state[3] = rotate_clockwise(state[2]), rotate_clockwise(
            state[4]), rotate_clockwise(state[3]), rotate_clockwise(state[0])
        print("turn_cube_clock_wise_around_top")
        return state

    turns.append(turn_cube_right)

    def turn_cube_left():
        state[1] = rotate_anti_clockwise(state[1])
        state[5] = rotate_clockwise(state[5])
        state[0], state[2], state[4], state[3] = rotate_anti_clockwise(state[3]), rotate_anti_clockwise(
            state[0]), rotate_anti_clockwise(state[2]), rotate_anti_clockwise(state[4])
        print("turn_cube_anti_clock_wise_around_top")
        return state

    turns.append(turn_cube_left)
    return turns


def plus(func, turns):
    boxes = [1, 2, 3, 4]
    count = 4
    if state[1][0][1] == "r":
        count = count - 1
        boxes.remove(1)

    if state[1][-1][1] == "r":
        count = count - 1
        boxes.remove(3)

    if state[1][1][0] == "r":
        count = count - 1
        boxes.remove(4)

    if state[1][1][-1] == "r":
        count = count - 1
        boxes.remove(2)

    if count != 0:
        for i in boxes:

            if i == 2:
                pass
            elif i == 1:
                turns[0]()
            elif i == 3:
                turns[1]()
            else:
                turns[1]()
                turns[1]()

            if i:
                if state[0][1][-1] == "r":
                    func[1](0)
                elif state[5][1][-1] == "r":
                    func[0](0)
                    func[0](0)
                elif state[3][0][1] == "r":
                    func[9](0)
                    func[6](0)
                    func[8](0)
                elif state[3][1][0] == "r":
                    func[0](0)
                    func[9](0)
                    func[6](0)
                    func[8](0)
                elif state[3][1][-1] == "r":
                    func[1](0)
                    func[9](0)
                    func[6](0)
                    func[8](0)
                elif state[3][-1][1] == "r":
                    func[8](0)
                    func[5](0)
                    func[9](0)
                elif state[2][0][1] == "r":
                    func[9](0)
                    func[7](0)
                    func[8](0)
                elif state[2][1][0] == "r":
                    func[2](0)
                    func[9](0)
                    func[7](0)
                    func[8](0)
                    func[3](0)
                elif state[2][1][-1] == "r":
                    func[3](0)
                    func[9](0)
                    func[7](0)
                    func[8](0)
                    func[2](0)
                elif state[2][-1][1] == "r":
                    func[8](0)
                    func[4](0)
                    func[9](0)
                elif state[4][1][-1] == "r":
                    func[0](0)
                elif state[4][0][1] == "r":
                    func[4](0)
                    func[0](0)
                elif state[4][1][0] == "r":
                    func[4](0)
                    func[4](0)
                    func[0](0)
                    func[5](0)
                    func[5](0)
                elif state[4][-1][1] == "r":
                    func[5](0)
                    func[0](0)
                    func[4](0)
                elif state[0][0][1] == "r":
                    func[6](0)
                    func[1](0)
                    func[7](0)
                elif state[0][1][0] == "r":
                    func[6](0)
                    func[6](0)
                    func[1](0)
                    func[7](0)
                    func[7](0)
                elif state[0][-1][1] == 'r':
                    func[7](0)
                    func[1](0)
                elif state[5][0][1] == "r":
                    func[8](0)
                    func[4](0)
                    func[4](0)
                    func[9](0)
                elif state[5][1][0] == "r":
                    func[10](0)
                    func[10](0)
                    func[0](0)
                    func[0](0)
                elif state[5][-1][1] == "r":
                    func[11](0)
                    func[0](0)
                    func[0](0)
                else:
                    pass
            if i == 2:
                pass
            elif i == 1:
                turns[1]()
            elif i == 3:
                turns[0]()
            else:
                turns[1]()
                turns[1]()

            display_cube(state)

def mid_algo(func):
    func[8](0)
    func[0](0)
    func[8](0)
    func[1](0)
    func[8](0)
    func[0](0)
    func[8](0)
    func[8](0)
    func[1](0)


def mid(current_position, func, turns):
    centers = "gybwg"
    top_centers = current_position[4][0][1] + current_position[3][1][0] + current_position[0][-1][
        1] + current_position[2][1][-1] + current_position[4][0][1]
    x = 0
    des = "no"
    a = ""
    for i in range(len(top_centers) - 1):
        a = top_centers[i] + top_centers[i + 1]
        if a in centers:
            x = top_centers.index(a) - centers.index(a)
            des = "no"
            break
        else:
            x = top_centers.index("g")
            des = "yes"
    if x > 0:
        for j in range(x):
            func[8](0)
    else:
        x = abs(x)
        for j in range(x):
            func[9](0)
    top_centers = current_position[4][0][1] + current_position[3][1][0] + current_position[0][-1][
        1] + current_position[2][1][-1] + current_position[4][0][1]
    if des == "yes":
        turns[0]()
        mid_algo(func)
        func[9](0)
        turns[1]()
        mid_algo(func)
    elif top_centers == centers:
        pass
    else:
        if a[0] == "b":
            mid_algo(func)
        elif a[0] == "g":
            turns[0]()
            turns[0]()
            mid_algo(func)
            turns[1]()
            turns[1]()
        elif a[0] == "y":
            turns[1]()
            mid_algo(func)
            turns[0]()
        else:
            turns[0]()
            mid_algo(func)
            turns[1]()


def top_layer(current_position, func):
    r = "r"
    g = "g"
    w = "w"
    b = "b"
    o = "o"
    y = "y"

    R = func[0]
    Rdash = func[1]
    L = func[2]
    Ldash = func[3]
    F = func[4]
    Fdash = func[5]
    B = func[6]
    Bdash = func[7]
    U = func[8]
    Udash = func[9]
    D = func[10]
    Ddash = func[11]

    for i in range(4):
        if current_position[1][0][-1] == r:
            a_ = current_position[0][-1][-1]
            b_ = current_position[3][0][0]
            if a_ == w:
                if b_ == b:
                    Bdash(0)
                    D(0)
                    B(0)
                    D(0)
                    Ldash(0)
                    Ddash(0)
                    L(0)
            elif a_ == g:
                if b_ == w:
                    Bdash(0)
                    Ddash(0)
                    Ddash(0)
                    B(0)
                    L(0)
                    D(0)
                    Ldash(0)
            elif a_ == y:
                if b_ == g:
                    Bdash(0)
                    Ddash(0)
                    B(0)
                    F(0)
                    D(0)
                    Fdash(0)
        if current_position[1][-1][-1] == r:
            a_ = current_position[4][0][-1]
            b_ = current_position[3][-1][0]
            if a_ == b:
                if b_ == w:
                    F(0)
                    B(0)
                    Ddash(0)
                    Ddash(0)
                    Fdash(0)
                    Bdash(0)
            elif a_ == y:
                if b_ == b:
                    F(0)
                    D(0)
                    Fdash(0)
                    Bdash(0)
                    Ddash(0)
                    B(0)
            elif a_ == w:
                if b_ == g:
                    Rdash(0)
                    Ddash(0)
                    R(0)
                    L(0)
                    D(0)
                    Ldash(0)
        if current_position[1][0][0] == r:
            a_ = current_position[0][-1][0]
            b_ = current_position[2][0][-1]
            if a_ == g:
                if b_ == y:
                    Rdash(0)
                    Ldash(0)
                    D(0)
                    D(0)
                    R(0)
                    L(0)
            elif a_ == y:
                if b_ == b:
                    Ldash(0)
                    Ddash(0)
                    L(0)
                    R(0)
                    D(0)
                    Rdash(0)
            elif a_ == w:
                if b_ == g:
                    B(0)
                    D(0)
                    Bdash(0)
                    Fdash(0)
                    Ddash(0)
                    F(0)
        if current_position[1][-1][0] == r:
            a_ = current_position[2][-1][-1]
            b_ = current_position[4][0][0]
            if a_ == g:
                if b_ == y:
                    L(0)
                    D(0)
                    Ldash(0)
                    Rdash(0)
                    Ddash(0)
                    R(0)
            elif a_ == y:
                if b_ == b:
                    L(0)
                    R(0)
                    D(0)
                    D(0)
                    Rdash(0)
                    Ldash(0)
            elif a_ == b:
                if b_ == w:
                    Fdash(0)
                    Ddash(0)
                    F(0)
                    B(0)
                    D(0)
                    Bdash(0)
        if current_position[4][0][-1] == r:
            a_ = current_position[1][2][2]
            b_ = current_position[3][2][0]
            if a_ == b:
                if b_ == y:
                    F(0)
                    Bdash(0)
                    D(0)
                    Fdash(0)
                    B(0)
            elif a_ == w:
                if b_ == b:
                    F(0)
                    Ldash(0)
                    D(0)
                    D(0)
                    L(0)
                    Fdash(0)
            elif a_ == g:
                if b_ == w:
                    F(0)
                    Ddash(0)
                    Ddash(0)
                    Fdash(0)
                    Fdash(0)
                    D(0)
                    F(0)
            else:
                Rdash(0)
                D(0)
                R(0)
                Ddash(0)
                Rdash(0)
                D(0)
                R(0)
        elif current_position[4][-1][-1] == r:
            a_ = current_position[3][-1][-1]
            b_ = current_position[5][0][-1]
            if a_ == y:
                if b_ == g:
                    Ddash(0)
                    Rdash(0)
                    D(0)
                    R(0)
            elif a_ == b:
                if b_ == y:
                    Bdash(0)
                    D(0)
                    B(0)
            elif a_ == w:
                if b_ == b:
                    Ldash(0)
                    D(0)
                    D(0)
                    L(0)
            elif a_ == g:
                if b_ == w:
                    Ddash(0)
                    L(0)
                    D(0)
                    Ldash(0)
        elif current_position[5][0][-1] == r:
            a_ = current_position[4][-1][-1]
            b_ = current_position[3][-1][-1]
            if a_ == y:
                if b_ == g:
                    Rdash(0)
                    D(0)
                    D(0)
                    R(0)
                    D(0)
                    Rdash(0)
                    Ddash(0)
                    R(0)
            elif a_ == b:
                if b_ == y:
                    U(0)
                    Rdash(0)
                    D(0)
                    D(0)
                    R(0)
                    D(0)
                    Rdash(0)
                    Ddash(0)
                    R(0)
                    Udash(0)
            elif a_ == w:
                if b_ == b:
                    U(0)
                    U(0)
                    Rdash(0)
                    D(0)
                    D(0)
                    R(0)
                    D(0)
                    Rdash(0)
                    Ddash(0)
                    R(0)
                    Udash(0)
                    Udash(0)
            elif a_ == g:
                if b_ == w:
                    Udash(0)
                    Rdash(0)
                    D(0)
                    D(0)
                    R(0)
                    D(0)
                    Rdash(0)
                    Ddash(0)
                    R(0)
                    U(0)
        elif current_position[5][-1][-1] == r:
            a_ = current_position[3][0][-1]
            b_ = current_position[0][0][-1]
            if a_ == y:
                if b_ == g:
                    Ddash(0)
                    Rdash(0)
                    D(0)
                    D(0)
                    R(0)
                    D(0)
                    Rdash(0)
                    Ddash(0)
                    R(0)
            elif a_ == b:
                if b_ == y:
                    Ddash(0)
                    U(0)
                    Rdash(0)
                    D(0)
                    D(0)
                    R(0)
                    D(0)
                    Rdash(0)
                    Ddash(0)
                    R(0)
                    Udash(0)
            elif a_ == w:
                if b_ == b:
                    Ddash(0)
                    U(0)
                    U(0)
                    Rdash(0)
                    D(0)
                    D(0)
                    R(0)
                    D(0)
                    Rdash(0)
                    Ddash(0)
                    R(0)
                    Udash(0)
                    Udash(0)
            elif a_ == g:
                if b_ == w:
                    Ddash(0)
                    Udash(0)
                    Rdash(0)
                    D(0)
                    D(0)
                    R(0)
                    D(0)
                    Rdash(0)
                    Ddash(0)
                    R(0)
                    U(0)
        elif current_position[0][0][-1] == r:
            a_ = current_position[3][0][-1]
            b_ = current_position[5][-1][-1]
            if a_ == y:
                if b_ == b:
                    Bdash(0)
                    Ddash(0)
                    B(0)
            elif a_ == b:
                if b_ == w:
                    D(0)
                    Ldash(0)
                    Ddash(0)
                    L(0)
            elif a_ == w:
                if b_ == g:
                    L(0)
                    D(0)
                    D(0)
                    Ldash(0)
            else:
                Ddash(0)
                Rdash(0)
                Ddash(0)
                R(0)
        elif current_position[0][-1][-1] == r:
            a_ = current_position[1][0][-1]
            b_ = current_position[3][0][0]
            if a_ == y:
                if b_ == b:
                    Bdash(0)
                    Ddash(0)
                    B(0)
                    D(0)
                    Bdash(0)
                    Ddash(0)
                    B(0)
            elif a_ == b:
                if b_ == w:
                    Bdash(0)
                    Ddash(0)
                    B(0)
                    B(0)
                    D(0)
                    D(0)
                    Bdash(0)
            elif a_ == g:
                if b_ == y:
                    F(0)
                    Bdash(0)
                    Ddash(0)
                    Fdash(0)
                    Bdash(0)
            else:
                Bdash(0)
                L(0)
                D(0)
                D(0)
                Ldash(0)
                B(0)
        elif current_position[3][0][0] == r:
            a_ = current_position[1][0][-1]
            b_ = current_position[0][-1][-1]
            if a_ == b:
                if b_ == y:
                    Bdash(0)
                    D(0)
                    B(0)
                    Ddash(0)
                    Bdash(0)
                    D(0)
                    B(0)
            elif a_ == y:
                if b_ == g:
                    Bdash(0)
                    D(0)
                    B(0)
                    Ddash(0)
                    F(0)
                    D(0)
                    Fdash(0)
            elif a_ == g:
                if b_ == w:
                    Bdash(0)
                    D(0)
                    B(0)
                    Fdash(0)
                    Ddash(0)
                    Ddash(0)
                    F(0)
            else:
                R(0)
                Ldash(0)
                D(0)
                Rdash(0)
                L(0)
        elif current_position[3][0][-1] == r:
            a_ = current_position[0][0][-1]
            b_ = current_position[5][-1][-1]
            if a_ == b:
                if b_ == y:
                    Ddash(0)
                    Bdash(0)
                    D(0)
                    B(0)
            elif a_ == y:
                if b_ == g:
                    Ddash(0)
                    F(0)
                    D(0)
                    Fdash(0)
            elif a_ == w:
                if b_ == b:
                    Ldash(0)
                    D(0)
                    L(0)
            else:
                D(0)
                D(0)
                L(0)
                D(0)
                Ldash(0)
        elif current_position[3][-1][0] == r:
            a_ = current_position[1][-1][-1]
            b_ = current_position[4][0][-1]
            if a_ == g:
                if b_ == y:
                    Rdash(0)
                    Ddash(0)
                    R(0)
                    D(0)
                    Rdash(0)
                    Ddash(0)
                    R(0)
            elif a_ == y:
                if b_ == b:
                    Rdash(0)
                    Ddash(0)
                    R(0)
                    D(0)
                    D(0)
                    Bdash(0)
                    Ddash(0)
                    B(0)
            elif a_ == b:
                if b_ == w:
                    R(0)
                    B(0)
                    D(0)
                    D(0)
                    Bdash(0)
                    Rdash(0)
            else:
                Rdash(0)
                L(0)
                Ddash(0)
                R(0)
                Ldash(0)
        elif current_position[3][-1][-1] == r:
            a_ = current_position[4][-1][-1]
            b_ = current_position[5][0][-1]
            if a_ == g:
                if b_ == y:
                    D(0)
                    F(0)
                    Ddash(0)
                    Fdash(0)
            elif a_ == y:
                if b_ == b:
                    D(0)
                    Bdash(0)
                    Ddash(0)
                    B(0)
            elif a_ == b:
                if b_ == w:
                    B(0)
                    D(0)
                    D(0)
                    Bdash(0)
            else:
                L(0)
                Ddash(0)
                Ldash(0)
        elif current_position[4][0][0] == r:
            a_ = current_position[1][-1][0]
            b_ = current_position[2][-1][-1]
            if a_ == y:
                if b_ == b:
                    Fdash(0)
                    R(0)
                    D(0)
                    D(0)
                    Rdash(0)
                    F(0)
            elif a_ == g:
                if b_ == y:
                    Fdash(0)
                    Ddash(0)
                    F(0)
                    F(0)
                    D(0)
                    D(0)
                    Fdash(0)
            elif a_ == w:
                if b_ == g:
                    L(0)
                    Ddash(0)
                    Ldash(0)
                    D(0)
                    L(0)
                    Ddash(0)
                    Ldash(0)
            elif a_ == b:
                if b_ == w:
                    Fdash(0)
                    B(0)
                    Ddash(0)
                    F(0)
                    Bdash(0)
        elif current_position[4][-1][0] == r:
            a_ = current_position[2][-1][0]
            b_ = current_position[5][0][0]
            if a_ == y:
                if b_ == b:
                    R(0)
                    D(0)
                    D(0)
                    Rdash(0)
            elif a_ == g:
                if b_ == y:
                    D(0)
                    Rdash(0)
                    Ddash(0)
                    R(0)
            elif a_ == w:
                if b_ == g:
                    D(0)
                    L(0)
                    Ddash(0)
                    Ldash(0)
            else:
                B(0)
                Ddash(0)
                Bdash(0)
        elif current_position[5][0][0] == r:
            a_ = current_position[4][-1][0]
            b_ = current_position[2][-1][0]
            if a_ == y:
                if b_ == b:
                    R(0)
                    D(0)
                    D(0)
                    Rdash(0)
                    Bdash(0)
                    Ddash(0)
                    B(0)
                    D(0)
                    Bdash(0)
                    Ddash(0)
                    B(0)
            elif a_ == g:
                if b_ == y:
                    Rdash(0)
                    D(0)
                    R(0)
                    F(0)
                    D(0)
                    Fdash(0)
                    Ddash(0)
                    F(0)
                    D(0)
                    Fdash(0)
            elif a_ == w:
                if b_ == g:
                    L(0)
                    D(0)
                    D(0)
                    Ldash(0)
                    Ddash(0)
                    L(0)
                    D(0)
                    Ldash(0)
            else:
                Ddash(0)
                B(0)
                D(0)
                D(0)
                Bdash(0)
                Ddash(0)
                B(0)
                D(0)
                Bdash(0)
        elif current_position[5][-1][0] == r:
            a_ = current_position[2][0][0]
            b_ = current_position[0][0][0]
            if a_ == y:
                if b_ == b:
                    Ddash(0)
                    Bdash(0)
                    Ddash(0)
                    Ddash(0)
                    B(0)
                    D(0)
                    Bdash(0)
                    Ddash(0)
                    B(0)
            elif a_ == g:
                if b_ == y:
                    D(0)
                    D(0)
                    Rdash(0)
                    D(0)
                    D(0)
                    R(0)
                    D(0)
                    Rdash(0)
                    Ddash(0)
                    R(0)
            elif a_ == w:
                if b_ == g:
                    D(0)
                    L(0)
                    D(0)
                    D(0)
                    Ldash(0)
                    Ddash(0)
                    L(0)
                    D(0)
                    Ldash(0)
            else:
                B(0)
                Ddash(0)
                Ddash(0)
                Bdash(0)
                Ddash(0)
                B(0)
                D(0)
                Bdash(0)
        elif current_position[0][0][0] == r:
            a_ = current_position[2][0][0]
            if a_ == b:
                Ddash(0)
                R(0)
                D(0)
                Rdash(0)
            elif a_ == y:
                Rdash(0)
                D(0)
                D(0)
                R(0)
            elif a_ == g:
                Fdash(0)
                D(0)
                F(0)
            else:
                Ddash(0)
                Ldash(0)
                D(0)
                L(0)
        elif current_position[0][-1][0] == r:
            a_ = current_position[1][0][0]
            if a_ == w:
                B(0)
                D(0)
                Bdash(0)
                Ddash(0)
                B(0)
                D(0)
                Bdash(0)
            elif a_ == b:
                B(0)
                D(0)
                Bdash(0)
                Bdash(0)
                D(0)
                D(0)
                B(0)
            elif a_ == y:
                B(0)
                Rdash(0)
                D(0)
                D(0)
                R(0)
                Bdash(0)
            else:
                B(0)
                Fdash(0)
                D(0)
                Bdash(0)
                F(0)
        elif current_position[2][0][0] == r:
            a_ = current_position[0][0][0]
            if a_ == y:
                R(0)
                Ddash(0)
                Rdash(0)
            elif a_ == g:
                F(0)
                D(0)
                D(0)
                Fdash(0)
            elif a_ == w:
                D(0)
                Fdash(0)
                Ddash(0)
                F(0)
            else:
                D(0)
                B(0)
                Ddash(0)
                Bdash(0)
        elif current_position[2][0][-1] == r:
            a_ = current_position[1][0][0]
            if a_ == y:
                R(0)
                Ldash(0)
                Ddash(0)
                Rdash(0)
                L(0)
            elif a_ == g:
                Ldash(0)
                F(0)
                D(0)
                D(0)
                Fdash(0)
                L(0)
            elif a_ == w:
                Ldash(0)
                Ddash(0)
                L(0)
                L(0)
                D(0)
                D(0)
                Ldash(0)
            else:
                Ldash(0)
                Ddash(0)
                L(0)
                D(0)
                Ldash(0)
                Ddash(0)
                L(0)
        elif current_position[2][-1][0] == r:
            a_ = current_position[4][-1][0]
            if a_ == b:
                Bdash(0)
                D(0)
                D(0)
                B(0)
            elif a_ == y:
                Rdash(0)
                D(0)
                R(0)
            elif a_ == g:
                Ddash(0)
                Fdash(0)
                D(0)
                F(0)
            else:
                D(0)
                Ldash(0)
                Ddash(0)
                Ddash(0)
                L(0)
        elif current_position[2][-1][-1] == r:
            a_ = current_position[1][-1][0]
            if a_ == b:
                L(0)
                Bdash(0)
                D(0)
                D(0)
                B(0)
                Ldash(0)
            elif a_ == y:
                L(0)
                Rdash(0)
                D(0)
                R(0)
                Ldash(0)
            elif a_ == g:
                L(0)
                D(0)
                Ldash(0)
                Ddash(0)
                L(0)
                D(0)
                Ldash(0)
            else:
                L(0)
                D(0)
                Ldash(0)
                Ldash(0)
                D(0)
                D(0)
                L(0)
        display_cube(state)

def second_algo(func, turns):
    func[11](0)
    func[1](0)
    func[10](0)
    func[0](0)
    turns[0]()
    func[10](0)
    func[2](0)
    func[11](0)
    func[3](0)
    turns[1]()


def second_reverse_algo(func, turns):
    func[10](0)
    func[2](0)
    func[11](0)
    func[3](0)
    turns[1]()
    func[11](0)
    func[1](0)
    func[10](0)
    func[0](0)
    turns[0]()


def second_layer(current_position, func, turns):
    b = "b"
    g = "g"
    w = "w"
    y = "y"
    o = "o"

    D = func[10]
    Ddash = func[11]

    while current_position[4][1][0] != g or current_position[4][1][-1] != g or current_position[3][0][
        1] != y or current_position[3][-1][1] != y or current_position[2][0][1] != w or \
            current_position[2][-1][1] != w or current_position[0][1][0] != b or \
            current_position[0][1][-1] != b:

        i = 1
        while i < 5:
            middle_pieces = {1: [current_position[4][-1][1], current_position[5][0][1]],
                             2: [current_position[3][1][-1], current_position[5][1][-1]],
                             3: [current_position[0][0][1], current_position[5][-1][1]],
                             4: [current_position[2][1][0], current_position[5][1][0]]}
            if middle_pieces[i][1] == o or middle_pieces[i][0] == o:
                dummy_mids = [current_position[4][-1][1], current_position[5][0][1], current_position[3][1][-1],
                              current_position[5][1][-1], current_position[0][0][1], current_position[5][-1][1],
                              current_position[2][1][0], current_position[5][1][0]]
                x = dummy_mids.count("o")

                if x == 4:
                    if current_position[4][1][0] != g or current_position[2][-1][1] != w:
                        second_reverse_algo(func, turns)
                        display_cube(state)
                    elif current_position[4][1][-1] != g or current_position[3][-1][1] != y:
                        second_algo(func, turns)
                        display_cube(state)
                    elif current_position[0][1][0] != b or current_position[2][0][1] != w:
                        turns[0]()
                        turns[0]()
                        second_algo(func, turns)
                        turns[1]()
                        turns[1]()
                    elif current_position[0][1][-1] != b or current_position[3][0][1] != y:
                        turns[0]()
                        turns[0]()
                        second_reverse_algo(func, turns)
                        turns[1]()
                        turns[1]()
                i = i + 1

            else:
                if middle_pieces[i][0] == g:
                    if i == 2:
                        Ddash(0)
                    elif i == 3:
                        D(0)
                        D(0)
                    elif i == 4:
                        D(0)
                    if middle_pieces[i][1] == y:
                        second_algo(func, turns)
                    elif middle_pieces[i][1] == w:
                        second_reverse_algo(func, turns)

                elif middle_pieces[i][0] == y:
                    if i == 1:
                        D(0)
                    elif i == 3:
                        Ddash(0)
                    elif i == 4:
                        D(0)
                        D(0)
                    turns[0]()
                    if middle_pieces[i][1] == b:
                        second_algo(func, turns)
                    elif middle_pieces[i][1] == g:
                        second_reverse_algo(func, turns)
                    turns[1]()

                elif middle_pieces[i][0] == b:
                    if i == 1:
                        D(0)
                        D(0)
                    elif i == 2:
                        D(0)
                    elif i == 4:
                        Ddash(0)
                    turns[0]()
                    turns[0]()
                    if middle_pieces[i][1] == w:
                        second_algo(func, turns)
                    elif middle_pieces[i][1] == y:
                        second_reverse_algo(func, turns)
                    turns[1]()
                    turns[1]()

                elif middle_pieces[i][0] == w:
                    if i == 1:
                        Ddash(0)
                    elif i == 2:
                        Ddash(0)
                        Ddash(0)
                    elif i == 3:
                        D(0)
                    turns[1]()
                    if middle_pieces[i][1] == g:
                        second_algo(func, turns)
                    elif middle_pieces[i][1] == b:
                        second_reverse_algo(func, turns)
                    turns[0]()
            display_cube(state)


def bottom_plus_algo(func):
    func[4](0)
    func[0](0)
    func[8](0)
    func[1](0)
    func[9](0)
    func[5](0)


def bottom_plus(current_position, func, flips, turns):
    flips[0]()
    flips[0]()
    dummy_mids = [current_position[1][0][1], current_position[1][1][0], current_position[1][1][1],
                  current_position[1][1][-1], current_position[1][-1][1]]
    x = dummy_mids.count("o")
    display_cube(state)
    while x != 5:
        if x == 1:
            bottom_plus_algo(func)
        else:
            if current_position[1][0][1] == "o" and current_position[1][1][-1] == "o":
                turns[1]()
                bottom_plus_algo(func)
                turns[0]()
            elif current_position[1][0][1] == "o" and current_position[1][-1][1] == "o":
                turns[1]()
                bottom_plus_algo(func)
                turns[0]()
            elif current_position[1][1][-1] == "o" and current_position[1][-1][1] == "o":
                turns[1]()
                turns[1]()
                bottom_plus_algo(func)
                turns[0]()
                turns[0]()
            elif current_position[1][-1][1] == "o" and current_position[1][1][0] == "o":
                turns[0]()
                bottom_plus_algo(func)
                turns[1]()
            else:
                bottom_plus_algo(func)

        dummy_mids = [current_position[1][0][1], current_position[1][1][0], current_position[1][1][1],
                      current_position[1][1][-1], current_position[1][-1][1]]
        x = dummy_mids.count("o")
        display_cube(state)


state, N = splitter(solved_state(random.randint(3, 20)))
x = moves_generator(N)
y = flips_generator()
z = turn_generator()
scrambler(N)
print(state)
center_piece_solver()
display_cube(state)
edge_solver(x)
display_cube(state)
plus(x, z)
display_cube(state)
mid(state, x, z)
display_cube(state)
top_layer(state, x)
display_cube(state)
print(time.time() - time1)
