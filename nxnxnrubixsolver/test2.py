"""
solver.py is a module in python which theoretically can solve a rubix cube of any size.
"""

import random

# Constants to store the colors of the cube as strings of the starting letter
BLUE = "b"
RED = "r"
WHITE = "w"
YELLOW = "y"
GREEN = "g"
ORANGE = "o"

NUMBER_OF_MOVES = 0  # To keep track of number of moves


class CustomException(Exception):
    """
    Custom exception to be raised when an invalid state is passed.
    """
    pass


def rotate_clockwise(lst: list) -> list:
    """
    Rotates the given face of the cube clockwise.

    :param lst: Face of the cube to be rotated clockwise.
    :return: Clockwise rotated face as a list.
    """

    rotated_face = []  # Initialize an empty list for the rotated face
    n = len(lst)  # Determine the size of the cube face

    # Traverse through the elements of the cube face
    for i in range(n):
        temp = []  # Temporary list to store rotated elements of each row
        for j in range(n):
            temp = list(lst[j][i]) + temp  # Append elements in reverse order
        rotated_face.append(temp)  # Append rotated row to the result

    return rotated_face


def rotate_anti_clockwise(lst: list) -> list:
    """
    Rotates the given face of the cube counterclockwise

    :param lst: Face of the cube to be rotated counterclockwise.
    :return: Counterclockwise rotated face as a list
    """
    rotated_face = []  # Initialize an empty list for the rotated face
    n = len(lst)  # Determine the size of the cube face

    # Traverse through the elements of the cube face
    for i in range(n - 1, -1, -1):
        temp = []  # Temporary list to store rotated elements of each row
        for j in range(n):
            temp = temp + list(lst[j][i])  # Append elements in the order
        rotated_face.append(temp)  # Append rotated row to the result
    return rotated_face


def splitter(string: str) -> (list[list[list]], int):
    """
    splits the initial state of the cube to a list which initially in the form of a string for easier manipulations.

    :param string: Initial state of the cube.
    :return: A list representing initial state.
    """
    state_ = [[], [], [], [], [], []]  # Initialize a list of 6 empty lists to store the values of 6 faces.
    a = len(string)  # Determine the size of the string.
    b = (a / 6) ** (1 / 2)  # Determining the size of the cube.

    # Raise custom exception when the size of initial state is invalid.
    try:
        if b % 1 != 0:  # Raise the exception when the size of cube has decimal values.
            raise CustomException
        else:
            b = int(b)  # casting b from float to int.
    except CustomException:
        print("You have entered an invalid input please check")  # Printing the exception.
        return 0

    # A nested for loop to traverse the state and fill the initialized state_ list
    for i in range(6):  # i runs 6 times as cube has 6 faces.
        for j in range(b):  # j runs size of cube times.
            row = string[i * b * b + j * b: i * b * b + j * b + b]  # row is a string of size b, is a row of the face.
            row = list(row)  # cast row into list
            state_[i].append(row)  # appending row to the state into i th list i.e, i th face.
    return state_, b


def display_cube(current_state: list[list[list]]) -> None:
    """
    This function displays the current state of the cube.

    :param current_state: A list that represents current state.
    :return: Null
    """

    # A dictionary to map colors with the symbols used. These symbols are copied pasted from WhatsApp.
    color_index = {"r": "🟥", "g": "🟩", "w": "⬜", "b": "🟦", "y": "🟨", "o": "🟧", " ": " "}
    n = len(current_state[0])
    for i in range(n):
        print(" " * (2 * n + 2), end="")
        for j in current_state[0][i]:
            print(color_index[j], end="")
        print()
    print()
    for i in range(n):
        for j in current_state[2][i] + [" "] + current_state[1][i] + [" "] + current_state[3][i]:
            print(color_index[j], end="")
        print()
    print()
    for i in range(n):
        print(" " * (2 * n + 2), end="")
        for j in current_state[4][i]:
            print(color_index[j], end="")
        print()
    print()
    for i in range(n):
        print(" " * (2 * n + 2), end="")
        for j in current_state[5][i]:
            print(color_index[j], end="")
        print()
    print()


