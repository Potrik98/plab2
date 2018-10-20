from utils import is_int
from FSM import FSM


class State:
    def __init__(self, fsm: FSM):
        self._fsm = FSM

    #
    # Processes the input and returns the next state
    #
    def process_input(self, input: str):
        raise NotImplementedError()


#
# This state is the initial state of the fsm,
# and will transition to the other states on input
#
class RecieveInputState(State):
    def process_input(self, input: str) -> State:
        if is_int(str):
            # If a number key is pressed, start code input
            input_code_state = InputCodeState(self._fsm.get_correct_code())
            input_code_state.process_input(input)  # process the first digit
            return input_code_state


#
# This state handles input of the key code,
# and will wait until a complete code is inputted
# before checking it
#
class InputCodeState(State):
    def __init__(self, fsm: FSM, correct_code="000"):
        super().__init__(fsm)
        self._correct_code = correct_code
        self._code_so_far = ""
        self._inputs_so_far = 0
        self._code_length = len(self._correct_code)

    def process_input(self, input: str) -> State:
        if not is_int(str):
            return self  # Ignore any invalid input
        self._code_so_far += input
        self._inputs_so_far += 1
        if self._inputs_so_far == self._code_length:
            # A code of the right length has been inputted
            if self._code_so_far == self._correct_code:
                # Code is correct
                pass  # TODO: return next state
            else:
                # Code is incorrect, return to the initial state
                return RecieveInputState(self._fsm)
        else:
            # Code hasn't been completed yet,
            # stay in the same state
            return self
