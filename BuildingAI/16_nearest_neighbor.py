# classifies testing data using knn method
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


# create random data with two classes
X, Y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

# scale the data so that all values are between 0.0 and 1.0
X = MinMaxScaler().fit_transform(X)

# split two data points from the data as test data and
# use the remaining n-2 points as the training data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=2)

# place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# produce line segments that connect the test data points
# to the nearest neighbors for drawing the chart
lines = []


def dist(a, b):  # distance function
    sum = 0
    for ai, bi in zip(a, b):
        sum += (ai - bi)**2
    return np.sqrt(sum)


def main(X_train, X_test, y_train, y_test):
    global y_predict
    global lines
    k = 3  # classify test items based on classes of k nearest neighbors

    # process each of the test data points
    for i, test_item in enumerate(X_test):
        # calculate the distances to all training points using list comprehension
        distances = [dist(train_item, test_item) for train_item in X_train]
        # sort list of distances from nearest to furthest
        nearest_neighbors = np.argsort(distances)
        # create a list with the classes of the k nearest neighbors
        nearest_classes = y_train[nearest_neighbors[:k]]
        # takes a mean of the classes and round, if majority is 1 will round to 1 and viceversa
        y_predict[i] = np.round(np.mean(nearest_classes))
    print(y_predict)


main(X_train, X_test, y_train, y_test)
