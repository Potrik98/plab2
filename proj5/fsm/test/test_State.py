import unittest
from unittest.mock import patch
from fsm.State import (
    RecieveInputState,
    InputCodeState,
    ChangeCodeState,
    LoggedInState,
    GetLedIdState,
    GetLedDurationState,
    SleepingState
)
from fsm.FSMController import FSMController


class StateTest(unittest.TestCase):
    def test_RecieveInputState_number_input(self):
        fsm = FSMController()
        state = RecieveInputState(fsm)
        next_state = state.process_input('1')
        self.assertIsInstance(next_state, InputCodeState)

    def test_InputCodeState_correct_code(self):
        fsm = FSMController()
        correct_code = "123"
        state = InputCodeState(fsm, correct_code)
        state = state.process_input('1')
        state = state.process_input('2')
        state = state.process_input('3')
        # Correct code input should result in the logged in state
        self.assertIsInstance(state, LoggedInState)

    def test_InputCodeState_incorrect_code(self):
        fsm = FSMController()
        correct_code = "123"
        state = InputCodeState(fsm, correct_code)
        state = state.process_input('1')
        state = state.process_input('1')
        state = state.process_input('1')
        self.assertIsInstance(state, RecieveInputState)

    def test_ChangeCodeState_correct_confirmation(self):
        fsm = FSMController()
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
        fsm = FSMController()
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
        fsm = FSMController()
        state = LoggedInState(fsm)
        state = state.process_input('0')
        state = state.process_input('#')
        # Action 0 should return to the sleeping state
        self.assertIsInstance(state, SleepingState)
        state = LoggedInState(fsm)
        state = state.process_input('1')
        state = state.process_input('#')
        # Action 1 should enter GetLedIdState
        self.assertIsInstance(state, GetLedIdState)

    def test_LoggedInState_abort(self):
        fsm = FSMController()
        state = LoggedInState(fsm)
        state = state.process_input('1')
        state = state.process_input('*')  # Abort
        self.assertIsInstance(state, LoggedInState)
        state = state.process_input('0')
        state = state.process_input('#')
        # Action 0 should return to the sleeping state
        self.assertIsInstance(state, SleepingState)

    def test_LoggedInState_invalid_action(self):
        fsm = FSMController()
        state = LoggedInState(fsm)
        state = state.process_input('1')
        state = state.process_input('1')
        state = state.process_input('#')  # Abort, invalid action
        self.assertIsInstance(state, LoggedInState)
        state = state.process_input('0')
        state = state.process_input('#')
        # Action 0 should return to the sleeping state
        self.assertIsInstance(state, SleepingState)

    def test_login_lights(self):
        fsm = FSMController()
        correct_code = "123"
        state = InputCodeState(fsm, correct_code)
        with patch.object(fsm, 'show_passcode_accepted_lights') as mock:
            state = state.process_input('1')
            state = state.process_input('2')
            state = state.process_input('3')
        mock.assert_called_once_with()

    def test_login_failed_lights(self):
        fsm = FSMController()
        correct_code = "123"
        state = InputCodeState(fsm, correct_code)
        with patch.object(fsm, 'show_error_lights') as mock:
            state = state.process_input('6')
            state = state.process_input('6')
            state = state.process_input('6')
        mock.assert_called_once_with()

    def test_startup_lights(self):
        fsm = FSMController()
        state = SleepingState(fsm)
        with patch.object(fsm, 'show_startup_lights') as mock:
            state = state.process_input('1')
        mock.assert_called_once_with()

    def test_shutdown_lights(self):
        fsm = FSMController()
        state = LoggedInState(fsm)
        with patch.object(fsm, 'show_shutdown_lights') as mock:
            state = state.process_input('0')
            state = state.process_input('#')
        mock.assert_called_once_with()

    def test_led_lights(self):
        fsm = FSMController()
        state = GetLedIdState(fsm)
        with patch.object(fsm, 'set_led') as mock:
            state = state.process_input('1')
            state = state.process_input('#')  # End led id input
            self.assertIsInstance(state, GetLedDurationState)
            self.assertEqual(state._led_id, 1)  # LED id should be 1
            state = state.process_input("5")
            state = state.process_input("#")  # End led duration input
        # set led should be called with id 1 and duration 5
        mock.assert_called_once_with(1, 5)
        # Should return to the logged in state
        self.assertIsInstance(state, LoggedInState)


if __name__ == '__main__':
    unittest.main()
