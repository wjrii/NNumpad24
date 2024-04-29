print("Starting")
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers
from kmk.handlers.sequences import simple_key_sequence
from kmk.handlers.sequences import send_string

from kmk.extensions.lock_status import LockStatus
from kmk.extensions.LED import LED

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP1,board.GP3,board.GP5,board.GP7)
keyboard.row_pins = (board.GP9,board.GP11,board.GP13,board.GP15,board.GP17,board.GP22)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

leds = LED(led_pin=[board.GP25],brightness=0)

class LEDLockStatus(LockStatus):
    def set_lock_leds(self):
        if self.get_num_lock():
            leds.set_brightness(50, leds=[0])
        else:
            leds.set_brightness(0, leds=[0])

    def after_hid_send(self, sandbox):
        super().after_hid_send(sandbox)  # Critically important. Do not forget
        if self.report_updated:
            self.set_lock_leds()

keyboard.extensions.append(leds)
keyboard.extensions.append(LEDLockStatus())

CALCEXE = send_string("calc.exe")
WINCALC = simple_key_sequence(
    (KC.LWIN(KC.R),
    KC.MACRO_SLEEP_MS(200),
    CALCEXE, 
    KC.ENTER,)
)

NLED = simple_key_sequence(
    (KC.NLCK,
    KC.LED_TOG(),)
)

keyboard.keymap = [
    [KC.BKSP,	KC.SPC,		KC.COMM,   	 KC.PMNS,
    KC.NLCK,	KC.PSLS,	KC.PAST,	KC.EQL,
    KC.KP_7,    KC.KP_8,	KC.KP_9,	KC.PPLS,
    KC.KP_4,    KC.KP_5,	KC.KP_6,	KC.PENT,
    KC.DEL,	    KC.KP_1,	KC.KP_2,	KC.KP_3,
    KC.TAB,	    KC.KP_0,	KC.KP_0,	KC.PDOT]
]

if __name__ == '__main__':
    keyboard.go()
