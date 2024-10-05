b = "b"
g = "g"
r = "r"
w = "w"
o = "o"
y = "y"
current_position = {"top": [[r, r, o], [w, r, w], [g, y, y]], "front": [[w, g, g], [r, g, w], [y, y, r]],
                    "opposite": [[y, r, b], [b, b, r], [y, b, w]],
                    "right": [[g, g, o], [b, y, o], [o, g, w]], "left": [[g, y, b], [g, w, o], [o, w, r]],
                    "bottom": [[b, o, b], [o, o, b], [r, y, w]]}

no_of_moves = 0


def flip_top_to_south():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    for i in right:
        for j in range(len(i)):
            if j == 2:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])

    r1_ = []
    r2_ = []
    r3_ = []
    for i in left:
        for j in range(len(i)):
            if j == 0:
                r1_.append(i[j])
            elif j == 1:
                r2_.append(i[j])
            else:
                r3_.append(i[j])
    r1_.reverse()
    r2_.reverse()
    r3_.reverse()
    current_position["top"] = opposite
    current_position['front'] = top
    current_position["opposite"] = bottom
    current_position['bottom'] = front
    current_position["left"] = [r1_, r2_, r3_]
    current_position["right"] = [r1, r2, r3]
    print("flip top to south")


def flip_top_to_north():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    for i in left:
        for j in range(len(i)):
            if j == 2:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    r1_ = []
    r2_ = []
    r3_ = []
    for i in right:
        for j in range(len(i)):
            if j == 0:
                r1_.append(i[j])
            elif j == 1:
                r2_.append(i[j])
            else:
                r3_.append(i[j])
    r1_.reverse()
    r2_.reverse()
    r3_.reverse()
    current_position["top"] = front
    current_position['front'] = bottom
    current_position["opposite"] = top
    current_position['bottom'] = opposite
    current_position["right"] = [r1_, r2_, r3_]
    current_position["left"] = [r1, r2, r3]
    print("flip top to north")


def flip_top_to_west():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    for i in opposite:
        for j in range(len(i)):
            if j == 2:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    r1.reverse()
    r2.reverse()
    r3.reverse()
    r1_ = []
    r2_ = []
    r3_ = []
    for i in front:
        for j in range(len(i)):
            if j == 0:
                r1_.append(i[j])
            elif j == 1:
                r2_.append(i[j])
            else:
                r3_.append(i[j])
    left[0].reverse()
    left[1].reverse()
    left[2].reverse()
    left.reverse()
    bottom[0].reverse()
    bottom[1].reverse()
    bottom[2].reverse()
    bottom.reverse()
    current_position["top"] = right
    current_position['front'] = [r3_, r2_, r1_]
    current_position["opposite"] = [r3, r2, r1]
    current_position['bottom'] = left
    current_position["right"] = bottom
    current_position["left"] = top
    print("flip top to west")


def flip_top_to_east():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    for i in front:
        for j in range(len(i)):
            if j == 2:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    r1.reverse()
    r2.reverse()
    r3.reverse()
    r1_ = []
    r2_ = []
    r3_ = []
    for i in opposite:
        for j in range(len(i)):
            if j == 0:
                r1_.append(i[j])
            elif j == 1:
                r2_.append(i[j])
            else:
                r3_.append(i[j])
    bottom[0].reverse()
    bottom[1].reverse()
    bottom[2].reverse()
    bottom.reverse()
    right[0].reverse()
    right[1].reverse()
    right[2].reverse()
    right.reverse()
    current_position["top"] = left
    current_position['front'] = [r3, r2, r1]
    current_position["opposite"] = [r3_, r2_, r1_]
    current_position['bottom'] = right
    current_position["right"] = top
    current_position["left"] = bottom
    print("flip top to east")


def flip_top_to_bottom():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    right[0].reverse()
    right[1].reverse()
    right[2].reverse()
    right.reverse()
    left[0].reverse()
    left[1].reverse()
    left[2].reverse()
    left.reverse()
    current_position["top"] = bottom
    current_position['bottom'] = top
    current_position['front'] = opposite
    current_position["opposite"] = front
    current_position["left"] = left
    current_position['right'] = right
    print("flip top to bottom")


def turn_cube_to_right():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]

    r1 = []
    r2 = []
    r3 = []
    for i in top:
        for j in range(len(i)):
            if j == 2:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    r1.reverse()
    r2.reverse()
    r3.reverse()

    r1_ = []
    r2_ = []
    r3_ = []
    for i in front:
        for j in range(len(i)):
            if j == 0:
                r1_.append(i[j])
            elif j == 1:
                r2_.append(i[j])
            else:
                r3_.append(i[j])
    r1_.reverse()
    r2_.reverse()
    r3_.reverse()

    r1__ = []
    r2__ = []
    r3__ = []
    for i in opposite:
        for j in range(len(i)):
            if j == 2:
                r1__.append(i[j])
            elif j == 1:
                r2__.append(i[j])
            else:
                r3__.append(i[j])
    r1__.reverse()
    r2__.reverse()
    r3__.reverse()

    r11 = []
    r21 = []
    r31 = []
    for i in left:
        for j in range(len(i)):
            if j == 2:
                r11.append(i[j])
            elif j == 1:
                r21.append(i[j])
            else:
                r31.append(i[j])
    r11.reverse()
    r21.reverse()
    r31.reverse()

    r11_ = []
    r21_ = []
    r31_ = []
    for i in right:
        for j in range(len(i)):
            if j == 2:
                r11_.append(i[j])
            elif j == 1:
                r21_.append(i[j])
            else:
                r31_.append(i[j])
    r11_.reverse()
    r21_.reverse()
    r31_.reverse()

    r111_ = []
    r211_ = []
    r311_ = []
    for i in bottom:
        for j in range(len(i)):
            if j == 2:
                r111_.append(i[j])
            elif j == 1:
                r211_.append(i[j])
            else:
                r311_.append(i[j])
    current_position["top"] = [r3, r2, r1]
    current_position['front'] = [r31_, r21_, r11_]
    current_position["opposite"] = [r31, r21, r11]
    current_position['bottom'] = [r111_, r211_, r311_]
    current_position["left"] = [r1_, r2_, r3_]
    current_position["right"] = [r3__, r2__, r1__]

    print("turn cube to right")


