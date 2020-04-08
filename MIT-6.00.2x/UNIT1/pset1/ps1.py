###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Previously, I implemented it with dictionary sort. It works fine in py3.6+.
    # cows_sorted = {k: v for k, v in sorted(cows.items(), key=lambda item: item[1], reverse=True)}
    # spaceships = []
    
    # while len(cows_sorted) != 0:
    #     spaceship = []
    #     spaceshipWeight = 0.0
    #     for k in cows_sorted.keys():
    #         if spaceshipWeight + cows_sorted[k] <= limit:
    #             spaceship.append(k)
    #             spaceshipWeight += cows_sorted[k]
    #     for e in spaceship:
    #         del cows_sorted[e]
    #     spaceships.append(spaceship)
    
    # return spaceships

    # But in py3.5, it needs to consider dictionary ordering
    cows_sorted = sorted(cows.items(), key=lambda item: item[1], reverse=True)
    spaceships = []
    while len(cows_sorted) != 0:
        spaceship = []
        remove_list = []
        spaceshipWeight = 0.0
        for i in range(len(cows_sorted)):
            if spaceshipWeight + cows_sorted[i][1] <= limit:
                spaceship.append(cows_sorted[i][0])
                spaceshipWeight += cows_sorted[i][1]
                remove_list.append(i)        
        for j in sorted(remove_list, reverse=True):
            cows_sorted.pop(j)
        spaceships.append(spaceship)
    
    return spaceships


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    for partition in get_partitions(cows):
        count = 0
        for i in range(len(partition)):
            spaceshipWeight = 0.0
            for j in range(len(partition[i])):
                spaceshipWeight += cows[partition[i][j]]
            if spaceshipWeight > limit:
                break
            else:
                count += 1
        if count == len(partition):
            return partition

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)

# print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))

# Test 1
# print(greedy_cow_transport({'MooMoo': 85, 'Louis': 45, 'Clover': 5, 'Miss Bella': 15, 'Muscles': 65, 'Milkshake': 75, 'Patches': 60, 'Horns': 50, 'Polaris': 20, 'Lotus': 10}, 100))
# # Test 2
# print(greedy_cow_transport({'Coco': 10, 'Rose': 50, 'Buttercup': 72, 'Betsy': 65, 'Daisy': 50, 'Patches': 12, 'Abby': 38, 'Lilly': 24, 'Willow': 35, 'Dottie': 85}, 100))
# # Test 3
# print(greedy_cow_transport({'Starlight': 54, 'Rose': 42, 'Buttercup': 11, 'Betsy': 39, 'Abby': 28, 'Luna': 41, 'Willow': 59, 'Coco': 59}, 120))

# Test 1
print(brute_force_cow_transport({'Milkshake': 40, 'Miss Bella': 25, 'Lotus': 40, 'Boo': 20, 'Horns': 25, 'MooMoo': 50}, 100))

# Test 2
print(brute_force_cow_transport({'Buttercup': 72, 'Daisy': 50, 'Betsy': 65}, 75))

# Test 3
print(brute_force_cow_transport({'Starlight': 54, 'Buttercup': 11, 'Luna': 41, 'Betsy': 39}, 145))