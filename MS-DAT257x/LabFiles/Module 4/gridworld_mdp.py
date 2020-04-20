# gridworkd_mdp.py - provides a full MDP specification for a 4x4 gridworld. 
# The Gridworld has a "single goal state", located in the upper/left and lower/right corners 
# of the grid.

def get_state_count():
    return 15

def get_available_actions(state):
    actions = ["up", "down", "left", "right"]
    return actions

def get_transitions(state, action):
    next_state_num = next_state[(state, action)]
    reward = 0 if state == 0 else -1
    prob = 1
    trans = (next_state_num, reward, prob)
    return [trans]
    
def build_next_state_dictionary():
    next_state = {}
    next_state[(0, "left")] = 0
    next_state[(0, "up")] = 0
    next_state[(0, "right")] = 0
    next_state[(0, "down")] = 0

    next_state[(1, "left")] = 0
    next_state[(1, "up")] = 1
    next_state[(1, "right")] = 2
    next_state[(1, "down")] = 5

    next_state[(2, "left")] = 1
    next_state[(2, "up")] = 2
    next_state[(2, "right")] = 3
    next_state[(2, "down")] = 6

    next_state[(3, "left")] = 2
    next_state[(3, "up")] = 3
    next_state[(3, "right")] = 3
    next_state[(3, "down")] = 7

    next_state[(4, "left")] = 4
    next_state[(4, "up")] = 0
    next_state[(4, "right")] = 5
    next_state[(4, "down")] = 8

    next_state[(5, "left")] = 4
    next_state[(5, "up")] = 1
    next_state[(5, "right")] = 6
    next_state[(5, "down")] = 9

    next_state[(6, "left")] = 5
    next_state[(6, "up")] = 2
    next_state[(6, "right")] = 7
    next_state[(6, "down")] = 10

    next_state[(7, "left")] = 6
    next_state[(7, "up")] = 3
    next_state[(7, "right")] = 7
    next_state[(7, "down")] = 11

    next_state[(8, "left")] = 8
    next_state[(8, "up")] = 4
    next_state[(8, "right")] = 9
    next_state[(8, "down")] = 12

    next_state[(9, "left")] = 8
    next_state[(9, "up")] = 5
    next_state[(9, "right")] = 10
    next_state[(9, "down")] = 13

    next_state[(10, "left")] = 9
    next_state[(10, "up")] = 6
    next_state[(10, "right")] = 11
    next_state[(10, "down")] = 14

    next_state[(11, "left")] = 10
    next_state[(11, "up")] = 7
    next_state[(11, "right")] = 11
    next_state[(11, "down")] = 0

    next_state[(12, "left")] = 12
    next_state[(12, "up")] = 8
    next_state[(12, "right")] = 13
    next_state[(12, "down")] = 12

    next_state[(13, "left")] = 12
    next_state[(13, "up")] = 9
    next_state[(13, "right")] = 14
    next_state[(13, "down")] = 13

    next_state[(14, "left")] = 13
    next_state[(14, "up")] = 10
    next_state[(14, "right")] = 0
    next_state[(14, "down")] = 14

    return next_state

# main code
next_state = build_next_state_dictionary()