def turn_cube_to_left():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]

    r1 = []
    r2 = []
    r3 = []
    for i in top:
        for j in range(len(i)):
            if j == 2:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])

    r1_ = []
    r2_ = []
    r3_ = []
    for i in front:
        for j in range(len(i)):
            if j == 0:
                r1_.append(i[j])
            elif j == 1:
                r2_.append(i[j])
            else:
                r3_.append(i[j])

    r1__ = []
    r2__ = []
    r3__ = []
    for i in opposite:
        for j in range(len(i)):
            if j == 2:
                r1__.append(i[j])
            elif j == 1:
                r2__.append(i[j])
            else:
                r3__.append(i[j])

    r11 = []
    r21 = []
    r31 = []
    for i in left:
        for j in range(len(i)):
            if j == 2:
                r11.append(i[j])
            elif j == 1:
                r21.append(i[j])
            else:
                r31.append(i[j])

    r11_ = []
    r21_ = []
    r31_ = []
    for i in right:
        for j in range(len(i)):
            if j == 2:
                r11_.append(i[j])
            elif j == 1:
                r21_.append(i[j])
            else:
                r31_.append(i[j])

    r111_ = []
    r211_ = []
    r311_ = []
    for i in bottom:
        for j in range(len(i)):
            if j == 2:
                r111_.append(i[j])
            elif j == 1:
                r211_.append(i[j])
            else:
                r311_.append(i[j])
    r111_.reverse()
    r211_.reverse()
    r311_.reverse()
    current_position["top"] = [r1, r2, r3]
    current_position['front'] = [r11, r21, r31]
    current_position["opposite"] = [r11_, r21_, r31_]
    current_position['bottom'] = [r311_, r211_, r111_]
    current_position["left"] = [r1__, r2__, r3__]
    current_position["right"] = [r3_, r2_, r1_]

    print("turn cube to left")


def U():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    left[0][2], opposite[2][2] = opposite[2][2], left[0][2]
    left[1][2], opposite[2][1] = opposite[2][1], left[1][2]
    left[2][2], opposite[2][0] = opposite[2][0], left[2][2]
    left[0][2], front[0][0] = front[0][0], left[0][2]
    left[1][2], front[0][1] = front[0][1], left[1][2]
    left[2][2], front[0][2] = front[0][2], left[2][2]
    front[0][0], right[2][0] = right[2][0], front[0][0]
    front[0][1], right[1][0] = right[1][0], front[0][1]
    front[0][2], right[0][0] = right[0][0], front[0][2]
    for i in top:
        for j in range(len(i)):
            if j == 0:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    r1.reverse()
    r2.reverse()
    r3.reverse()
    current_position["top"] = [r1, r2, r3]
    current_position["bottom"] = bottom
    current_position["right"] = right
    current_position["left"] = left
    current_position["front"] = front
    current_position["opposite"] = opposite
    print("U")


def Udash():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    left[0][2], opposite[2][2] = opposite[2][2], left[0][2]
    left[1][2], opposite[2][1] = opposite[2][1], left[1][2]
    left[2][2], opposite[2][0] = opposite[2][0], left[2][2]
    opposite[2][2], right[2][0] = right[2][0], opposite[2][2]
    opposite[2][1], right[1][0] = right[1][0], opposite[2][1]
    opposite[2][0], right[0][0] = right[0][0], opposite[2][0]
    front[0][0], right[2][0] = right[2][0], front[0][0]
    front[0][1], right[1][0] = right[1][0], front[0][1]
    front[0][2], right[0][0] = right[0][0], front[0][2]
    for i in top:
        for j in range(len(i)):
            if j == 0:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    current_position["top"] = [r3, r2, r1]
    current_position["bottom"] = bottom
    current_position["right"] = right
    current_position["left"] = left
    current_position["front"] = front
    current_position["opposite"] = opposite
    print("Udash")


def D():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    left[0][0], opposite[0][2] = opposite[0][2], left[0][0]
    left[1][0], opposite[0][1] = opposite[0][1], left[1][0]
    left[2][0], opposite[0][0] = opposite[0][0], left[2][0]
    opposite[0][2], right[2][2] = right[2][2], opposite[0][2]
    opposite[0][1], right[1][2] = right[1][2], opposite[0][1]
    opposite[0][0], right[0][2] = right[0][2], opposite[0][0]
    front[2][0], right[2][2] = right[2][2], front[2][0]
    front[2][1], right[1][2] = right[1][2], front[2][1]
    front[2][2], right[0][2] = right[0][2], front[2][2]
    for i in bottom:
        for j in range(len(i)):
            if j == 0:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    r1.reverse()
    r2.reverse()
    r3.reverse()
    current_position["top"] = top
    current_position["bottom"] = [r1, r2, r3]
    current_position["right"] = right
    current_position["left"] = left
    current_position["front"] = front
    current_position["opposite"] = opposite
    print("D")


def Ddash():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    left[0][0], opposite[0][2] = opposite[0][2], left[0][0]
    left[1][0], opposite[0][1] = opposite[0][1], left[1][0]
    left[2][0], opposite[0][0] = opposite[0][0], left[2][0]
    left[0][0], front[2][0] = front[2][0], left[0][0]
    left[1][0], front[2][1] = front[2][1], left[1][0]
    left[2][0], front[2][2] = front[2][2], left[2][0]
    front[2][0], right[2][2] = right[2][2], front[2][0]
    front[2][1], right[1][2] = right[1][2], front[2][1]
    front[2][2], right[0][2] = right[0][2], front[2][2]
    for i in bottom:
        for j in range(len(i)):
            if j == 0:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    current_position["top"] = top
    current_position["bottom"] = [r3, r2, r1]
    current_position["right"] = right
    current_position["left"] = left
    current_position["front"] = front
    current_position["opposite"] = opposite
    print("Ddash")


def R():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    top[0][2], opposite[0][2] = opposite[0][2], top[0][2]
    top[1][2], opposite[1][2] = opposite[1][2], top[1][2]
    top[2][2], opposite[2][2] = opposite[2][2], top[2][2]
    top[0][2], front[0][2] = front[0][2], top[0][2]
    top[1][2], front[1][2] = front[1][2], top[1][2]
    top[2][2], front[2][2] = front[2][2], top[2][2]
    front[0][2], bottom[0][2] = bottom[0][2], front[0][2]
    front[1][2], bottom[1][2] = bottom[1][2], front[1][2]
    front[2][2], bottom[2][2] = bottom[2][2], front[2][2]

    for i in right:
        for j in range(len(i)):
            if j == 0:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    r1.reverse()
    r2.reverse()
    r3.reverse()
    current_position["top"] = top
    current_position["bottom"] = bottom
    current_position["right"] = [r1, r2, r3]
    current_position["left"] = left
    current_position["front"] = front
    current_position["opposite"] = opposite
    print("R")


