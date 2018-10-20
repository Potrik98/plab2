from fsm.utils import is_int
from fsm.FSMController import FSMController


class State:
    def __init__(self, fsm: FSMController):
        self._fsm = fsm

    #
    # Processes the input and returns the next state
    #
    def process_input(self, input: str):
        raise NotImplementedError()


#
# This is the initial sleeping state
#
class SleepingState(State):
    def __init__(self, fsm: FSMController):
        super().__init__(fsm)
        self._fsm.show_shutdown_lights()

    def process_input(self, input: str) -> State:
        # Press any key to wake up
        self._fsm.show_startup_lights()
        return RecieveInputState(self._fsm)


#
# This state is entered after a correct key code is entered
# When in the logged in state, the user can do any action
# identified with a string of numbers.
# To execute an action, type any string of numbers,
# and end with '#' to execute, or '*' (or anything else)
# to abort entering the action identifier.
#
class LoggedInState(State):
    def __init__(self, fsm: FSMController):
        super().__init__(fsm)
        self._actions = {
            '0': SleepingState(fsm),
            '1': GetLedIdState(fsm)
        }
        self._action_identifier = ""

    def process_input(self, input: str) -> State:
        if is_int(input):
            self._action_identifier += input
            return self
        elif input == '#':
            # execute the action with the right identifier
            if self._action_identifier not in self._actions:
                # invalid action, abort
                self._fsm.show_error_lights()
                return LoggedInState(self._fsm)
            else:
                # Go to the action state
                action_state = self._actions[self._action_identifier]
                action_state.__init__(self._fsm)
                return action_state
        else:
            # abort
            return LoggedInState(self._fsm)


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
    def __init__(self, fsm: FSMController, correct_code: str):
        super().__init__(fsm)
        self._correct_code = correct_code
        self._code_so_far = ""
        self._inputs_so_far = 0
        self._code_length = len(self._correct_code)
        self._next_state = LoggedInState(fsm)

    def process_input(self, input: str) -> State:
        if not is_int(input):
            return self  # Ignore any invalid input
        self._code_so_far += input
        self._inputs_so_far += 1
        if self._inputs_so_far == self._code_length:
            # A code of the right length has been inputted
            if self._code_so_far == self._correct_code:
                # Code is correct
                self._fsm.show_passcode_accepted_lights()
                return self._next_state
            else:
                # Code is incorrect, return to the initial state
                self._fsm.show_error_lights()
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
    def __init__(self, fsm: FSMController, correct_code: str):
        super().__init__(fsm, correct_code)
        self._next_state = SetCodeState(fsm, correct_code)


#
# This state tries to change the key code.
# The code must be confirmed afterwards.
#
class ChangeCodeState(State):
    def __init__(self, fsm: FSMController):
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
    def __init__(self, fsm: FSMController, new_code: str):
        super().__init__(fsm)
        fsm.set_correct_code(new_code)

    def process_input(self, input: str) -> State:
        # Returning to the initial state
        return RecieveInputState(self._fsm).process_input(input)


#
# This state gets the led id from input
# in order to set it
#
class GetLedIdState(State):
    def __init__(self, fsm: FSMController):
        super().__init__(fsm)
        self._led_id = ""

    def process_input(self, input: str) -> State:
        if is_int(input):
            # Append the input to the led
            self._led_id += input
            return self
        else:
            # Duration input complete
            # Proceed to the get duration state
            return GetLedDurationState(self._fsm, int(self._led_id))


#
# This state gets the led duration from input
# and sets the led
# The duration is the number of seconds
#
class GetLedDurationState(State):
    def __init__(self, fsm: FSMController, led_id: int):
        super().__init__(fsm)
        self._led_id = led_id
        self._duration = ""

    def process_input(self, input: str) -> State:
        if is_int(input):
            # Append the input to the duration
            self._duration += input
            return self
        else:
            # Duration input complete
            self._fsm.set_led(self._led_id, int(self._duration))
            return LoggedInState(self._fsm)  # Return to the logged in state
