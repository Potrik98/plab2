def init_passcode_entry():
    # Sett state til 1
    return 1


def light_one_led(lednum, duration):
    return 1


def flash_leds():
    for n in range(6):
        light_one_led(n, 0.1)

def twinkle_leds():

