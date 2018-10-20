class State:
    #
    # Processes the input and returns the next state
    #
    def process_input(self, input: str) -> State:
        raise NotImplementedError


class FSM:
    def __init__(self):
        self._state: State
