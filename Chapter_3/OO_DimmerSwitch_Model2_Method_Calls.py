class DimmerSwitch:
    def __init__(self, label) -> None:
        self._switch_is_on = False
        self.brightness = 0
        self.label = label

    def turn_on(self):
        self.switch_is_on = True

    def turn_off(self):
        self.switch_is_on = False

    def raise_level(self):
        if self.brightness < 10:
            self.brightness += 1

    def lower_level(self):
        if self.brightness > 0:
            self.brightness -= 1

    def show(self):
        print('Label: ', self.label)
        print("Light is on? : ", self.switch_is_on)
        print("Brightness is: ", self.brightness)


o_dimmer_1 = DimmerSwitch("Dimmer1")
o_dimmer_2 = DimmerSwitch("Dimmer2")

o_dimmer_1.raise_level()
o_dimmer_2.raise_level()