def Rdash():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    top[0][2], opposite[0][2] = opposite[0][2], top[0][2]
    top[1][2], opposite[1][2] = opposite[1][2], top[1][2]
    top[2][2], opposite[2][2] = opposite[2][2], top[2][2]
    opposite[0][2], bottom[0][2] = bottom[0][2], opposite[0][2]
    opposite[1][2], bottom[1][2] = bottom[1][2], opposite[1][2]
    opposite[2][2], bottom[2][2] = bottom[2][2], opposite[2][2]
    front[0][2], bottom[0][2] = bottom[0][2], front[0][2]
    front[1][2], bottom[1][2] = bottom[1][2], front[1][2]
    front[2][2], bottom[2][2] = bottom[2][2], front[2][2]

    for i in right:
        for j in range(len(i)):
            if j == 0:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    current_position["top"] = top
    current_position["bottom"] = bottom
    current_position["right"] = [r3, r2, r1]
    current_position["left"] = left
    current_position["front"] = front
    current_position["opposite"] = opposite
    print("Rdash")


def L():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    top[0][0], opposite[0][0] = opposite[0][0], top[0][0]
    top[1][0], opposite[1][0] = opposite[1][0], top[1][0]
    top[2][0], opposite[2][0] = opposite[2][0], top[2][0]
    opposite[0][0], bottom[0][0] = bottom[0][0], opposite[0][0]
    opposite[1][0], bottom[1][0] = bottom[1][0], opposite[1][0]
    opposite[2][0], bottom[2][0] = bottom[2][0], opposite[2][0]
    front[0][0], bottom[0][0] = bottom[0][0], front[0][0]
    front[1][0], bottom[1][0] = bottom[1][0], front[1][0]
    front[2][0], bottom[2][0] = bottom[2][0], front[2][0]
    for i in left:
        for j in range(len(i)):
            if j == 0:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    r1.reverse()
    r2.reverse()
    r3.reverse()

    current_position["top"] = top
    current_position["bottom"] = bottom
    current_position["right"] = right
    current_position["left"] = [r1, r2, r3]
    current_position["front"] = front
    current_position["opposite"] = opposite
    print("L")


def Ldash():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    top[0][0], opposite[0][0] = opposite[0][0], top[0][0]
    top[1][0], opposite[1][0] = opposite[1][0], top[1][0]
    top[2][0], opposite[2][0] = opposite[2][0], top[2][0]
    top[0][0], front[0][0] = front[0][0], top[0][0]
    top[1][0], front[1][0] = front[1][0], top[1][0]
    top[2][0], front[2][0] = front[2][0], top[2][0]
    front[0][0], bottom[0][0] = bottom[0][0], front[0][0]
    front[1][0], bottom[1][0] = bottom[1][0], front[1][0]
    front[2][0], bottom[2][0] = bottom[2][0], front[2][0]

    for i in left:
        for j in range(len(i)):
            if j == 0:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    current_position["top"] = top
    current_position["bottom"] = bottom
    current_position["right"] = right
    current_position["left"] = [r3, r2, r1]
    current_position["front"] = front
    current_position["opposite"] = opposite
    print("Ldash")


def F():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    left[2][0], top[2][0] = top[2][0], left[2][0]
    left[2][1], top[2][1] = top[2][1], left[2][1]
    left[2][2], top[2][2] = top[2][2], left[2][2]
    left[2][0], bottom[0][2] = bottom[0][2], left[2][0]
    left[2][1], bottom[0][1] = bottom[0][1], left[2][1]
    left[2][2], bottom[0][0] = bottom[0][0], left[2][2]
    bottom[0][2], right[2][0] = right[2][0], bottom[0][2]
    bottom[0][1], right[2][1] = right[2][1], bottom[0][1]
    bottom[0][0], right[2][2] = right[2][2], bottom[0][0]
    for i in front:
        for j in range(len(i)):
            if j == 0:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    r1.reverse()
    r2.reverse()
    r3.reverse()

    current_position["top"] = top
    current_position["bottom"] = bottom
    current_position["right"] = right
    current_position["left"] = left
    current_position["front"] = [r1, r2, r3]
    current_position["opposite"] = opposite
    print("F")


def Fdash():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    left[2][0], top[2][0] = top[2][0], left[2][0]
    left[2][1], top[2][1] = top[2][1], left[2][1]
    left[2][2], top[2][2] = top[2][2], left[2][2]
    top[2][0], right[2][0] = right[2][0], top[2][0]
    top[2][1], right[2][1] = right[2][1], top[2][1]
    top[2][2], right[2][2] = right[2][2], top[2][2]
    bottom[0][2], right[2][0] = right[2][0], bottom[0][2]
    bottom[0][1], right[2][1] = right[2][1], bottom[0][1]
    bottom[0][0], right[2][2] = right[2][2], bottom[0][0]
    for i in front:
        for j in range(len(i)):
            if j == 0:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    current_position["top"] = top
    current_position["bottom"] = bottom
    current_position["right"] = right
    current_position["left"] = left
    current_position["front"] = [r3, r2, r1]
    current_position["opposite"] = opposite
    print("Fdash")


def B():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    left[0][0], top[0][0] = top[0][0], left[0][0]
    left[0][1], top[0][1] = top[0][1], left[0][1]
    left[0][2], top[0][2] = top[0][2], left[0][2]
    top[0][0], right[0][0] = right[0][0], top[0][0]
    top[0][1], right[0][1] = right[0][1], top[0][1]
    top[0][2], right[0][2] = right[0][2], top[0][2]
    bottom[2][2], right[0][0] = right[0][0], bottom[2][2]
    bottom[2][1], right[0][1] = right[0][1], bottom[2][1]
    bottom[2][0], right[0][2] = right[0][2], bottom[2][0]
    for i in opposite:
        for j in range(len(i)):
            if j == 0:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    r1.reverse()
    r2.reverse()
    r3.reverse()
    current_position["top"] = top
    current_position["bottom"] = bottom
    current_position["right"] = right
    current_position["left"] = left
    current_position["front"] = front
    current_position["opposite"] = [r1, r2, r3]
    print("B")


