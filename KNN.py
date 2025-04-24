import math
from collections import Counter
data = [
    ((160, 2), "apple"),
    ((170, 6), "banana"),
    ((180, 8), "banana"),
    ((210, 7), "apple"),
    ((120, 6), "banana"),
    ((210, 4), "apple"),
    ((130, 10), "banana"),  
    ((230, 1), "apple"),
] 
def euclidian_distance(point1, point2):
    #d = sqrt((x2-x1)^2 + (y2-y1)^2)
    # where (x1, y1) and (x2, y2) are the coordinates of the two points in the 2D space
    # point1 and point2 are tuples representing the coordinates of the two points
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
def knn(new_point, k):
    distances = []
    for features, point in data:
        distance = euclidian_distance(features, new_point)
        distances.append((distance, point))

    distances.sort()

    neighbors = [label for _, label in distances[:k]] 
    vote = Counter(neighbors)
    print(f"Votes: {vote}")
    most_common = vote.most_common(1)[0][0]
    print(f"Most common label:",{most_common} )
    print(f"The most common label among the {k} nearest neighbors is: {most_common}") 

    return most_common

new_point = (190, 8)
k = 3
neighbors =  knn(new_point, k)


