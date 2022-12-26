class LightSwitch:
    def __init__(self) -> None:
        self.switch_is_on = False

    def turn_on(self):
        self.switch_is_on = True

    def turn_off(self):
        self.switch_is_on = False

    def show(self):
        print(self.switch_is_on)

o_light_switch_1 = LightSwitch()
o_light_switch_2 = LightSwitch()
o_light_switch_1.show()
o_light_switch_2.show()
