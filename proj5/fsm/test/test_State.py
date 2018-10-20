import unittest
from fsm.State import RecieveInputState, InputCodeState
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


if __name__ == '__main__':
    unittest.main()
