from typing import Dict



# Single state class where:
#   trans_func - function to determen the transition due to some logic
#   transitions - array of possible transitions
class State:
    def __init__(self, trans_func, transitions):
        self.trans_func = trans_func
        self.transitions = transitions

    def get_transitions(self):
        return self.transitions

    def next(self):
        return self.trans_func()





# Main fsm class
class FSM:
    def __init__(self, start_state: State, states):
        self.state = start_state
        self.states = states

    def next(self, state: str):
        curr_state = self.states[state]
        next_state = curr_state.next()
        return next_state





# TEST example for constructing/using FSM
def transition_1():
    num = input("State 1, Enter number [1, 2]: ")
    if num == "1":
        return "state_1"
    elif num == "2":
        return "state_2"

state_1 = State(transition_1, {"state_1", "state_2"})


def transition_2():
    num = input("State 2, Enter number [1, 2 ,3]: ")
    if num == "1":
        return "state_1"
    elif num == "2":
        return "state_2"
    elif num == "3":
        return "state_3"

state_2 = State(transition_2, {"state_1", "state_2", "state_3"})


def transition_3():
    num = input("State 3, Enter number [1, 3]: ")
    if num == "1":
        return "state_1"
    elif num == "3":
        return "state_3"

state_3 = State(transition_3, {"state_1", "state_3"})




states = { "state_1": state_1, "state_2": state_2, "state_3": state_3 }

test_fsm = FSM(state_1, states)


next_state = test_fsm.next("state_1")
while True:
    next_state = test_fsm.next(next_state)