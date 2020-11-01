#!/bin/bash

# python runtext.py --led-multiplexing=1 --led-chain=2 --led-cols=64 --led-no-hardware-pulse 1 -r 16 -t "2 Mugs - 10:30"
#
# python pulsing-colors.py --led-no-hardware-pulse 1 -r 32
# python pulsing-brightness.py --led-no-hardware-pulse 1 -r 32
#
# python graphics.py --led-no-hardware-pulse 1 -r 16 --led-gpio-mapping=adafruit-hat
# python grayscale-block.py --led-no-hardware-pulse 1 -r 32
#
# python image-draw.py --led-no-hardware-pulse -r 32
# python image-scroller.py --led-no-hardware-pulse 1 -r 16
# python rotating-block-generator.py --led-multiplexing=1 --led-brightness=10 --led-gpio-mapping=adafruit-hat --led-chain=2 --led-no-hardware-pulse 1 --led-cols=32
# python simple-square.py --led-no-hardware-pulse 1 -r 16  --led-gpio-mapping=adafruit-hat
# python kit.py --led-no-hardware-pulse 1 -r 16
# python mario_hatday.py --led-multiplexing=1 --led-brightness=30 --led-gpio-mapping=adafruit-hat --led-chain=2 --led-no-hardware-pulse 1 --led-cols=32
# python horizontal-lines.py --led-multiplexing=1 --led-brightness=30 --led-gpio-mapping=adafruit-hat --led-chain=2 --led-no-hardware-pulse 1 --led-cols=32
# python cat_in_hat.py --led-multiplexing=1 --led-brightness=20 --led-gpio-mapping=adafruit-hat --led-chain=2 --led-no-hardware-pulse 1 --led-cols=32
#  python gol-acorn.py --led-multiplexing=1 --led-brightness=10 --led-gpio-mapping=adafruit-hat --led-chain=2 --led-no-hardware-pulse 1 --led-cols=32
# python gol-random.py --led-multiplexing=1 --led-brightness=10 --led-gpio-mapping=adafruit-hat --led-chain=2 --led-no-hardware-pulse 1 --led-cols=32
# python cono-keyboard.py --led-multiplexing=1 --led-brightness=10 --led-gpio-mapping=adafruit-hat --led-chain=2 --led-no-hardware-pulse 1 --led-cols=32
# python gol-gosper-gun.py --led-multiplexing=1 --led-brightness=10 --led-gpio-mapping=adafruit-hat --led-chain=2 --led-no-hardware-pulse 1 --led-cols=32
# python3 gol-block-switch.py --led-multiplexing=1 --led-brightness=10 --led-gpio-mapping=adafruit-hat --led-chain=2 --led-no-hardware-pulse 1 --led-cols=32
# python gol-acorn.py --led-no-hardware-pulse 1 -r 16
# python gol-block-switch.py --led-no-hardware-pulse 1 -r 16
# python gol-red-glider.py --led-no-hardware-pulse 1 --led-multiplexing=1 --led-brightness=10 --led-gpio-mapping=adafruit-hat --led-chain=2 --led-no-hardware-pulse 1 --led-cols=32
#
# python gol-gosper-gun.py --led-no-hardware-pulse 1 -r 16
# python spaceInvader.py --led-no-hardware-pulse 1 --led-multiplexing=1 --led-brightness=10 --led-gpio-mapping=adafruit-hat --led-chain=2 --led-no-hardware-pulse 1 --led-cols=32
# python fixed-text.py --led-no-hardware-pulse 1 -r 16  -t "United Way::25%" --led-gpio-mapping=adafruit-hat
# python fixed-text.py --led-no-hardware-pulse 1 -r 32 --led-gpio-mapping=adafruit-hat -u 50 -t "4 mugs::"

python runtext.py --led-multiplexing=1 --led-chain=2 --led-cols=64 --led-no-hardware-pulse 1 -r 32 -t "This is some long text."

# python bcd_clock.py --led-no-hardware-pulse 1 -r 16
