# node: <-, ^, ->, v, o
EXP_REWARD = {"s1": 0, "s2": -1, "s3": 0, "s4": 1}
EXP_TRANS = {
    "s1": [None, None, "s2", "s3", "s1"],
    "s2": ["s1", None, None, "s4", "s2"],
    "s3": [None, "s1", "s4", None, "s3"],
    "s4": ["s3", "s2", None, None, "s4"],
}


def state_value(position, policy, gamma=0.9, step=0):
    """
    v = immediate reward + gamma * v'
    :param position:
    :param policy: {pos: a list of possibilities}
    :param gamma:
    :return:
    """
    # immediate_reward
    # if position == "s4":
    #     return 1 / (1 - gamma)
    if step > 900:
        return 0
    returns = 0
    for action, prob in zip(EXP_TRANS[position], policy[position]):
        if prob > 0:
            returns += (EXP_REWARD[action] + gamma * state_value(action, policy, gamma, step + 1)) * prob

    return returns


a_policy = {
    "s1": [0, 0, 0.5, 0.5, 0],
    "s2": [0, 0, 0, 1, 0],
    "s3": [0, 0, 1, 0, 0],
    "s4": [0, 0, 0, 0, 1],
}
state_s1 = state_value("s1", a_policy)
print(state_s1)
state_s2 = state_value("s2", a_policy)
print(state_s2)
state_s3 = state_value("s3", a_policy)
print(state_s3)
state_s4 = state_value("s4", a_policy)
print(state_s4)