def Bdash():
    global no_of_moves
    no_of_moves += 1
    top = current_position["top"]
    front = current_position['front']
    opposite = current_position['opposite']
    left = current_position["left"]
    right = current_position["right"]
    bottom = current_position["bottom"]
    r1 = []
    r2 = []
    r3 = []
    left[0][0], top[0][0] = top[0][0], left[0][0]
    left[0][1], top[0][1] = top[0][1], left[0][1]
    left[0][2], top[0][2] = top[0][2], left[0][2]
    left[0][0], bottom[2][2] = bottom[2][2], left[0][0]
    left[0][1], bottom[2][1] = bottom[2][1], left[0][1]
    left[0][2], bottom[2][0] = bottom[2][0], left[0][2]
    bottom[2][2], right[0][0] = right[0][0], bottom[2][2]
    bottom[2][1], right[0][1] = right[0][1], bottom[2][1]
    bottom[2][0], right[0][2] = right[0][2], bottom[2][0]
    for i in opposite:
        for j in range(len(i)):
            if j == 0:
                r1.append(i[j])
            elif j == 1:
                r2.append(i[j])
            else:
                r3.append(i[j])
    current_position["top"] = top
    current_position["bottom"] = bottom
    current_position["right"] = right
    current_position["left"] = left
    current_position["front"] = front
    current_position["opposite"] = [r3, r2, r1]
    print("F")


def display_cube():
    color_index = {"r": "🟥", "g": "🟩", "w": "⬜", "b": "🟦", "y": "🟨", "o": "🟧"}
    for i in current_position["opposite"]:
        for j in range(3):
            if j == 0:
                print(f"         {color_index[i[j]]}", end="")
            elif j == 1:
                print(f"{color_index[i[j]]}", end="")
            else:
                print(f"{color_index[i[j]]}")
    print("")
    for i in range(3):
        print(
            f"{color_index[current_position['left'][i][0]]}{color_index[current_position['left'][i][1]]}{color_index[current_position['left'][i][2]]}",
            end="  ")
        print(
            f"{color_index[current_position['top'][i][0]]}{color_index[current_position['top'][i][1]]}{color_index[current_position['top'][i][2]]}",
            end="  ")
        print(
            f"{color_index[current_position['right'][i][0]]}{color_index[current_position['right'][i][1]]}{color_index[current_position['right'][i][2]]}")
    print("")
    for i in current_position["front"]:
        for j in range(3):
            if j == 0:
                print(f"         {color_index[i[j]]}", end="")
            elif j == 1:
                print(f"{color_index[i[j]]}", end="")
            else:
                print(f"{color_index[i[j]]}")
    print("")
    for i in current_position["bottom"]:
        for j in range(3):
            if j == 0:
                print(f"         {color_index[i[j]]}", end="")
            elif j == 1:
                print(f"{color_index[i[j]]}", end="")
            else:
                print(f"{color_index[i[j]]}")


def plus():
    boxes = [1, 2, 3, 4]
    count = 4
    for i in range(3):
        if i == 1:
            x = current_position["top"][i][0]
            if x == r:
                count -= 1
                boxes.remove(4)
            y = current_position["top"][i][2]
            if y == r:
                count -= 1
                boxes.remove(2)
        else:
            x = current_position["top"][i][1]
            if x == r:
                count -= 1
                boxes.remove(i + 1)
    if count != 0:
        for i in boxes:
            if i == 2:
                pass
            elif i == 1:
                turn_cube_to_right()
            elif i == 3:
                turn_cube_to_left()
            else:
                turn_cube_to_left()
                turn_cube_to_left()
            if i:
                if current_position["opposite"][1][2] == r:
                    Rdash()
                elif current_position["bottom"][1][2] == r:
                    R()
                    R()
                elif current_position["right"][0][1] == r:
                    Udash()
                    B()
                    U()
                elif current_position["right"][1][0] == r:
                    R()
                    Udash()
                    B()
                    U()
                elif current_position["right"][1][2] == r:
                    Rdash()
                    Udash()
                    B()
                    U()
                elif current_position["right"][2][1] == r:
                    U()
                    Fdash()
                    Udash()
                elif current_position["left"][0][1] == r:
                    Udash()
                    Bdash()
                    U()
                elif current_position["left"][1][0] == r:
                    L()
                    Udash()
                    Bdash()
                    U()
                    Ldash()
                elif current_position["left"][1][2] == r:
                    Ldash()
                    Udash()
                    Bdash()
                    U()
                    L()
                elif current_position["left"][2][1] == r:
                    U()
                    F()
                    Udash()
                elif current_position["front"][1][2] == r:
                    R()
                elif current_position["front"][0][1] == r:
                    F()
                    R()
                elif current_position["front"][1][0] == r:
                    F()
                    F()
                    R()
                    Fdash()
                    Fdash()
                elif current_position["front"][2][1] == r:
                    Fdash()
                    R()
                    F()
                elif current_position["opposite"][0][1] == r:
                    B()
                    Rdash()
                    Bdash()
                elif current_position["opposite"][1][0] == r:
                    B()
                    B()
                    Rdash()
                    Bdash()
                    Bdash()
                elif current_position["opposite"][2][1] == r:
                    Bdash()
                    Rdash()
                elif current_position["bottom"][0][1] == r:
                    U()
                    F()
                    F()
                    Udash()
                elif current_position["bottom"][1][0] == r:
                    D()
                    D()
                    R()
                    R()
                elif current_position["bottom"][2][1] == r:
                    Bdash()
                    R()
                    R()
                else:
                    pass
            if i == 2:
                pass
            elif i == 1:
                turn_cube_to_left()
            elif i == 3:
                turn_cube_to_right()
            else:
                turn_cube_to_left()
                turn_cube_to_left()


def mids_algo():
    U()
    R()
    U()
    Rdash()
    U()
    R()
    U()
    U()
    Rdash()


