from State import State


class FSM:
    def __init__(self):
        self._state: State
        self._correct_code = "666"

    def get_correct_code(self) -> str:
        return self._correct_code
