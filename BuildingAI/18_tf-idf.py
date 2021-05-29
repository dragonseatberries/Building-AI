# tfidf method used to assign reasonable weights on words
import numpy as np
import math
text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

# function that calculates the tfidf vectors for each line in text
# returns a list of vectors


def find_tfidf(text):
    # tasks your code should perform:

    # 1. separate the text into sentences with lower cased words
    docs = [line.lower().split() for line in text.split('\n')]
    # get a list of unique words that appear in it
    vocabulary = list(set(text.split()))
    N = len(docs)

    # 2. go over each unique word and calculate its term frequency, and its document frequency
    tf = {}
    df = {}
    for word in vocabulary:
        tf[word] = [doc.count(word)/len(doc) for doc in docs]
        df[word] = sum([word in doc for doc in docs])/N

    # 3. go over each line in the text and calculate its TF-IDF representation, which will be a vector
    tfidf_data = []
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            if df[word] == 0:
                df[word] = 1
            tfidf.append(tf[word][doc_index] * math.log(1/df[word], 10))
        tfidf_data.append(tfidf)

    print(tfidf_data)

    return tfidf_data

# function that calculates the manhattan distance between tfidf values of vectors for row1 and row2
# returns distance as float


def distance(row1, row2):
    sum = 0
    for ai, bi in zip(row1, row2):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)

# function that calculates the distances between each line, and finds which pair is the closest


def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=float)
    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i][j] = np.inf
            else:
                dist[i][j] = distance(data[i], data[j])
    print(np.unravel_index(np.argmin(dist), (N, N)))


find_nearest_pair(find_tfidf(text))