def mids():
    centers = "gybwg"
    top_centers = current_position["front"][0][1] + current_position["right"][1][0] + current_position["opposite"][2][
        1] + current_position["left"][1][2] + current_position["front"][0][1]
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
            U()
    else:
        x = abs(x)
        for j in range(x):
            Udash()
    top_centers = current_position["front"][0][1] + current_position["right"][1][0] + current_position["opposite"][2][
        1] + current_position["left"][1][2] + current_position["front"][0][1]
    if des == "yes":
        turn_cube_to_right()
        mids_algo()
        Udash()
        turn_cube_to_left()
        mids_algo()
    elif top_centers == centers:
        pass
    else:
        if a[0] == b:
            mids_algo()
        elif a[0] == g:
            turn_cube_to_right()
            turn_cube_to_right()
            mids_algo()
            turn_cube_to_left()
            turn_cube_to_left()
        elif a[0] == y:
            turn_cube_to_left()
            mids_algo()
            turn_cube_to_right()
        else:
            turn_cube_to_right()
            mids_algo()
            turn_cube_to_left()


def top_layer():
    for i in range(4):
        if current_position["top"][0][2] == r:
            a_ = current_position["opposite"][2][2]
            b_ = current_position["right"][0][0]
            if a_ == w:
                if b_ == b:
                    Bdash()
                    D()
                    B()
                    D()
                    Ldash()
                    Ddash()
                    L()
            elif a_ == g:
                if b_ == w:
                    Bdash()
                    Ddash()
                    Ddash()
                    B()
                    L()
                    D()
                    Ldash()
            elif a_ == y:
                if b_ == g:
                    Bdash()
                    Ddash()
                    B()
                    F()
                    D()
                    Fdash()
        if current_position["top"][2][2] == r:
            a_ = current_position['front'][0][2]
            b_ = current_position["right"][2][0]
            if a_ == b:
                if b_ == w:
                    F()
                    B()
                    Ddash()
                    Ddash()
                    Fdash()
                    Bdash()
            elif a_ == y:
                if b_ == b:
                    F()
                    D()
                    Fdash()
                    Bdash()
                    Ddash()
                    B()
            elif a_ == w:
                if b_ == g:
                    Rdash()
                    Ddash()
                    R()
                    L()
                    D()
                    Ldash()
        if current_position["top"][0][0] == r:
            a_ = current_position["opposite"][2][0]
            b_ = current_position["left"][0][2]
            if a_ == g:
                if b_ == y:
                    Rdash()
                    Ldash()
                    D()
                    D()
                    R()
                    L()
            elif a_ == y:
                if b_ == b:
                    Ldash()
                    Ddash()
                    L()
                    R()
                    D()
                    Rdash()
            elif a_ == w:
                if b_ == g:
                    B()
                    D()
                    Bdash()
                    Fdash()
                    Ddash()
                    F()
        if current_position["top"][2][0] == r:
            a_ = current_position["left"][2][2]
            b_ = current_position["front"][0][0]
            if a_ == g:
                if b_ == y:
                    L()
                    D()
                    Ldash()
                    Rdash()
                    Ddash()
                    R()
            elif a_ == y:
                if b_ == b:
                    L()
                    R()
                    D()
                    D()
                    Rdash()
                    Ldash()
            elif a_ == b:
                if b_ == w:
                    Fdash()
                    Ddash()
                    F()
                    B()
                    D()
                    Bdash()
        if current_position["front"][0][2] == r:
            a_ = current_position["top"][2][2]
            b_ = current_position["right"][2][0]
            if a_ == b:
                if b_ == y:
                    F()
                    Bdash()
                    D()
                    Fdash()
                    B()
            elif a_ == w:
                if b_ == b:
                    F()
                    Ldash()
                    D()
                    D()
                    L()
                    Fdash()
            elif a_ == g:
                if b_ == w:
                    F()
                    Ddash()
                    Ddash()
                    Fdash()
                    Fdash()
                    D()
                    F()
            else:
                Rdash()
                D()
                R()
                Ddash()
                Rdash()
                D()
                R()
        elif current_position["front"][2][2] == r:
            a_ = current_position["right"][2][2]
            b_ = current_position["bottom"][0][2]
            if a_ == y:
                if b_ == g:
                    Ddash()
                    Rdash()
                    D()
                    R()
            elif a_ == b:
                if b_ == y:
                    Bdash()
                    D()
                    B()
            elif a_ == w:
                if b_ == b:
                    Ldash()
                    D()
                    D()
                    L()
            elif a_ == g:
                if b_ == w:
                    Ddash()
                    L()
                    D()
                    Ldash()
        elif current_position["bottom"][0][2] == r:
            a_ = current_position['front'][2][2]
            b_ = current_position["right"][2][2]
            if a_ == y:
                if b_ == g:
                    Rdash()
                    D()
                    D()
                    R()
                    D()
                    Rdash()
                    Ddash()
                    R()
            elif a_ == b:
                if b_ == y:
                    U()
                    Rdash()
                    D()
                    D()
                    R()
                    D()
                    Rdash()
                    Ddash()
                    R()
                    Udash()
            elif a_ == w:
                if b_ == b:
                    U()
                    U()
                    Rdash()
                    D()
                    D()
                    R()
                    D()
                    Rdash()
                    Ddash()
                    R()
                    Udash()
                    Udash()
            elif a_ == g:
                if b_ == w:
                    Udash()
                    Rdash()
                    D()
                    D()
                    R()
                    D()
                    Rdash()
                    Ddash()
                    R()
                    U()
        elif current_position["bottom"][2][2] == r:
            a_ = current_position["right"][0][2]
            b_ = current_position["opposite"][0][2]
            if a_ == y:
                if b_ == g:
                    Ddash()
                    Rdash()
                    D()
                    D()
                    R()
                    D()
                    Rdash()
                    Ddash()
                    R()
            elif a_ == b:
                if b_ == y:
                    Ddash()
                    U()
                    Rdash()
                    D()
                    D()
                    R()
                    D()
                    Rdash()
                    Ddash()
                    R()
                    Udash()
            elif a_ == w:
                if b_ == b:
                    Ddash()
                    U()
                    U()
                    Rdash()
                    D()
                    D()
                    R()
                    D()
                    Rdash()
                    Ddash()
                    R()
                    Udash()
                    Udash()
            elif a_ == g:
                if b_ == w:
                    Ddash()
                    Udash()
                    Rdash()
                    D()
                    D()
                    R()
                    D()
                    Rdash()
                    Ddash()
                    R()
                    U()
        elif current_position["opposite"][0][2] == r:
            a_ = current_position["right"][0][2]
            b_ = current_position["bottom"][2][2]
            if a_ == y:
                if b_ == b:
                    Bdash()
                    Ddash()
                    B()
            elif a_ == b:
                if b_ == w:
                    D()
                    Ldash()
                    Ddash()
                    L()
            elif a_ == w:
                if b_ == g:
                    L()
                    D()
                    D()
                    Ldash()
            else:
                Ddash()
                Rdash()
                Ddash()
                R()
        elif current_position["opposite"][2][2] == r:
            a_ = current_position["top"][0][2]
            b_ = current_position["right"][0][0]
            if a_ == y:
                if b_ == b:
                    Bdash()
                    Ddash()
                    B()
                    D()
                    Bdash()
                    Ddash()
                    B()
            elif a_ == b:
                if b_ == w:
                    Bdash()
                    Ddash()
                    B()
                    B()
                    D()
                    D()
                    Bdash()
            elif a_ == g:
                if b_ == y:
                    F()
                    Bdash()
                    Ddash()
                    Fdash()
                    Bdash()
            else:
                Bdash()
                L()
                D()
                D()
                Ldash()
                B()
        elif current_position["right"][0][0] == r:
            a_ = current_position["top"][0][2]
            b_ = current_position["opposite"][2][2]
            if a_ == b:
                if b_ == y:
                    Bdash()
                    D()
                    B()
                    Ddash()
                    Bdash()
                    D()
                    B()
            elif a_ == y:
                if b_ == g:
                    Bdash()
                    D()
                    B()
                    Ddash()
                    F()
                    D()
                    Fdash()
            elif a_ == g:
                if b_ == w:
                    Bdash()
                    D()
                    B()
                    Fdash()
                    Ddash()
                    Ddash()
                    F()
            else:
                R()
                Ldash()
                D()
                Rdash()
                Ldash()
        elif current_position["right"][0][2] == r:
            a_ = current_position["opposite"][0][2]
            b_ = current_position["bottom"][2][2]
            if a_ == b:
                if b_ == y:
                    Ddash()
                    Bdash()
                    D()
                    B()
            elif a_ == y:
                if b_ == g:
                    Ddash()
                    F()
                    D()
                    Fdash()
            elif a_ == w:
                if b_ == b:
                    Ldash()
                    D()
                    L()
            else:
                D()
                D()
                L()
                D()
                Ldash()
        elif current_position["right"][2][0] == r:
            a_ = current_position["top"][2][2]
            b_ = current_position['front'][0][2]
            if a_ == g:
                if b_ == y:
                    Rdash()
                    Ddash()
                    R()
                    D()
                    Rdash()
                    Ddash()
                    R()
            elif a_ == y:
                if b_ == b:
                    Rdash()
                    Ddash()
                    R()
                    D()
                    D()
                    Bdash()
                    Ddash()
                    B()
            elif a_ == b:
                if b_ == w:
                    R()
                    B()
                    D()
                    D()
                    Bdash()
                    Rdash()
            else:
                R()
                Ldash()
                Ddash()
                Rdash()
                L()
        elif current_position["right"][2][2] == r:
            a_ = current_position["front"][2][2]
            b_ = current_position["bottom"][0][2]
            if a_ == g:
                if b_ == y:
                    D()
                    F()
                    Ddash()
                    Fdash()
            elif a_ == y:
                if b_ == b:
                    D()
                    Bdash()
                    Ddash()
                    B()
            elif a_ == b:
                if b_ == w:
                    B()
                    D()
                    D()
                    Bdash()
            else:
                L()
                Ddash()
                Ldash()
        elif current_position["front"][0][0] == r:
            a_ = current_position["top"][2][0]
            b_ = current_position["left"][2][2]
            if a_ == y:
                if b_ == b:
                    Fdash()
                    R()
                    D()
                    D()
                    Rdash()
                    F()
            elif a_ == g:
                if b_ == y:
                    Fdash()
                    Ddash()
                    F()
                    F()
                    D()
                    D()
                    Fdash()
            elif a_ == w:
                if b_ == g:
                    L()
                    Ddash()
                    Ldash()
                    D()
                    L()
                    Ddash()
                    Ldash()
            elif a_ == b:
                if b_ == w:
                    Fdash()
                    B()
                    Ddash()
                    F()
                    Bdash()
        elif current_position["front"][2][0] == r:
            a_ = current_position["left"][2][0]
            b_ = current_position["bottom"][0][0]
            if a_ == y:
                if b_ == b:
                    R()
                    D()
                    D()
                    Rdash()
            elif a_ == g:
                if b_ == y:
                    D()
                    Rdash()
                    Ddash()
                    R()
            elif a_ == w:
                if b_ == g:
                    D()
                    L()
                    Ddash()
                    Ldash()
            else:
                B()
                Ddash()
                Bdash()
        elif current_position["bottom"][0][0] == r:
            a_ = current_position['front'][2][0]
            b_ = current_position['left'][2][0]
            if a_ == y:
                if b_ == b:
                    R()
                    D()
                    D()
                    Rdash()
                    Bdash()
                    Ddash()
                    B()
                    D()
                    Bdash()
                    Ddash()
                    B()
            elif a_ == g:
                if b_ == y:
                    Rdash()
                    D()
                    R()
                    F()
                    D()
                    Fdash()
                    Ddash()
                    F()
                    D()
                    Fdash()
            elif a_ == w:
                if b_ == g:
                    L()
                    D()
                    D()
                    Ldash()
                    Ddash()
                    L()
                    D()
                    Ldash()
            else:
                Ddash()
                B()
                D()
                D()
                Bdash()
                Ddash()
                B()
                D()
                Bdash()
        elif current_position["bottom"][2][0] == r:
            a_ = current_position["left"][0][0]
            b_ = current_position["opposite"][0][0]
            if a_ == y:
                if b_ == b:
                    Ddash()
                    Bdash()
                    Ddash()
                    Ddash()
                    B()
                    D()
                    Bdash()
                    Ddash()
                    B()
            elif a_ == g:
                if b_ == y:
                    D()
                    D()
                    Rdash()
                    D()
                    D()
                    R()
                    D()
                    Rdash()
                    Ddash()
                    R()
            elif a_ == w:
                if b_ == g:
                    D()
                    L()
                    D()
                    D()
                    Ldash()
                    Ddash()
                    L()
                    D()
                    Ldash()
            else:
                B()
                Ddash()
                Ddash()
                Bdash()
                Ddash()
                B()
                D()
                Bdash()
        elif current_position["opposite"][0][0] == r:
            a_ = current_position["left"][0][0]
            if a_ == b:
                Ddash()
                R()
                D()
                Rdash()
            elif a_ == y:
                Rdash()
                D()
                D()
                R()
            elif a_ == g:
                Fdash()
                D()
                F()
            else:
                Ddash()
                Ldash()
                D()
                L()
        elif current_position["opposite"][2][0] == r:
            a_ = current_position["top"][0][0]
            if a_ == w:
                B()
                D()
                Bdash()
                Ddash()
                B()
                D()
                Bdash()
            elif a_ == b:
                B()
                D()
                Bdash()
                Bdash()
                D()
                D()
                B()
            elif a_ == y:
                B()
                Rdash()
                D()
                D()
                R()
                Bdash()
            else:
                B()
                Fdash()
                D()
                Bdash()
                F()
        elif current_position["left"][0][0] == r:
            a_ = current_position["opposite"][0][0]
            if a_ == y:
                R()
                Ddash()
                Rdash()
            elif a_ == g:
                F()
                D()
                D()
                Fdash()
            elif a_ == w:
                D()
                Fdash()
                Ddash()
                F()
            else:
                D()
                B()
                Ddash()
                Bdash()
        elif current_position["left"][0][2] == r:
            a_ = current_position["top"][0][0]
            if a_ == y:
                R()
                Ldash()
                Ddash()
                Rdash()
                L()
            elif a_ == g:
                Ldash()
                F()
                D()
                D()
                Fdash()
                L()
            elif a_ == w:
                Ldash()
                Ddash()
                L()
                L()
                D()
                D()
                Ldash()
            else:
                Ldash()
                Ddash()
                L()
                D()
                Ldash()
                Ddash()
                L()
        elif current_position["left"][2][0] == r:
            a_ = current_position["front"][2][0]
            if a_ == b:
                Bdash()
                D()
                D()
                B()
            elif a_ == y:
                Rdash()
                D()
                R()
            elif a_ == g:
                Ddash()
                Fdash()
                D()
                F()
            else:
                D()
                Ldash()
                Ddash()
                Ddash()
                L()
        elif current_position["left"][2][2] == r:
            a_ = current_position["top"][2][0]
            if a_ == b:
                L()
                Bdash()
                D()
                D()
                B()
                Ldash()
            elif a_ == y:
                L()
                Rdash()
                D()
                R()
                Ldash()
            elif a_ == g:
                L()
                D()
                Ldash()
                Ddash()
                L()
                D()
                Ldash()
            else:
                L()
                D()
                Ldash()
                Ldash()
                D()
                D()
                L()


