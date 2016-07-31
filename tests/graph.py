
import math
import heapq
import random

def gaussCluster(center, stdDev, count=50):
    return [(random.gauss(center[0], stdDev),
             random.gauss(center[1], stdDev),
             random.gauss(center[2], stdDev)) for _ in range(count)]

def makeDummyData():
    return gaussCluster((-4,0,0), 1) + gaussCluster((4,0,0), 1)


class KNNGraph():
    def __init__(self, n_neighbors=10):
        self.n_neighbors = n_neighbors

    def set_n_neighbors(self, n_neighbors=10):
        if n_neighbors < 1:
            raise Exception('the value for n_neighbors should be bigger than zero')
        self.n_neighbors = n_neighbors

    def calc_distance(self, node, data, labels, n_neighbors=None, dist_type='euclidean'):

        def euclidean_distance(x,y):
            return math.sqrt(sum([(a-b)**2 for (a,b) in zip(x,y)]))

        def jaccard_distance(x,y,weighted=True):
            x = [round(_,2) for _ in x]
            y = [round(_,2) for _ in y]
            set1, set2 = set(x), set(y)
            if not sum(set1) or not sum(set2):
                return 0
            if weighted:
                intersection = set1 & set2
                union = set1 | set2
                return 1 - sum(intersection) / float(sum(union))
            else:
                return 1 - len(set1 & set2) / float(len(set1 | set2))
                # return 1 - sum([min(a,b) for (a,b) in zip(x,y)]) / sum([max(a,b) for (a,b) in zip(x,y)])

        def cosine_distance(x,y):
            return 1 - float(sum([a*b for (a,b) in zip(x,y)])) / (math.sqrt(sum([_**2 for _ in x])) * math.sqrt(sum([_**2 for _ in y])))

        def knn(data, labels, k, distance):
            def nn(x):
                # get k nearest neighbors (itself included)
                closestPoints = heapq.nsmallest(k, enumerate(data), key=lambda y: distance(x, y[1]))

                # load distance
                closestPoints = [(node_id, distance(x, vector)) for node_id, vector in closestPoints]

                # normalize, and weighed (1-)
                sum_values = sum([_[1] for _ in closestPoints])
                closestPoints = [(node_id, 1-float(dis)/sum_values) for node_id, dis in closestPoints]
                return closestPoints

            return nn
        if not n_neighbors:
            n_neighbors = self.n_neighbors
        n_neighbors += 1 # not including itself

        nn = knn(data, labels, n_neighbors, euclidean_distance)
        print nn(node)[1:]
        nn = knn(data, labels, n_neighbors, jaccard_distance)
        print nn(node)[1:]
        nn = knn(data, labels, n_neighbors, cosine_distance)
        print nn(node)[1:]

        return nn(node)[1:]

if __name__ == "__main__":
   import sys

   k = sys.argv[1] if len(sys.argv) == 2 else 8

   trainingPoints = makeDummyData() # has 50 points from each class
   trainingLabels = [1] * 50 + [2] * 50  # an arbitrary choice of labeling

   knn = KNNGraph(n_neighbors=10)
   node = trainingPoints[0]
   # print node
   ans = knn.calc_distance(node, trainingPoints, trainingLabels)

print 0.
print .0

"""
# min_values, max_values = [], []
# for (a,b) in zip(x,y):
#     min_values.append(min(a,b))
#     max_values.append(max(a,b))
# return 1 - sum(min_values)/sum(max_values)
"""