def moves_generator(n: int) -> list:
    """
    Generates all the possible moves which are used to manipulate the cube in correct way.

    :param n: n is the size of the cube.
    :return: A list of various functions that can manipulate the cube accurately.
    """
    functions = []  # Initializing a function to the lists of functions.

    def r_move(i: int) -> None:
        """
        Rotates the i th column from right face of the cube clockwise.

        :param i: Passing i to the function performs R move on i th column[from right side].
        :return: returns nothing
        """
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1  # Incrementing the number of moves by 1.

        # Rotating the right face of the cube when i=0 is passed.
        if i == 0:
            temp = state[3]
            state[3] = rotate_clockwise(temp)  # Replacing current right face with clockwise rotated right face.

        # Changing the i th columns of top, front, bottom and back faces appropriately.
        for j in range(n):
            state[0][j][n - i - 1], state[5][j][n - i - 1] = state[5][j][n - i - 1], state[0][j][n - i - 1]
            state[1][j][n - i - 1], state[4][j][n - i - 1] = state[4][j][n - i - 1], state[1][j][n - i - 1]
            state[4][j][n - i - 1], state[0][j][n - i - 1] = state[0][j][n - i - 1], state[4][j][n - i - 1]
        print(f"R{i}")

    functions.append(r_move)  # Appending R move to the functions list.

    def r_dash_move(i: int) -> None:
        """
        Rotates i th column from the right face of the cube counterclockwise.

        :param i: Passing i to the function performs R dash move on i th column[from right side].
        :return: returns nothing
        """
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1  # Incrementing the number of moves by 1.

        # Rotating the right face of the cube when i=0 is passed.
        if i == 0:
            temp = state[3]
            state[3] = rotate_anti_clockwise(temp)  # Replacing current right face with counterclockwise rotated face.

        # Changing the i th columns of top, front, bottom and back faces appropriately.
        for j in range(n):
            state[0][j][n - i - 1], state[5][j][n - i - 1] = state[5][j][n - i - 1], state[0][j][n - i - 1]
            state[1][j][n - i - 1], state[4][j][n - i - 1] = state[4][j][n - i - 1], state[1][j][n - i - 1]
            state[1][j][n - i - 1], state[5][j][n - i - 1] = state[5][j][n - i - 1], state[1][j][n - i - 1]
        print(f"R dash{i}")

    functions.append(r_dash_move)  # Appending R dash move to the functions list.

    def l_move(i: int) -> None:
        """
        Rotates i th column from left face of the cube clockwise.

        :param i: Passing i to the function performs l move on the i th column from left.
        :return: returns nothing
        """
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1  # Incrementing the number of moves by 1.

        # Rotating the left face of the cube clockwise when i = 0 is passed.
        if i == 0:
            temp = state[2]
            state[2] = rotate_clockwise(temp)  # Replacing current left face with clockwise rotated left face.

        # Changing the i th columns of top, front, bottom and back faces appropriately.
        for j in range(n):
            state[0][j][i], state[5][j][i] = state[5][j][i], state[0][j][i]
            state[1][j][i], state[4][j][i] = state[4][j][i], state[1][j][i]
            state[1][j][i], state[5][j][i] = state[5][j][i], state[1][j][i]
        print(f"L{i}")

    functions.append(l_move)  # Appending L move to the functions list.

    def l_dash_move(i: int) -> None:
        """
        Rotates the i th column from left face of the cube counterclockwise.

        :param i: Performs L dash move on i th column from left face of the cube.
        :return: Returns nothing.
        """
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1  # Incrementing Number of moves by 1.

        # Rotating left face of the cube counterclockwise when i = 0 is passed
        if i == 0:
            temp = state[2]
            state[2] = rotate_anti_clockwise(temp)  # Replacing the current left face with rotated left face.

        # Changing i th column from left face appropriately.
        for j in range(n):
            state[0][j][i], state[5][j][i] = state[5][j][i], state[0][j][i]
            state[1][j][i], state[4][j][i] = state[4][j][i], state[1][j][i]
            state[4][j][i], state[0][j][i] = state[0][j][i], state[4][j][i]
        print(f"L dash{i}")

    functions.append(l_dash_move)  # Appending L dash move to the functions list.

    def f_move(i: int) -> None:
        """
        Rotates i th row from front face of the cube clockwise.

        :param i: Performs F move on i th row from the front face of the cube.
        :return: returns nothing
        """
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1  # Increment the number of moves by 1.

        # Rotate the front face of the cube clockwise when i = 0 is passed.
        if i == 0:
            temp = state[4]
            state[4] = rotate_clockwise(temp)  # Replacing the current front face with the rotated front face.

        # Changing i th row from front face of the cube appropriately.
        for j in range(n):
            state[2][n - i - 1][j], state[5][i][n - j - 1] = state[5][i][n - j - 1], state[2][n - i - 1][j]
            state[1][n - i - 1][j], state[3][n - i - 1][j] = state[3][n - i - 1][j], state[1][n - i - 1][j]
            state[1][n - i - 1][j], state[5][i][n - j - 1] = state[5][i][n - j - 1], state[1][n - i - 1][j]
        print(f"F{i}")

    functions.append(f_move)  # Appending F move to the functions.

    def f_dash_move(i: int) -> None:
        """
        Rotates i th row from the front face of the cube counterclockwise.

        :param i: Performs F dash move on i th row from the front face of the cube.
        :return: returns nothing.
        """
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1  # Increment Number of moves by 1.

        # Rotating the front face of the cube counterclockwise when i = 0 is passed.
        if i == 0:
            temp = state[4]
            state[4] = rotate_anti_clockwise(temp)  # Replacing the current front face with rotated front face.

        # Changing i th row from front face of the cube appropriately.
        for j in range(n):
            state[2][n - i - 1][j], state[5][i][n - j - 1] = state[5][i][n - j - 1], state[2][n - i - 1][j]
            state[1][n - i - 1][j], state[3][n - i - 1][j] = state[3][n - i - 1][j], state[1][n - i - 1][j]
            state[2][n - i - 1][j], state[3][n - i - 1][j] = state[3][n - i - 1][j], state[2][n - i - 1][j]
        print(f"F dash{i}")

    functions.append(f_dash_move)  # Appending F dash move to the functions.

    def b_move(i: int) -> None:
        """
        Rotates i th row from the back face of the cube clockwise.

        :param i: Performs B move on the on i th row from the back face of the cube.
        :return: Returns nothing.
        """
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1  # Incrementing the number of moves by 1.

        # Rotating the back face of the cube clockwise when i = 0 is passed.
        if i == 0:
            temp = state[0]
            state[0] = rotate_clockwise(temp)  # Replacing the current back face with the rotated back face.

        # changing the i th row from the back face of the cube appropriately.
        for j in range(n):
            state[2][i][j], state[5][n - i - 1][n - j - 1] = state[5][n - i - 1][n - j - 1], state[2][i][j]
            state[1][i][j], state[3][i][j] = state[3][i][j], state[1][i][j]
            state[2][i][j], state[3][i][j] = state[3][i][j], state[2][i][j]
        print(f"B{i}")

    functions.append(b_move)  # Appending B move to the functions.

    def b_dash_move(i: int) -> None:
        """
        Rotate i th row from back face of the cube counterclockwise.
        :param i: Perfoms B dash move on i th row from the back face of the cube.
        :return: Returns nothing.
        """
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1  # Incrementing the number of moves by 1.

        # Rotating the back face of the cube counterclockwise when i = 0 is passed.
        if i == 0:
            temp = state[0]
            state[0] = rotate_anti_clockwise(temp)  # Replacing the current back face with the rotated back face.

        # Changing i th row from the back face of the cube appropriately.
        for j in range(n):
            state[2][i][j], state[5][n - i - 1][n - j - 1] = state[5][n - i - 1][n - j - 1], state[2][i][j]
            state[1][i][j], state[3][i][j] = state[3][i][j], state[1][i][j]
            state[1][i][j], state[5][n - i - 1][n - j - 1] = state[5][n - i - 1][n - j - 1], state[1][i][j]
        print(f"B dash{i}")

    functions.append(b_dash_move)  # Appending B dash move to the functions.

    def u_move(i: int) -> None:
        """
        Rotates i th row from the top face of the cube clockwise.

        :param i: Performs U move on the i th row from the top face of the cube.
        :return: Returns nothing.
        """
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1  # Incrementing the Number of moves by 1.

        # Rotating the top face of the cube clockwise when i = 0 is passed.
        if i == 0:
            temp = state[1]
            state[1] = rotate_clockwise(temp)

        # Changing the values of i th row from the top face accurately.
        for j in range(n):
            state[0][n - i - 1][j], state[3][j][i] = state[3][j][i], state[0][n - i - 1][j]
            state[4][i][j], state[2][j][n - i - 1] = state[2][j][n - i - 1], state[4][i][j]
            state[0][n - i - 1][j], state[4][i][j] = state[4][i][j], state[0][n - i - 1][j]
        state[4][i].reverse()
        state[0][n - i - 1].reverse()
        print(f"U{i}")

    functions.append(u_move)  # Appending U move to the functions.

    def u_dash_move(i: int) -> None:
        """
        Rotates i th row from the top face of the cube counterclockwise.

        :param i: Performs U dash move on the i th row from the top face of the cube.
        :return: Returns nothing.
        """
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1  # Incrementing Number of moves by 1.

        # Rotate the top face of the cube counterclockwise when i = 0 is passed.
        if i == 0:
            temp = state[1]
            state[1] = rotate_anti_clockwise(temp)  # Replacing the current top face of the cube with rotated one.

        # Change the i th row from the top face of the cube appropriately.
        for j in range(n):
            state[0][n - i - 1][j], state[3][j][i] = state[3][j][i], state[0][n - i - 1][j]
            state[4][i][j], state[2][j][n - i - 1] = state[2][j][n - i - 1], state[4][i][j]
            state[2][j][n - i - 1], state[3][j][i] = state[3][j][i], state[2][j][n - i - 1]
        for j in range(int(n / 2)):
            state[2][j][n - i - 1], state[2][n - j - 1][n - i - 1] = state[2][n - j - 1][n - i - 1], state[2][j][
                n - i - 1]
            state[3][j][i], state[3][n - j - 1][i] = state[3][n - j - 1][i], state[3][j][i]
        print(f"U dash{i}")

    functions.append(u_dash_move)  # Appending U dash move to the functions.

    def d_move(i: int) -> None:
        """
        Rotates the i th row from the bottom face of the cube clockwise.

        :param i: Performs D move on i th row from the bottom face of the cube.
        :return: Returns nothing.
        """
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1  # Incrementing Number of moves by 1.

        # Rotate the bottom face of the cube clockwise when i = 0 is passed.
        if i == 0:
            temp = state[5]
            state[5] = rotate_clockwise(temp)  # Replacing the current bottom face with the rotated bottom face.

        # Change the values of i th row from the bottom of the cube appropriately.
        for j in range(n):
            state[0][i][j], state[3][j][n - i - 1] = state[3][j][n - i - 1], state[0][i][j]
            state[4][n - i - 1][j], state[2][j][i] = state[2][j][i], state[4][n - i - 1][j]
            state[2][j][i], state[3][j][n - i - 1] = state[3][j][n - i - 1], state[2][j][i]
        for j in range(int(n / 2)):
            state[2][j][i], state[2][n - j - 1][i] = state[2][n - j - 1][i], state[2][j][i]
            state[3][j][n - i - 1], state[3][n - j - 1][n - i - 1] = state[3][n - j - 1][n - i - 1], state[3][j][
                n - i - 1]
        print(f"D{i}")

    functions.append(d_move)  # Appending D move to the functions.

    def d_dash_move(i: int) -> None:
        """
        Rotates the i th row from the bottom face of the cube counterclockwise.

        :param i: Performs D dash move on the i th row from the bottom face of the cube.
        :return: Returns nothing.
        """
        global NUMBER_OF_MOVES
        NUMBER_OF_MOVES += 1  # Increment the Number of moves by `1.

        # Rotate the bottom face of the cube counterclockwise when i = 0 is passed.
        if i == 0:
            temp = state[5]
            state[5] = rotate_anti_clockwise(temp)  # Replace the current bottom face of the cube with rotated one.

        # Change the values of the i th row from the bottom face of the cube appropriately.
        for j in range(n):
            state[0][i][j], state[3][j][n - i - 1] = state[3][j][n - i - 1], state[0][i][j]
            state[4][n - i - 1][j], state[2][j][i] = state[2][j][i], state[4][n - i - 1][j]
            state[0][i][j], state[4][n - i - 1][j] = state[4][n - i - 1][j], state[0][i][j]
        for j in range(int(n / 2)):
            state[0][i][j], state[0][i][n - j - 1] = state[0][i][n - j - 1], state[0][i][j]
        state[4][n - i - 1].reverse()
        print(f"Ddash{i}")

    functions.append(d_dash_move)  # Appending D dash move to the functions.
    return functions