def second_algo():
    Ddash()
    Rdash()
    D()
    R()
    turn_cube_to_right()
    D()
    L()
    Ddash()
    Ldash()
    turn_cube_to_left()


def second_reverse_algo():
    D()
    L()
    Ddash()
    Ldash()
    turn_cube_to_left()
    Ddash()
    Rdash()
    D()
    R()
    turn_cube_to_right()


def second_layer():
    middle_pieces = {1: [current_position['front'][2][1], current_position["bottom"][0][1]],
                     2: [current_position["right"][1][2], current_position["bottom"][1][2]],
                     3: [current_position["opposite"][0][1], current_position["bottom"][2][1]],
                     4: [current_position["left"][1][0], current_position["bottom"][1][0]]}
    while current_position['front'][1][0] != g or current_position['front'][1][2] != g or current_position["right"][0][
        1] != y or current_position["right"][2][1] != y or current_position["left"][0][1] != w or \
            current_position["left"][2][1] != w or current_position["opposite"][1][0] != b or \
            current_position["opposite"][1][2] != b:
        for i in middle_pieces:
            if middle_pieces[i][1] != o:
                if middle_pieces[i][0] == g:
                    if i == 2:
                        Ddash()
                    elif i == 3:
                        D()
                        D()
                    elif i == 4:
                        D()
                    if middle_pieces[i][1] == y:
                        second_algo()
                    else:
                        second_reverse_algo()
                    middle_pieces = {1: [current_position['front'][2][1], current_position["bottom"][0][1]],
                                     2: [current_position["right"][1][2], current_position["bottom"][1][2]],
                                     3: [current_position["opposite"][0][1], current_position["bottom"][2][1]],
                                     4: [current_position["left"][1][0], current_position["bottom"][1][0]]}
                elif middle_pieces[i][0] == y:
                    if i == 1:
                        D()
                    elif i == 3:
                        Ddash()
                    elif i == 4:
                        D()
                        D()
                    turn_cube_to_right()
                    if middle_pieces[i][1] == b:
                        second_algo()
                    else:
                        second_reverse_algo()
                    turn_cube_to_left()
                    middle_pieces = {1: [current_position['front'][2][1], current_position["bottom"][0][1]],
                                     2: [current_position["right"][1][2], current_position["bottom"][1][2]],
                                     3: [current_position["opposite"][0][1], current_position["bottom"][2][1]],
                                     4: [current_position["left"][1][0], current_position["bottom"][1][0]]}
                elif middle_pieces[i][0] == b:
                    if i == 1:
                        D()
                        D()
                    elif i == 2:
                        D()
                    elif i == 4:
                        Ddash()
                    turn_cube_to_right()
                    turn_cube_to_right()
                    if middle_pieces[i][1] == w:
                        second_algo()
                    else:
                        second_reverse_algo()
                    turn_cube_to_left()
                    turn_cube_to_left()
                    middle_pieces = {1: [current_position['front'][2][1], current_position["bottom"][0][1]],
                                     2: [current_position["right"][1][2], current_position["bottom"][1][2]],
                                     3: [current_position["opposite"][0][1], current_position["bottom"][2][1]],
                                     4: [current_position["left"][1][0], current_position["bottom"][1][0]]}
                elif middle_pieces[i][0] == w:
                    if i == 1:
                        Ddash()
                    elif i == 2:
                        Ddash()
                        Ddash()
                    elif i == 3:
                        D()
                    turn_cube_to_left()
                    if middle_pieces[i][1] == g:
                        second_algo()
                    else:
                        second_reverse_algo()
                    turn_cube_to_right()
                else:
                    dummy_mids = [current_position['front'][2][1], current_position["bottom"][0][1],
                                  current_position["right"][1][2], current_position["bottom"][1][2],
                                  current_position["opposite"][0][1], current_position["bottom"][2][1],
                                  current_position["left"][1][0], current_position["bottom"][1][0]]
                    x = dummy_mids.count("o")
                    if x == 4:
                        if current_position["front"][1][0] != g:
                            second_reverse_algo()
                        elif current_position["front"][1][2] != g:
                            second_algo()
                        elif current_position["opposite"][1][0] != b:
                            turn_cube_to_right()
                            turn_cube_to_right()
                            second_algo()
                            turn_cube_to_left()
                            turn_cube_to_left()
                        elif current_position["opposite"][1][2] != b:
                            turn_cube_to_right()
                            turn_cube_to_right()
                            second_reverse_algo()
                            turn_cube_to_left()
                            turn_cube_to_left()
                        middle_pieces = {1: [current_position['front'][2][1], current_position["bottom"][0][1]],
                                         2: [current_position["right"][1][2], current_position["bottom"][1][2]],
                                         3: [current_position["opposite"][0][1], current_position["bottom"][2][1]],
                                         4: [current_position["left"][1][0], current_position["bottom"][1][0]]}


