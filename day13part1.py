import numpy as np
from scipy.optimize import linprog

with open("./inputs/13input.txt", "r") as f:
    data = f.read()

coeffs = []
vals = []
for chunk in data.split("\n\n"):
    for line in chunk.splitlines():
        if "Button A:" in line:
            x1, y1 = (
                line
                .replace("Button A: ", "")
                .replace("X+", "")
                .replace("Y+", "")
                .replace(" ", "")
                .split(",")
                      )
        elif "Button B:" in line:
            x2, y2 = (
                line
                .replace("Button B: ", "")
                .replace("X+", "")
                .replace("Y+", "")
                .replace(" ", "")
                .split(",")
                      )
        elif "Prize: " in line:
            x,y = (
                line
                .replace("Prize: ", "")
                .replace("X=", "")
                .replace("Y=", "")
                .replace(" ", "")
                .split(",")
                      )
        else:
            raise ValueError
    coeffs.append(np.array([[int(x1), int(x2)], [int(y1), int(y2)]]))
    vals.append(np.array([int(x),int(y)]))

def has_integer_solution(coeff_matrix, constants):
    det = np.linalg.det(coeff_matrix)
    if det == 0:
        return False

    det = int(round(det))
    mod_solutions = np.linalg.solve(coeff_matrix, constants) % det
    return np.allclose(mod_solutions, np.round(mod_solutions))

def minimizeEq(coeff_matrix, constants):

    A, B = np.linalg.solve(coeff_matrix, constants)

    return ((3 * A) + B)

cost = 0
for co, k in zip(coeffs, vals):
    if has_integer_solution(co, k):
        cost += minimizeEq(co, k)

print(cost)
