from fsm.FSMController import FSMController
from fsm.State import SleepingState
from Keypad import Keypad


class KPC:
    def __init__(self):
        self._fsm = FSMController()
        self._fsm.set_state(SleepingState(self._fsm))
        self._fsm.set_correct_code("0000")
        self._running = False
        self._keypad = Keypad()

    def _main_loop(self):
        while self._running:
            input = self._keypad.wait_for_next_signal()
            self._fsm.process_input(input)

    def start(self):
        self._running = True
        self._main_loop()


if __name__ == '__main__':
    kpc = KPC()
    kpc.start()
