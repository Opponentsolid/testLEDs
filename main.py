from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

factory = PiGPIOFactory(host='192.168.1.135')
ledGreen = LED(18, pin_factory=factory)
ledYellow = LED(23, pin_factory=factory)
ledRed = LED(24, pin_factory=factory)



while True:
    ledGreen.on()
    sleep(0.5)
    ledRed.on()
    sleep(0.5)
    ledYellow.on()
    sleep(0.5)
    ledGreen.off()
    sleep(0.5)
    ledRed.off()
    sleep(0.5)
    ledYellow.off()
    sleep(0.5)

