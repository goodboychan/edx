# -*- coding: utf-8 -*-
"""
Created on Mon May 22 23:05:55 2017

@author: kcsgo
"""

# Video 3.3.2
import numpy as np

p1 = np.array([1, 1])
p2 = np.array([4, 4])

np.sqrt(np.power(p2 - p1, 2))


def distance(p1, p2):
    """
    Find the distance between points p1 and p2.
    """
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

print(distance(p1, p2))

# Video 3.3.3
import random

def majority_vote(votes):
    """
    Return the most common element in votes.
    """
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
                       
    winners = []
    max_count = max(vote_counts.values())               
    for vote, count in vote_counts.items():
        if count == max_count:
            winners.append(vote)
        
    return random.choice(winners)

import scipy.stats as ss

def majority_vote_short(votes):
    """
    Return the most common element in votes.
    """
    mode, count = ss.mstats.mode(votes)
    return mode

votes = [1,2,3,1,2,3,1,2,3,3,3,3]
vote_counts = majority_vote(votes)
vote_counts_short = majority_vote_short(votes)
print(vote_counts)
print(vote_counts_short)

# Video 3.3.4
# for over all points
    # compute the distance between point p and every other point
# sort distances and return those k points that are nearest to point p

import matplotlib.pyplot as plt

def find_nearest_neighbors(p, points, k=5):
    """
    Find the k nearest neighbors of point p and return their indices. 
    """
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]

def knn_predict(p, points, outcomes, k=5):
    """
    Predict class of p based on knn
    """
    # find k nearest neighbors
    ind = find_nearest_neighbors(p, points, k)
    # predict the class of p based on majority vote
    return majority_vote(outcomes[ind])

# Example for kNN 
points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]])
p = np.array([2.5, 2])
plt.plot(points[:, 0], points[:, 1], "ro")
plt.plot(p[0], p[1], "bo")
plt.axis([0.5, 3.5, 0.5, 3.5])
    
# Example for kNN predict
outcomes = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])
knn_predict(np.array([2.5, 2.7]), points, outcomes, k=2)

