import numpy as np


def calculate(arr):
    if len(arr) != 9:
        return -1
    calculations = {}
    matrix = np.array(arr).reshape(3, 3)
    calculations["mean"] = [
        list(np.mean(matrix, axis=0)),
        list(np.mean(matrix, axis=1)),
        np.mean(matrix)
    ]
    calculations["variance"] = [
        list(np.var(matrix, axis=0)),
        list(np.var(matrix, axis=1)),
        np.var(matrix)
    ]
    calculations["standard deviation"] = [
        list(np.std(matrix, axis=0)),
        list(np.std(matrix, axis=1)),
        np.std(matrix)
    ]
    calculations["max"] = [
        list(np.max(matrix, axis=0)),
        list(np.max(matrix, axis=1)),
        np.max(matrix)
    ]
    calculations["min"] = [
        list(np.min(matrix, axis=0)),
        list(np.min(matrix, axis=1)),
        np.min(matrix)
    ]
    calculations["sum"] = [
        list(np.sum(matrix, axis=0)),
        list(np.sum(matrix, axis=1)),
        np.sum(matrix)
    ]
    return calculations