def bottom_plus_algo():
    F()
    R()
    U()
    Rdash()
    Udash()
    Fdash()


def bottom_plus():
    flip_top_to_bottom()
    dummy_mids = [current_position["top"][0][1], current_position["top"][1][0], current_position["top"][1][1],
                  current_position["top"][1][2], current_position["top"][2][1]]
    x = dummy_mids.count("o")
    display_cube()
    while x != 5:
        if x == 1:
            bottom_plus_algo()
        else:
            if current_position["top"][0][1] == o and current_position["top"][1][2] == o:
                turn_cube_to_left()
                bottom_plus_algo()
                turn_cube_to_right()
            elif current_position["top"][0][1] == o and current_position["top"][2][1] == o:
                turn_cube_to_left()
                bottom_plus_algo()
                turn_cube_to_right()
            elif current_position["top"][1][2] == o and current_position["top"][2][1] == o:
                turn_cube_to_left()
                turn_cube_to_left()
                bottom_plus_algo()
                turn_cube_to_right()
                turn_cube_to_right()
            elif current_position["top"][2][1] == o and current_position["top"][1][0] == o:
                turn_cube_to_right()
                bottom_plus_algo()
                turn_cube_to_left()
            else:
                bottom_plus_algo()

        dummy_mids = [current_position["top"][0][1], current_position["top"][1][0], current_position["top"][1][1],
                      current_position["top"][1][2], current_position["top"][2][1]]
        x = dummy_mids.count("o")


