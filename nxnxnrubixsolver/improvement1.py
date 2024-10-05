import random

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
            print(condition)
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

        elif i + j == N - 1 and c == 2:
            pass


def test_string_generator(n):
    string = (6 * n * n) * ["w"]
    string[int(n / 2) * n + int(n / 2)] = "w"
    string[n * n + int(n / 2) * n + int(n / 2)] = "r"
    string[0:n * n] = (n * n) * ["r"]
    string[int(n / 2) * n + int(n / 2)] = "w"
    return string


state, N = splitter(test_string_generator(24))
x = moves_generator(N)
display_cube(state)
print(NUMBER_OF_MOVES)

for i in range(1, N - 1):
    for j in range(1, N - 1):
        center_piece_arranger((i, j), (0, j, N - 1 - i), "r", x)
        display_cube(state)

print(NUMBER_OF_MOVES)
