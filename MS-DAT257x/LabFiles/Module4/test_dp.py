# test_dp.py - a set of functions for testing Dynamic Programming algorithms
import gridworld_mdp as gw 

def error(msg):
    print("ERROR: " + msg)

def passed(msg):
    print("passed test: " + msg)

def get_equiprobable_policy_actions(state):
    tuples = [("up", .25), ("down", .25), ("left", .25), ("right", .25)]
    return tuples

def find_rounded_diffs(v, vexpect):
    diffs = 0
    first_diff_index = -1
    for i in range(len(vexpect)):
        diff = abs(round(vexpect[i]) - round(v[i]))

        if diff > 0:       
            #print("DIFF=", diff, ", i=", i, ", vexpect[i]=", vexpect[i], ", v[i]=", v[i])
            if (first_diff_index == -1):
                first_diff_index = i
            diffs += 1

    return (diffs, first_diff_index)

def find_exact_diffs(v, vexpect):
    diff_count = 0
    first_diff_index = -1
    for i in range(len(vexpect)):
        ve = vexpect[i]
        val = v[i]

        if isinstance(ve, tuple):
            diff = (not (val in ve))
        else:
            diff = (val != ve)

        if diff:      
            #print("DIFF=", diff, ", i=", i, ", vexpect[i]=", ve, ", v[i]=", val)
            if (first_diff_index == -1):
                first_diff_index = i
            diff_count += 1

    return (diff_count, first_diff_index)

def policy_eval_core_test(eval_func, variant):
    print()
    print("Testing: Policy Evaluation (" + variant + ")")

    vexpect = [0, -14, -20, -22, -14, -18, -20, -20, -20, -20, -18, -14, -22, -20, -14]
    
    state_count = len(vexpect)
    #actions=["left", "right", "up", "down"]
    gamma = 1
    theta=.0001

    v = eval_func(state_count, gamma, theta, get_equiprobable_policy_actions, gw.get_transitions)

    # 1. check type of result
    if (not isinstance(v, list)):
        error("return value is not a list")
        return
    passed("return value is list")
    
    # 2. check length of list
    if (len(v) != len(vexpect)):
        error("length of  list is neq " + str(len(vexpect)))
        return
    passed("length of list = " + str(len(vexpect)))
    
    # 3. check value of elements (compared to 2 decimal places)
    diffs, first_diff_index = find_rounded_diffs(v, vexpect)

    if diffs > 0:
        error("list elements don't match expected values: # of mismatches=" + str(diffs))
        return
    passed("values of list elements")

    # 4. generate a pass code from fractional part of values
    pass_code = str(abs(int(10000000*(v[5] - int(v[5])))))
    pass_code = pass_code[:4] + "-" + pass_code[4:]
    print("PASSED: Policy Evaluation (" + variant + ") passcode = " + pass_code)

def policy_eval_two_arrays_test(eval_func):
    return policy_eval_core_test(eval_func, "two-arrays")

def policy_eval_in_place_test(eval_func):
    return policy_eval_core_test(eval_func, "in-place")

def policy_iteration_core_test(eval_func, name, passcode_index):
    print()
    print("Testing: " + name)

    vexpect =  [0, -1, -2, -3, -1, -2, -3, -2, -2, -3, -2, -1, -3, -2, -1]

    # piexpect is the optimal policy for our Gridworld (tuples represnt ties / equal actions)
    piexpect = [
        ("left", "up", "right","down"), "left", "left", ("left", "down"),     # first row (states 0-3)
        "up", ("left", "up"), ("left", "up", "right", "down"), "down",    # second row (states 4-7)
        "up", ("left", "up", "right", "down"), ("down", "right"), "down",    # third row (states 8-11)
        ("up", "right"), "right", "right"]                          # forth row (states 12-14)

    state_count = len(vexpect)
    actions=["left", "right", "up", "down"]
    gamma = .999
    theta=.0001

    result = eval_func(state_count, gamma, theta, gw.get_available_actions, gw.get_transitions)

    # 1. check type of result
    if (not isinstance(result, tuple)):
        error("return value is not a tuple")
        return
    passed("return value is tuple")
    
    # 2. check len of result
    if (len(result) != 2):
        error("length of tuple is neq 2")
        return
    passed("length of tuple = 2")

    # split results into variables
    v, pi = result

    # 3. check type/length of v
    if (not isinstance(v, list)) or (len(v) != state_count):
        error("v is not a list of length=" + str(state_count))
        return
    passed("v is list of length=" + str(state_count))

    #riv = [round(iv) for iv in v]
    #print("riv=", riv)

    # 4. check value of elements of v
    diffs, first_diff_index = find_rounded_diffs(v, vexpect)

    if diffs > 0:
        error("v elements don't match expected values: # of mismatches=" + str(diffs))
        return
    passed("values of v elements")

    # 5. check type/length of pi
    if (not isinstance(pi, list)) or (len(pi) != state_count):
        error("pi is not a list of length=" + str(state_count))
        return
    passed("pi is list of length=" + str(state_count))
    
    #print("pi=", pi)

    # 6. check value of elements of pi
    diffs, first_diff_index = find_exact_diffs(pi, piexpect)

    if diffs > 0:
        error("pi elements don't match expected values: # of mismatches=" + str(diffs))
        return
    passed("values of pi elements")

    # 7. generate a pass code from fractional part of values
    pass_value = v[passcode_index]
    pass_code = str(abs(int(10000000*(pass_value - int(pass_value)))))
    pass_code = pass_code[:4] + "-" + pass_code[4:]
    print("PASSED: " + name + " passcode = " + pass_code)
    
def policy_iteration_test(eval_func):
    return policy_iteration_core_test(eval_func, "Policy Iteration", 3)

def value_iteration_test(eval_func):
    return policy_iteration_core_test(eval_func, "Value Iteration", 5)

