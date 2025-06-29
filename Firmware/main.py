import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Tap
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

macros = Macros()
encoder_handler = EncoderHandler()
keyboard.modules = [macros, encoder_handler]

encoder_handler.pins = [(board.GP8, board.GP9, board.GP10)]
Zoom_in = [KC.LCTRL, KC.EQUAL]
Zoom_out = [KC.LCTRL, KC.MINUS]
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),),
    ((Tap(Zoom_out), Tap(Zoom_in), KC.NO),),
    ((KC.A, KC.Z, KC.N1),),
    ((KC.NO, KC.NO, KC.NO),),
]

PINS = [board.D2, board.D1]
keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)

macros.macros = [
    Tap([KC.LCTRL, KC.LEFT]),   # MACRO_0
    Tap([KC.LCTRL, KC.RIGHT]),  # MACRO_1
]

keyboard.keymap = [
    [KC.MACRO_0, KC.SPACE, KC.MACRO_1]
]

if __name__ == '__main__':
    keyboard.go()
