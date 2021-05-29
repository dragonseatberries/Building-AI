# estimating the coeffs using least sum squared difference method
import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500],
              [21, 3, 50, 1, 100],
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200, -50, 5000, 100],
              [2000, -250, -100, 150, 250],
              [3000, -100, -150, 0, 150]])


def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    index = 0  # starting index

    for coeff in c:  # loop through coeff options to see which one is the best
        sse = 0  # sum of squared differences of current coeff

        for xi, yi in zip(X, y):  # for each data point get the prediction value
            prediction = xi @ coeff
            sse += (yi-prediction)**2  # sum squared difference

        if sse < smallest_error:  # update record if current coeff yields a better prediction
            smallest_error = sse
            best_index = index  # keep track of the one yielding the smallest squared error

        index += 1

    print("the best set is set %d" % best_index)


find_best(X, y, c)


# condensed numpy method
x = np.array([
             [25, 2, 50, 1, 500],
             [39, 3, 10, 1, 1000],
             [13, 2, 13, 1, 1000],
             [82, 5, 20, 2, 120],
             [130, 6, 10, 2, 600]
             ])
y = np.array([127900, 222100, 143750, 268000, 460700])

# numpy method fits a linear regression line onto the given input and output of data points and returns the coeffs
c = np.linalg.lstsq(x, y)[0]
print(c)
print(x @ c)
