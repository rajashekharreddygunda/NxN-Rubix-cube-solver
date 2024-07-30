# NxN-Rubix-cube-solver
The algorithm theoretically solves a Rubix cube of any size. For the sake of simplicity i have made the code to choose a random value ranging between 3 and 30 as the size of the cube, generate a solved cube of that size, scramble it and then solve it. If someone wants give the size by themselves then change """ state, N = splitter(solved_state(random.randint(3, 30))) to state, N = splitter(solved_state(size))"""
[line number 3100 or so] Or if someone wants to give the state of the cube to the algorithm then change """state, N = splitter(solved_state(random.randint(3, 30))) to state, N = splitter(your_state)""".
Here are the instructions to give your_state.
1. your_state is a string and each character in your_state should be the first letter of the color of the piece.
2. In case of an odd sized cube like 3x3 place blue centered face facing the top and red centered face facing you and give the values starting from row 1 till the end of the face.
3. In case of an even sized cube do the same but choose any arbitary face.
4. Flip the blue-centered/top face opposite to you such that red-centered/front face becomes the top face and give the values.
5. Flip the red-centered/top face towards the right of you such that the white-centered/left face becomes the top face and give the values.
6. Flip the white-centered/top face towards the right of you such that the yellow-centered/bottom face becomes the top face and give the values.
7. Flip the yellow-centered/top face towards the right of you and then flip the current top face opposite to you such that green-centered/front face becomes the top face and give the values.
8. Flip the green-centered/top face opposite to you such that orange-centered/front face becomes the top face and give the values.
