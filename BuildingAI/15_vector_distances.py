# nearest neighbor
# treating data points as vectors and finding the distances between data points in order to find the closest neighbor of test data
import numpy as np

x_train = np.random.rand(10, 3)   # generate 10 random vectors of dimension 3
# generate one more random vector of the same dimension
x_test = np.random.rand(3)


def dist(a, b):  # euclidean distance function
    sum = 0
    for ai, bi in zip(a, b):
        sum += (ai - bi)**2
    return np.sqrt(sum)


def nearest(x_train, x_test):
    nearest = 0
    min_distance = np.Inf

    for i in range(len(x_train)):  # loop through all vectors and finds the closest neighbor
        distance = dist(x_train[i], x_test)
        if distance < min_distance:
            min_distance = distance
            nearest = i
    print(nearest)


nearest(x_train, x_test)

# numpy method #############################################

x_train = np.array([[25, 2, 50, 1, 500],
                    [39, 3, 10, 1, 1000],
                    [82, 5, 20, 2, 120],
                    [130, 6, 10, 2, 600]])
y_train = [127900, 222100,  268000, 460700]

x_test = np.array([[115, 6, 10, 1, 560], [13, 2, 13, 1, 1000]])


def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum += (ai - bi)**2
    return np.sqrt(sum)


n_train = len(x_train)  # number of data points in the training set

for test_item in x_test:
    # d will hold the distances between this test data point and all the training data points
    d = np.empty(n_train)
    for i, train_item in enumerate(x_train):
        d[i] = dist(test_item, train_item)
    # the nearest neighbour will be in y_train[nearest]
    nearest_index = np.argmin(d)
    print(y_train[nearest_index])
