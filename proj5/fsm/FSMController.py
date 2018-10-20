

class FSMController:
    def __init__(self):
        self._correct_code = "666"

    def get_correct_code(self) -> str:
        return self._correct_code

    def set_correct_code(self, code: str) -> None:
        self._correct_code = code

    def set_led(self, led_id: int, duration: int) -> None:
        pass  # TODO: use led controller
