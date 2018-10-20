import unittest
from fsm.State import (
    RecieveInputState,
    InputCodeState,
    ChangeCodeState,
    LoggedInState
)
from fsm.FSM import FSM


class StateTest(unittest.TestCase):
    def test_RecieveInputState_number_input(self):
        fsm = FSM()
        state = RecieveInputState(fsm)
        next_state = state.process_input('1')
        self.assertIsInstance(next_state, InputCodeState)

    def test_InputCodeState_correct_code(self):
        fsm = FSM()
        correct_code = "123"
        state = InputCodeState(fsm, correct_code)
        state = state.process_input('1')
        state = state.process_input('2')
        state = state.process_input('3')
        self.assertIsNone(state)  # TODO: Change this to the logged in state

    def test_InputCodeState_incorrect_code(self):
        fsm = FSM()
        correct_code = "123"
        state = InputCodeState(fsm, correct_code)
        state = state.process_input('1')
        state = state.process_input('1')
        state = state.process_input('1')
        self.assertIsInstance(state, RecieveInputState)

    def test_ChangeCodeState_correct_confirmation(self):
        fsm = FSM()
        state = ChangeCodeState(fsm)
        state = state.process_input('4')
        state = state.process_input('5')
        state = state.process_input('6')
        state = state.process_input('#')  # any non-numeric completes the code
        state = state.process_input('4')
        state = state.process_input('5')
        state = state.process_input('6')  # confirm the code
        self.assertEqual("456", fsm.get_correct_code())
        # Check that we returned to the initial state
        next_state = state.process_input('1')
        self.assertIsInstance(next_state, InputCodeState)

    def test_ChangeCodeState_incorrect_confirmation(self):
        fsm = FSM()
        state = ChangeCodeState(fsm)
        state = state.process_input('4')
        state = state.process_input('5')
        state = state.process_input('6')
        state = state.process_input('#')  # any non-numeric completes the code
        state = state.process_input('1')
        state = state.process_input('2')
        state = state.process_input('3')  # incorrect confirmation of the code
        # Incorrect confirmation should return to the initial state
        self.assertIsInstance(state, RecieveInputState)

    def test_LoggedInState_do_action(self):
        fsm = FSM()
        state = LoggedInState(fsm)
        state = state.process_input('0')
        state = state.process_input('#')
        # Action 0 should return to the initial state
        self.assertIsInstance(state, RecieveInputState)

    def test_LoggedInState_abort(self):
        fsm = FSM()
        state = LoggedInState(fsm)
        state = state.process_input('1')
        state = state.process_input('*')  # Abort
        self.assertIsInstance(state, LoggedInState)
        state = state.process_input('0')
        state = state.process_input('#')
        # Action 0 should return to the initial state
        self.assertIsInstance(state, RecieveInputState)

    def test_LoggedInState_invalid_action(self):
        fsm = FSM()
        state = LoggedInState(fsm)
        state = state.process_input('1')
        state = state.process_input('1')
        state = state.process_input('#')  # Abort, invalid action
        self.assertIsInstance(state, LoggedInState)
        state = state.process_input('0')
        state = state.process_input('#')
        # Action 0 should return to the initial state
        self.assertIsInstance(state, RecieveInputState)


if __name__ == '__main__':
    unittest.main()