def flips_generator() -> list:
    """
    Generates the flips that can manipulate the cube appropriately.

    :return:  Returns a list of flips that can manipulate the cube.
    """
    flips = []  # Initializing an empty list to store the flip functions.

    def flip_top_to_front() -> None:
        """
        Flips the top of the cube to the front i.e, the top face becomes front face.
        :return: Returns nothing.
        """
        state[3] = rotate_anti_clockwise(state[3])  # Rotating right face counterclockwise.
        state[2] = rotate_clockwise(state[2])  # Rotating left face clockwise.

        # Changing the remaining faces appropriately.
        state[0], state[1] = state[1], state[0]
        state[5], state[4] = state[4], state[5]
        state[0], state[4] = state[4], state[0]
        print("flip top to front")

    flips.append(flip_top_to_front)  # Appending the above function to the flips.

    def flip_top_to_back() -> None:
        """
        Flips the top face of the cube to the back i.e, the top face becomes back face.
        :return: Returns nothing.
        """
        state[3] = rotate_clockwise(state[3])  # Rotate right face clockwise.
        state[2] = rotate_anti_clockwise(state[2])  # Rotate left face counterclockwise.

        # Changing the remaining faces appropriately.
        state[0], state[1] = state[1], state[0]
        state[5], state[4] = state[4], state[5]
        state[1], state[5] = state[5], state[1]
        print("flip top to back")

    flips.append(flip_top_to_back)  # Appending the above function to flips.

    def flip_top_to_right() -> None:
        """
        Flips the top face of the cube to the right i.e, top face becomes right face.
        :return: Returns nothing.
        """
        state[0] = rotate_anti_clockwise(state[0])  # Rotate the back face counterclockwise.
        state[4] = rotate_clockwise(state[4])  # Rotate the front face clockwise.

        # Changing the remaining faces appropriately.
        state[2], state[1] = state[1], state[2]
        state[5], state[3] = rotate_clockwise(rotate_clockwise(state[3])), rotate_clockwise(rotate_clockwise(state[5]))
        state[2], state[3] = state[3], state[2]
        print("flip top to right")

    flips.append(flip_top_to_right)  # Appending the above function to flips.

    def flip_top_to_left() -> None:
        """
        Flips the top face of the cube to left i.e, the top face becomes left face.
        :return: Returns nothing.
        """
        state[0] = rotate_clockwise(state[0])  # Rotate the back face of the cube clockwise.
        state[4] = rotate_anti_clockwise(state[4])  # Rotate the front face of the cube counterclockwise.

        # Change the remaining faces of the cube appropriately.
        state[2], state[1] = state[1], state[2]
        state[5], state[3] = rotate_clockwise(rotate_clockwise(state[3])), rotate_clockwise(rotate_clockwise(state[5]))
        state[1], state[5] = rotate_clockwise(rotate_clockwise(state[5])), rotate_clockwise(rotate_clockwise(state[1]))
        print("flip top to left")

    flips.append(flip_top_to_left)  # Appending the above function  to the flips.

    return flips


