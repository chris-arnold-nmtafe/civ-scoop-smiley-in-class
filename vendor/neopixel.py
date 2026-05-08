from neopixel import NeoPixel
from machine import Pin
import time

class SenseHat:
    BLACK=(0,0,0)
    def __init__(self, window_name="", data_pin=14, max_brightness=64):
        self._pixels = [(max_brightness,max_brightness,max_brightness)] * 64
        self._pin = Pin(data_pin, Pin.OUT)
        self._display = NeoPixel(self._pin,64)
        self._low_light=False
    
    def _show(self):
        for i in range(0,64):
            sf = (0.05 if self._low_light else 0.1)
            self._display[i] = (int(self._pixels[i][0]*sf), int(self._pixels[i][1]*sf), int(self._pixels[i][2]*sf))
        self._display.write()

    def set_pixels(self, rgb_values):
        for i in range(0,64):
            self._pixels[i] = rgb_values[i] if i < len(rgb_values) else BLACK
        self._show()

    @property
    def low_light(self):
        """Emulates the SenseHAT.low_light property"""
        return self._low_light

    @low_light.setter
    def low_light(self, value):
        self._low_light = value
        self._show()
        #self.queue.put(('low_light', value))

    def close(self):
        self.root.destroy()


def main():  # sourcery skip: extract-duplicate-method
    """Used only to quickly test and demonstrate the mock SenseHAT class"""
    # from signal import pause
    rgb_values = [(255, 0, 0)] * 64

    mock_sense_hat = SenseHat()
    mock_sense_hat.set_pixels(rgb_values)

    time.sleep(1)
    mock_sense_hat.set_pixels([(0, 255, 0)] * 64)
    time.sleep(1)
    mock_sense_hat.set_pixels([(0, 0, 255)] * 64)
    # To enable low_light mode, set the low_light attribute to True
    mock_sense_hat.low_light = True
    time.sleep(1)
    mock_sense_hat.set_pixels(rgb_values)
    time.sleep(1)
    mock_sense_hat.set_pixels([(0, 255, 0)] * 64)
    time.sleep(1)
    mock_sense_hat.set_pixels([(0, 0, 255)] * 64)
    mock_sense_hat.low_light = False
    time.sleep(1)
    mock_sense_hat.set_pixels(rgb_values)
    time.sleep(1)
    mock_sense_hat.set_pixels([(0, 255, 0)] * 64)
    time.sleep(1)
    mock_sense_hat.set_pixels([(0, 0, 255)] * 64)

    # Keep the main thread alive FOREVER
    time.sleep(60)


if __name__ == '__main__':
    main()
