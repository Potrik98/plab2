from LedController import LedController


class FSMController:
    def __init__(self):
        self._correct_code = "666"
        self._state = None
        self._led_controller = LedController()

    def set_state(self, state) -> None:
        self._state = state

    def get_correct_code(self) -> str:
        return self._correct_code

    def process_input(self, input: str) -> None:
        self._state = self._state.process_input(input)

    def set_correct_code(self, code: str) -> None:
        self._correct_code = code

    def set_led(self, led_id: int, duration: int) -> None:
        self._led_controller.set_led_duration(led_id, duration)

    def show_startup_lights(self) -> None:
        self._led_controller.power_up_leds(1.0)

    def show_shutdown_lights(self) -> None:
        self._led_controller.power_down_leds(1.0)

    def show_passcode_accepted_lights(self) -> None:
        self._led_controller.twinkle_all_leds(3, 0.4)

    def show_error_lights(self) -> None:
        pass  # TODO