def turn_generator() -> list:
    """
    Generates the functions that can turn cube.
    :return: Returns a list of functions where each function turns the cube uniquely.
    """
    turns = []  # Initializing a list to store the turn functions.

    def turn_cube_right() -> None:
        """
        Turns the cube clockwise by 90 degrees around top face.
        :return: Returns nothing.
        """
        state[1] = rotate_clockwise(state[1])  # Rotate the top face of the cube clockwise.
        state[5] = rotate_anti_clockwise(state[5])  # Rotate the bottom face of the cube counterclockwise.

        # Change the remaining faces appropriately.
        state[0], state[2], state[4], state[3] = rotate_clockwise(state[2]), rotate_clockwise(
            state[4]), rotate_clockwise(state[3]), rotate_clockwise(state[0])
        print("turn_cube_clock_wise_around_top")

    turns.append(turn_cube_right)  # Appending the above function to turns.

    def turn_cube_left() -> None:
        """
        Turns the cube counterclockwise by 90 degrees around top face.
        :return: Returns nothing.
        """
        state[1] = rotate_anti_clockwise(state[1])  # Rotate the top face of the cube counterclockwise.
        state[5] = rotate_clockwise(state[5])  # Rotate the bottom face of the cube clockwise.

        # Change the remaining faces appropriately.
        state[0], state[2], state[4], state[3] = rotate_anti_clockwise(state[3]), rotate_anti_clockwise(
            state[0]), rotate_anti_clockwise(state[2]), rotate_anti_clockwise(state[4])
        print("turn_cube_anti_clock_wise_around_top")

    turns.append(turn_cube_left)  # Appending the above function to turns.
    return turns


