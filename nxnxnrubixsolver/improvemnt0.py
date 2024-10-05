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

    for k in range(12):
        functions.append([])

    # if n % 2 == 0:
    #    no_of_moves = int(n / 2)
    # else:
    #    no_of_moves = int(n / 2) + 1
    no_of_moves = n - 1

    for value in range(no_of_moves):
        def r_move(i=value):
            global NUMBER_OF_MOVES
            NUMBER_OF_MOVES += 1
            if i == 0:
                temp = state[3]
                state[3] = rotate_clockwise(temp)
            for j in range(n):
                state[0][j][n - i - 1], state[5][j][n - i - 1] = state[5][j][n - i - 1], state[0][j][n - i - 1]
                state[1][j][n - i - 1], state[4][j][n - i - 1] = state[4][j][n - i - 1], state[1][j][n - i - 1]
                state[4][j][n - i - 1], state[0][j][n - i - 1] = state[0][j][n - i - 1], state[4][j][n - i - 1]
            return state

        functions[0].append(r_move)

    for value in range(no_of_moves):
        def r_dash_move(i=value):
            global NUMBER_OF_MOVES
            NUMBER_OF_MOVES += 1
            if i == 0:
                temp = state[3]
                state[3] = rotate_anti_clockwise(temp)
            for j in range(n):
                state[0][j][n - i - 1], state[5][j][n - i - 1] = state[5][j][n - i - 1], state[0][j][n - i - 1]
                state[1][j][n - i - 1], state[4][j][n - i - 1] = state[4][j][n - i - 1], state[1][j][n - i - 1]
                state[1][j][n - i - 1], state[5][j][n - i - 1] = state[5][j][n - i - 1], state[1][j][n - i - 1]
            return state

        functions[1].append(r_dash_move)

    for value in range(no_of_moves):
        def l_move(i=value):
            global NUMBER_OF_MOVES
            NUMBER_OF_MOVES += 1
            if i == 0:
                temp = state[2]
                state[2] = rotate_clockwise(temp)
            for j in range(n):
                state[0][j][i], state[5][j][i] = state[5][j][i], state[0][j][i]
                state[1][j][i], state[4][j][i] = state[4][j][i], state[1][j][i]
                state[1][j][i], state[5][j][i] = state[5][j][i], state[1][j][i]

            return state

        functions[2].append(l_move)

    for value in range(no_of_moves):
        def l_dash_move(i=value):
            global NUMBER_OF_MOVES
            NUMBER_OF_MOVES += 1
            if i == 0:
                temp = state[2]
                state[2] = rotate_anti_clockwise(temp)
            for j in range(n):
                state[0][j][i], state[5][j][i] = state[5][j][i], state[0][j][i]
                state[1][j][i], state[4][j][i] = state[4][j][i], state[1][j][i]
                state[4][j][i], state[0][j][i] = state[0][j][i], state[4][j][i]

            return state

        functions[3].append(l_dash_move)

    for value in range(no_of_moves):
        def f_move(i=value):
            global NUMBER_OF_MOVES
            NUMBER_OF_MOVES += 1
            if i == 0:
                temp = state[4]
                state[4] = rotate_clockwise(temp)
            for j in range(n):
                state[2][n - i - 1][j], state[5][i][n - j - 1] = state[5][i][n - j - 1], state[2][n - i - 1][j]
                state[1][n - i - 1][j], state[3][n - i - 1][j] = state[3][n - i - 1][j], state[1][n - i - 1][j]
                state[1][n - i - 1][j], state[5][i][n - j - 1] = state[5][i][n - j - 1], state[1][n - i - 1][j]

            return state

        functions[4].append(f_move)

    for value in range(no_of_moves):
        def f_dash_move(i=value):
            global NUMBER_OF_MOVES
            NUMBER_OF_MOVES += 1
            if i == 0:
                temp = state[4]
                state[4] = rotate_anti_clockwise(temp)
            for j in range(n):
                state[2][n - i - 1][j], state[5][i][n - j - 1] = state[5][i][n - j - 1], state[2][n - i - 1][j]
                state[1][n - i - 1][j], state[3][n - i - 1][j] = state[3][n - i - 1][j], state[1][n - i - 1][j]
                state[2][n - i - 1][j], state[3][n - i - 1][j] = state[3][n - i - 1][j], state[2][n - i - 1][j]
            return state

        functions[5].append(f_dash_move)

    for value in range(no_of_moves):
        def b_move(i=value):
            global NUMBER_OF_MOVES
            NUMBER_OF_MOVES += 1
            if i == 0:
                temp = state[0]
                state[0] = rotate_clockwise(temp)
            for j in range(n):
                state[2][i][j], state[5][n - i - 1][n - j - 1] = state[5][n - i - 1][n - j - 1], state[2][i][j]
                state[1][i][j], state[3][i][j] = state[3][i][j], state[1][i][j]
                state[2][i][j], state[3][i][j] = state[3][i][j], state[2][i][j]

            return state

        functions[6].append(b_move)

    for value in range(no_of_moves):
        def b_dash_move(i=value):
            global NUMBER_OF_MOVES
            NUMBER_OF_MOVES += 1
            if i == 0:
                temp = state[0]
                state[0] = rotate_anti_clockwise(temp)
            for j in range(n):
                state[2][i][j], state[5][n - i - 1][n - j - 1] = state[5][n - i - 1][n - j - 1], state[2][i][j]
                state[1][i][j], state[3][i][j] = state[3][i][j], state[1][i][j]
                state[1][i][j], state[5][n - i - 1][n - j - 1] = state[5][n - i - 1][n - j - 1], state[1][i][j]
            return state

        functions[7].append(b_dash_move)

    for value in range(no_of_moves):
        def u_move(i=value):
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
            return state

        functions[8].append(u_move)

    for value in range(no_of_moves):
        def u_dash_move(i=value):
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
            return state

        functions[9].append(u_dash_move)

    for value in range(no_of_moves):
        def d_move(i=value):
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
            return state

        functions[10].append(d_move)

    for value in range(no_of_moves):
        def d_dash_move(i=value):
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
            return state

        functions[11].append(d_dash_move)

    return functions


def center_piece_arranger(target, position, color, func):
    i = target[0]
    j = target[1]
    a = position[1]
    b = position[2]
    c = position[0]
    if state[1][i][j] != color:
        if i + j == N - 1 and c == 0:
            while a != i and b != i:
                func[6][0]()
            func[0][j]()
            func[6][0]()
            func[3][j]()
            func[7][0]()
            func[1][j]()
            func[6][0]()
            func[2][j]()
            func[7][0]()

        elif i + j != N - 1 and c == 0:
            while a != j and b != N - 1 - i:
                func[6][0]()
            func[0][i]()
            func[7][0]()
            func[3][j]()
            func[6][0]()
            func[1][i]()
            func[7][0]()
            func[2][j]()
            func[6][0]()

        elif i + j == N - 1 and c == 2:
            pass


state, N = splitter(solved_state(7))
print("hello")
x = moves_generator(N)

x[11][0]()
x[1][1]()
display_cube(state)
print(NUMBER_OF_MOVES)
