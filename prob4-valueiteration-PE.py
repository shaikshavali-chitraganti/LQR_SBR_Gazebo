import numpy as np

Va = np.zeros([4, 4])

r = -1
gamma = 1
P = {"R": 0.25, "L": 0.25, "U": 0.25, "D": 0.25}


def update_grid_value(i, j, V):
    if (i == 0) and (1 <= j <= 2):
        return P["R"] * (r + gamma * V[i, j + 1]) + P["L"] * (r + gamma * V[i, j - 1]) + P["U"] * (
                r + gamma * V[i, j]) + P["D"] * (r + gamma * V[i + 1, j])
    elif (i == 0) and (j == 3):
        return P["R"] * (r + gamma * V[i, j]) + P["L"] * (r + gamma * V[i, j - 1]) + P["U"] * (r + gamma * V[i, j]) + P[
            "D"] * (r + gamma * V[i + 1, j])
    elif (i == 3) and (j == 0):
        return P["R"] * (r + gamma * V[i, j + 1]) + P["L"] * (r + gamma * V[i, j]) + P["U"] * (
                    r + gamma * V[i - 1, j]) + P["D"] * (r + gamma * V[i, j])
    elif (i == 3) and (1 <= j <= 2):
        return P["R"] * (r + gamma * V[i, j + 1]) + P["L"] * (r + gamma * V[i, j - 1]) + P["U"] * (
                r + gamma * V[i - 1, j]) + P["D"] * (r + gamma * V[i, j])
    elif (j == 0) and (1 <= i <= 2):
        return P["R"] * (r + gamma * V[i, j + 1]) + P["L"] * (r + gamma * V[i, j]) + P["U"] * (
                r + gamma * V[i - 1, j]) + P["D"] * (r + gamma * V[i + 1, j])
    elif (j == 3) and (1 <= i <= 2):
        return P["R"] * (r + gamma * V[i, j]) + P["L"] * (r + gamma * V[i, j - 1]) + P["U"] * (
                r + gamma * V[i - 1, j]) + P["D"] * (r + gamma * V[i + 1, j])
    elif (1 <= i <= 2) and (1 <= j <= 2):
        return P["R"] * (r + gamma * V[i, j + 1]) + P["L"] * (r + gamma * V[i, j - 1]) + P["U"] * (
                r + gamma * V[i - 1, j]) + P["D"] * (r + gamma * V[i + 1, j])
    elif ((i == 0) and (j == 0)) or ((i == 3) and (j == 3)):
        return 0


# print(V)
def value_iteration(X):
    Vt = np.copy(X)
    for i in range(len(X)):
        for j in range(len(X)):
            Vt[i, j] = update_grid_value(i, j, X)
    return Vt


for m in range(100):
    Vtemp = value_iteration(Va)
    print(Vtemp)
    Va = Vtemp