def solved_state(n: int) -> str:
    """
    Generates a solved state of the cube which then can be scrambled and solved.
    :param n: n is the size of the cube.
    :return: Returns a string which represents solved state of a cube.
    """
    string = ""  # Initializing an empty string which can be modified and then returned.
    string_ = "brwygo"  # Declaring a string with 6 characters representing 6 colors of the cube.

    # Initializing a for loop to run through the characters of string_.
    for ch in string_:
        string = string + ch * (n * n)  # Appending ch to the string by n squared times.
    return string


def scrambler(n: int) -> None:
    """
    Generates a scrambled state from the solved state of the cube.

    :param n: n is the size of the cube.
    :return: returns nothing.
    """
    no_of_moves = random.randint(100, 500)  # Declare no_of_moves as a random value between 100 and 500

    # Scramble the cube by selecting random move and random i, no_of_moves times.
    for i in range(no_of_moves):
        a = random.randint(0, 11)  # Declare a as a random value between 0 and 11.
        b = random.randint(0, int(n / 2) - 1)  # Declare b as a random value between 0 and half the size of the cube.
        X[a](b)  # X is a list of move functions, X[a][b] is a random move.


def center_pieces_locator(piece_map: dict) -> list[list[list]]:
    """
    Stores the coordinates of the piece which is required at the given position.
    :param piece_map: A dictionary with current structure of the cube i.e, what faces are located where.
    :return: Returns a 3d list where each index position has the coordinates of the piece  which has to come there.
    """

    # Initialize mid_pieces with all elements as [0,0,0].
    mid_pieces = [[[[0, 0, 0] for _ in range(N)] for _ in range(N)] for _ in range(6)]

    # Go through each color of the cube and decide where that piece has to go, and then set the values of the piece in
    # that index of the mid_pieces.
    for c in range(6):
        for x in range(1, N - 1):
            for y in range(1, N - 1):
                # Skip unnecessary checks
                if N % 2 != 0 and x / 2 == y / 2 and 2 * x == N - 1:
                    continue

                destination_face = piece_map[state[c][x][y]]
                if c != destination_face:
                    if mid_pieces[destination_face][x][y] == [0, 0, 0] and \
                            state[destination_face][x][y] != state[c][x][y]:
                        mid_pieces[destination_face][x][y] = [c, x, y]

                    elif mid_pieces[destination_face][y][N - 1 - x] == [0, 0, 0] and \
                            state[destination_face][y][N - 1 - x] != state[c][x][y]:
                        mid_pieces[destination_face][y][N - 1 - x] = [c, x, y]

                    elif mid_pieces[destination_face][N - 1 - y][x] == [0, 0, 0] and \
                            state[destination_face][N - 1 - y][x] != state[c][x][y]:
                        mid_pieces[destination_face][N - 1 - y][x] = [c, x, y]

                    elif mid_pieces[destination_face][N - 1 - x][N - 1 - y] == [0, 0, 0] and \
                            state[destination_face][N - 1 - x][N - 1 - y] != state[c][x][y]:
                        mid_pieces[destination_face][N - 1 - x][N - 1 - y] = [c, x, y]

    return mid_pieces


