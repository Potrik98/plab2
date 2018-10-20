from fsm.utils import is_int
from fsm.FSM import FSM


class State:
    def __init__(self, fsm: FSM):
        self._fsm = fsm

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
        if is_int(input):
            # If a number key is pressed, start code input
            input_code_state = InputCodeState(self._fsm,
                                              self._fsm.get_correct_code())
            input_code_state.process_input(input)  # process the first digit
            return input_code_state


#
# This state handles input of the key code,
# and will wait until a complete code is inputted
# before checking it
#
class InputCodeState(State):
    def __init__(self, fsm: FSM, correct_code: str):
        super().__init__(fsm)
        self._correct_code = correct_code
        self._code_so_far = ""
        self._inputs_so_far = 0
        self._code_length = len(self._correct_code)
        self._next_state = None  # TODO: change this to the next state

    def process_input(self, input: str) -> State:
        if not is_int(input):
            return self  # Ignore any invalid input
        self._code_so_far += input
        self._inputs_so_far += 1
        if self._inputs_so_far == self._code_length:
            # A code of the right length has been inputted
            if self._code_so_far == self._correct_code:
                # Code is correct
                return self._next_state
            else:
                # Code is incorrect, return to the initial state
                return RecieveInputState(self._fsm)
        else:
            # Code hasn't been completed yet,
            # stay in the same state
            return self


#
# This state confirms the code after a code change
# Extending InputCodeState ensures that the inputted
# confirmation of the code is correct.
# By making the next state SetCodeState, the code
# will be changed if the confirmation is correct,
# else we will return to the initial state if incorrect.
#
class ConfirmCodeState(InputCodeState):
    def __init__(self, fsm: FSM, correct_code: str):
        super().__init__(fsm, correct_code)
        self._next_state = SetCodeState(fsm, correct_code)


#
# This state tries to change the key code.
# The code must be confirmed afterwards.
#
class ChangeCodeState(State):
    def __init__(self, fsm: FSM):
        super().__init__(fsm)
        self._code_so_far = ""
        self._parent = ChangeCodeState

    def process_input(self, input: str) -> State:
        if is_int(input):
            # Add any number of inputted numbers to the code
            self._code_so_far += input
            return self
        else:
            # Any non numeric input terminates the code input
            # Enter the confirm code state.
            return ConfirmCodeState(self._fsm, self._code_so_far)


#
# This state applies the change of the key code
# and returns to the initial state
#
class SetCodeState(State):
    def __init__(self, fsm: FSM, new_code: str):
        super().__init__(fsm)
        fsm.set_correct_code(new_code)

    def process_input(self, input: str) -> State:
        # Returning to the initial state
        return RecieveInputState(self._fsm).process_input(input)
