# using nearest neighbor method on text
import numpy as np

# occurence of words stored in 2D array. each row is a sentence
# each cell a word
data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]


def distance(row1, row2):
    # return the sum of differences between the occurrences of each word in row1 and row2.
    sumdiff = 0.0
    for a, b in zip(row1, row2):
        sumdiff += abs(a-b)
    return sumdiff


def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    # for each line of data we can compare N other lines
    # elements at positions [i, j] where i = j we have 0 as the line is compared against itself
    # to avoid this, an infinite value is assigned at those positions
    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i][j] = np.inf
            else:
                dist[i][j] = distance(data[i], data[j])

    print(np.unravel_index(np.argmin(dist), (N, N)))


find_nearest_pair(data)