def center_piece_arranger(target: tuple[int, int], position: tuple[int, int, int], color: str, func: list) -> None:
    """
    Arranges a piece at given position into the target.

    :param target:  target is the tuple of row and column value of the top face where a particular piece has to go.
    :param position: position is the tuple of face, row and column values of that particular piece.
    :param color: color is the color of the particular piece and the color of the top face.
    :param func: func is a list of function which is returned by the function moves_generator(n) .
    :return: Returns nothing.
    """

    i = target[0]  # I indicate row value of the target.
    j = target[1]  # j indicates column value of the target.
    a = position[1]  # 1.a indicates row value of the position of the required piece.
    b = position[2]  # 2.b indicates the column value of the position of the required piece.
    c = position[0]  # 3.c indicates the face on which the required piece.

    # Whenever the piece at i th row and j th column of the front face of the cube is not equal to the color,
    # then it has to be replaced with the piece at the position given in the parameters.
    if state[1][i][j] != color:

        # When the required piece is on opposite face, and the sum of row and column is size of cube minus -1.

        # That's it guys, I have no time to write comments for all this code. I'll try to do it when I have time.
        # Until then, please adjust with this half uncommented code.
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


def center_piece_solver(x, y):  # solves all the centerpieces of the given cube using centerpiece arranger function
    mid = center_pieces_locator({"b": 0, "r": 1, "w": 2, "y": 3, "g": 4, "o": 5})
    temporary = {}
    for i in range(N):
        for j in range(N):
            if mid[1][i][j] != [0, 0, 0]:
                if mid[1][i][j][0] == 5:
                    temporary[(i, j)] = mid[1][i][j]
                    continue
                center_piece_arranger((i, j), mid[1][i][j], "r", x)
    for i in temporary:
        center_piece_arranger(i, mid[1][i[0]][i[1]], "r", x)

    y[0]()
    mid = center_pieces_locator({"b": 1, "r": 4, "w": 2, "y": 3, "g": 5, "o": 0})
    temporary = {}
    for i in range(N):
        for j in range(N):
            if mid[1][i][j] != [0, 0, 0]:
                if mid[1][i][j][0] == 5:
                    temporary[(i, j)] = mid[1][i][j]
                    continue
                center_piece_arranger((i, j), mid[1][i][j], "b", x)
    for i in temporary:
        center_piece_arranger(i, mid[1][i[0]][i[1]], "b", x)

    y[2]()
    mid = center_pieces_locator({"b": 3, "r": 4, "w": 1, "y": 5, "g": 2, "o": 0})
    temporary = {}
    for i in range(N):
        for j in range(N):
            if mid[1][i][j] != [0, 0, 0]:
                if mid[1][i][j][0] == 5:
                    temporary[(i, j)] = mid[1][i][j]
                    continue
                center_piece_arranger((i, j), mid[1][i][j], "w", x)
    for i in temporary:
        center_piece_arranger(i, mid[1][i[0]][i[1]], "w", x)

    y[0]()
    mid = center_pieces_locator({"b": 3, "r": 5, "w": 4, "y": 0, "g": 2, "o": 1})
    temporary = {}
    for i in range(N):
        for j in range(N):
            if mid[1][i][j] != [0, 0, 0]:
                if mid[1][i][j][0] == 5:
                    temporary[(i, j)] = mid[1][i][j]
                    continue
                center_piece_arranger((i, j), mid[1][i][j], "o", x)
    for i in temporary:
        center_piece_arranger(i, mid[1][i[0]][i[1]], "o", x)

    y[2]()
    mid = center_pieces_locator({"b": 5, "r": 2, "w": 4, "y": 0, "g": 1, "o": 3})
    temporary = {}
    for i in range(N):
        for j in range(N):
            if mid[1][i][j] != [0, 0, 0]:
                if mid[1][i][j][0] == 5:
                    temporary[(i, j)] = mid[1][i][j]
                    continue
                center_piece_arranger((i, j), mid[1][i][j], "g", x)
    for i in temporary:
        center_piece_arranger(i, mid[1][i[0]][i[1]], "g", x)

    y[0]()
    y[2]()