def captial_t():
    turn_cube_to_right()
    turn_cube_to_right()
    display_cube()
    centers = "gwbyg"
    top_centers = current_position["front"][0][1] + current_position["right"][1][0] + current_position["opposite"][2][
        1] + current_position["left"][1][2] + current_position["front"][0][1]
    x = 0
    des = "no"
    a = ""
    for i in range(len(top_centers) - 1):
        a = top_centers[i] + top_centers[i + 1]
        if a in centers:
            print(a)
            x = top_centers.index(a) - centers.index(a)
            des = "no"
            break
        else:
            x = top_centers.index("g")
            des = "yes"
    if x > 0:
        for j in range(x):
            U()
            display_cube()
    else:
        x = abs(x)
        for j in range(x):
            Udash()
            display_cube()

    top_centers = current_position["front"][0][1] + current_position["right"][1][0] + current_position["opposite"][2][
        1] + current_position["left"][1][2] + current_position["front"][0][1]
    if des == "yes":
        turn_cube_to_right()
        mids_algo()
        Udash()
        turn_cube_to_left()
        mids_algo()
    elif top_centers == centers:
        pass
    else:
        if a[0] == b:
            mids_algo()
        elif a[0] == g:
            turn_cube_to_right()
            turn_cube_to_right()
            mids_algo()
            turn_cube_to_left()
            turn_cube_to_left()
        elif a[0] == w:
            turn_cube_to_left()
            mids_algo()
            turn_cube_to_right()
        else:
            turn_cube_to_right()
            mids_algo()
            turn_cube_to_left()


def last_layer():
    dummy_x = 0
    for i in range(4):
        reference = current_position["top"][1][1] + current_position["front"][1][1] + current_position["left"][1][1] + \
                    current_position["top"][1][1] + current_position["front"][1][1] + current_position["left"][1][1]
        a = current_position["top"][2][0] + current_position["front"][0][0] + current_position["left"][2][2]
        if a not in reference:
            turn_cube_to_right()
            dummy_x += 1
        else:
            break
    if dummy_x == 4:
        R()
        Udash()
        Ldash()
        U()
        Rdash()
        Udash()
        L()
        U()
        for i in range(4):
            reference = current_position["top"][1][1] + current_position["front"][1][1] + current_position["left"][1][
                1] + \
                        current_position["top"][1][1] + current_position["front"][1][1] + current_position["left"][1][1]
            a = current_position["top"][2][0] + current_position["front"][0][0] + current_position["left"][2][2]
            if a not in reference:
                turn_cube_to_right()
                dummy_x += 1
            else:
                break
    a = current_position["top"][2][2] + current_position["front"][0][2] + current_position["right"][2][0]
    display_cube()
    for i in range(4):
        reference = current_position["top"][1][1] + current_position["front"][1][1] + current_position["right"][1][1] + \
                    current_position["top"][1][1] + current_position["front"][1][1] + current_position["right"][1][1]
        if a not in reference:
            R()
            Udash()
            Ldash()
            U()
            Rdash()
            Udash()
            L()
            U()
            a = current_position["top"][2][2] + current_position["front"][0][2] + current_position["right"][2][0]
            display_cube()
    for i in range(4):
        while current_position["top"][2][2] != o:
            Rdash()
            D()
            R()
            Ddash()
        else:
            U()


display_cube()
plus()
mids()
display_cube()
top_layer()
display_cube()
second_layer()
display_cube()
bottom_plus()
display_cube()
captial_t()
display_cube()
last_layer()
display_cube()
print(no_of_moves)
