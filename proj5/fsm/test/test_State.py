import unittest
from fsm.State import RecieveInputState, InputCodeState
from fsm.FSM import FSM


class StateTest(unittest.TestCase):
    def test_RecieveInputState(self):
        fsm = FSM()
        state = RecieveInputState(fsm)
        next_state = state.process_input('1')
        self.assertIsInstance(next_state, InputCodeState)


if __name__ == '__main__':
    unittest.main()