def edge_locator(a, b):  # stores the coordinates of the current piece at the required coordinates
    flip_count = 0
    edge_location = list([0, 0] for _ in range(N))
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

        Y[1]()
        flip_count = flip_count + 1
    return edge_location


def edge_arranger(i, func):  # places the edge piece at the required position
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


def parity(func, i):  # algorithm to solve the parity errors
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
                Y[0]()
            elif v1 == 1:
                Y[2]()
            elif v1 == 2:
                Y[1]()
            else:
                Y[3]()
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


def mid_solver(current_position, func, turns):
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

    for i in range(8):
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
                    B(0)
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
                    Rdash(0)
                    B(0)
                    D(0)
                    D(0)
                    Bdash(0)
                    R(0)
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
                    elif current_position[4][1][-1] != g or current_position[3][-1][1] != y:
                        second_algo(func, turns)
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
    y = 0
    while x != 5 and y < 4:
        if x == 1:
            bottom_plus_algo(func)

        elif x == 2:
            while current_position[1][-1][1] != "o":
                func[8](0)
            for var in range(1, int(N / 2)):
                parity(func, var)

        elif x == 4:
            while current_position[1][-1][1] == "o":
                func[8](0)
            for var in range(1, int(N / 2)):
                parity(func, var)

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
        y = y + 1

    if current_position[1][0][1] != "o":
        func[8](0)
        func[8](0)
        for var in range(1, int(N / 2)):
            parity(func, var)

    elif current_position[1][1][0] != "o":
        func[9](0)
        for var in range(1, int(N / 2)):
            parity(func, var)

    elif current_position[1][1][-1] != "o":
        func[8](0)
        for var in range(1, int(N / 2)):
            parity(func, var)

    elif current_position[1][-1][1] != "o":
        for var in range(1, int(N / 2)):
            parity(func, var)


def captial_t(current_position, func, turns):
    turns[1]()
    turns[1]()
    centers = "gwbyg"
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
        1] + current_position[2][1][2] + current_position[4][0][1]
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
        elif a[0] == "w":
            turns[1]()
            mid_algo(func)
            turns[0]()
        else:
            turns[0]()
            mid_algo(func)
            turns[1]()


