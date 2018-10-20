

class FSMController:
    def __init__(self):
        self._correct_code = "666"
        self._state = None

    def get_correct_code(self) -> str:
        return self._correct_code

    def process_input(self, input: str) -> None:
        self._state = self._state.process_input(input)

    def set_correct_code(self, code: str) -> None:
        self._correct_code = code

    def set_led(self, led_id: int, duration: int) -> None:
        pass  # TODO: use led controller

    def show_startup_lights(self) -> None:
        pass  # TODO

    def show_shutdown_lights(self) -> None:
        pass  # TODO

    def show_passcode_accepted_lights(self) -> None:
        pass  # TODO

    def show_error_lights(self) -> None:
        pass  # TODO
