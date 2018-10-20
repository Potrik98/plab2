

class FSM:
    def __init__(self):
        self._correct_code = "666"

    def get_correct_code(self) -> str:
        return self._correct_code

    def set_correct_code(self, code: str) -> None:
        self._correct_code = code