def last_layer(current_position, func, turns):
    R = func[0]
    Rdash = func[1]
    L = func[2]
    Ldash = func[3]
    U = func[8]
    Udash = func[9]
    D = func[10]
    Ddash = func[11]

    dummy_x = 0
    for i in range(4):
        reference = current_position[1][1][1] + current_position[4][1][1] + current_position[2][1][1] + \
                    current_position[1][1][1] + current_position[4][1][1] + current_position[2][1][1]
        a = current_position[1][-1][0] + current_position[4][0][0] + current_position[2][-1][-1]
        if a not in reference:
            turns[0]()
            dummy_x += 1
        else:
            break
    if dummy_x == 4:
        R(0)
        Udash(0)
        Ldash(0)
        U(0)
        Rdash(0)
        Udash(0)
        L(0)
        U(0)
        for i in range(4):
            reference = current_position[1][1][1] + current_position[4][1][1] + current_position[2][1][
                1] + \
                        current_position[1][1][1] + current_position[4][1][1] + current_position[2][1][1]
            a = current_position[1][-1][0] + current_position[4][0][0] + current_position[2][-1][-1]
            if a not in reference:
                turns[0]()
                dummy_x += 1
            else:
                break
    a = current_position[1][-1][-1] + current_position[4][0][-1] + current_position[3][-1][0]
    for i in range(4):
        reference = current_position[1][1][1] + current_position[4][1][1] + current_position[3][1][1] + \
                    current_position[1][1][1] + current_position[4][1][1] + current_position[3][1][1]
        if a not in reference:
            R(0)
            Udash(0)
            Ldash(0)
            U(0)
            Rdash(0)
            Udash(0)
            L(0)
            U(0)
            a = current_position[1][-1][-1] + current_position[4][0][-1] + current_position[3][-1][0]
    for i in range(4):
        while current_position[1][-1][-1] != "o":
            Rdash(0)
            D(0)
            R(0)
            Ddash(0)
        else:
            U(0)


def corner_parity(current_position, func, turns):
    if current_position[0][-1][0] != current_position[0][1][1] or current_position[0][-1][-1] != current_position[0][1][
        1] or current_position[2][0][-1] != current_position[2][1][1] or current_position[2][-1][-1] != \
            current_position[2][1][1] or current_position[3][0][0] != current_position[3][1][1] or \
            current_position[3][-1][0] != current_position[3][1][1] or current_position[4][0][0] != \
            current_position[4][1][1] or current_position[4][0][-1] != current_position[4][1][1]:
        for i in range(1, int(N / 2)):
            func[0](i)
            func[0](i)
        func[8](0)
        func[8](0)
        for i in range(1, int(N / 2)):
            func[0](i)
            func[0](i)
        func[8](0)
        func[8](0)
        for i in range(1, int(N / 2)):
            func[8](i)
            func[8](i)
        for i in range(1, int(N / 2)):
            func[0](i)
            func[0](i)
        func[8](0)
        func[8](0)
        for i in range(1, int(N / 2)):
            func[8](i)
            func[8](i)

        while current_position[4][1][1] != "b":
            turns[0]()
        captial_t(current_position, func, turns)
        last_layer(current_position, func, turns)


# Generates a solved state of a cube of a random size between 3, 30. You can change that 30 value to any value you
# want but, time increases with the size of the cube
state, N = splitter("byywyooywybbbgbbyyryobggo"
                    "gorrgboybbgorrgwwwwgyoyyy"
                    "rbrryyggbwrbwrygooggrbwr"
                    "bwooooygbbwwgybgogobwgoyo"
                    "orgrrrgwwowoggoorrwywgwwy"
                    "wwbbgbyryyrwroworrryrwbbgb")
display_cube(state)
X = moves_generator(N)  # Generating the moves.
Y = flips_generator()  # Generating the flips.
Z = turn_generator()  # Generating the turns.

display_cube(state)
center_piece_solver(X, Y)  # Solving the centers of the cube.
display_cube(state)
edge_solver(X)  # Solving the edges of the cube.
display_cube(state)
plus(X, Z)  # Making a plus on reduced cube.
display_cube(state)
mid_solver(state, X, Z)
top_layer(state, X)  # Solving the top layer of the cube.
display_cube(state)
second_layer(state, X, Z)  # Solving the second layer of the reduced cube.
display_cube(state)
bottom_plus(state, X, Y, Z)
display_cube(state)
captial_t(state, X, Z)
display_cube(state)
last_layer(state, X, Z)  # Solving the last layer of the reduced cube.
corner_parity(state, X, Z)  # Checking for parity errors and solving if any.
display_cube(state)
print(NUMBER_OF_MOVES)
