#Andy Wang Intruder Detector
class UserInput:
    def __init__(self):
        self.press = ""
        self.sensor = ""
        self.pin = ""

    def pressButton(self):
        self.press = int(input("Do you wish to press the button? 1 for yes, 0 for no!"))
        if self.press == 1:
            return True
        else:
            return False

    def activateSensor(self):
        self.sensor = int(input("Do you wish to active the sensor? 1 for yes, 0 for no!"))
        if self.sensor == 1:
            self.sensor = 0
            return True
        else:
            return False

    def enterPin(self):
        self.pin = int(input("Please enter your PIN code:"))
        if self.pin == 123:
            self.pin = 0
            return True
        else:
            return False


class System:
    def __init__(self):
        self.state = "systemInactive"


class StateChange:
    def systemInactive(self):
        UserInput.pressButton(self)
        if UserInput.pressButton(self) is True:
            self.state = "systemActive"
            StateChange.systemActive(self)
            return 0
        else:
            StateChange.systemInactive(self)
    def systemActive(self):
        action = UserInput()
        A = int(input("Which action do you want to make? 1 for press_button, 2 for active sensor, 3 for enter pin"))
        if A == 1:
            action.pressButton(self)
            StateChange.systemActive(self)
        elif A == 2:
            action.activateSensor()
            if action.activateSensor() is True:
                self.state = "alertMode"
                StateChange.alertMode(self)
                return 0
            else:
                StateChange.systemActive(self)
        elif A == 3:
            action.enterPin()
            if action.enterPin() is True:
                self.state = "systemInactive"
                StateChange.systemInactive(self)
            else:
                StateChange.systemActive(self)
        else:
            self.state = "alarmRings"
            StateChange.alarmRings(self)
    def alertMode(self):
        action = UserInput()
        A = int(input("Which action do you want to make? 1 for press_button, 2 for enter pin"))
        if A == 1:

    def alarmRings(self):
        print("RING RING RING!!!")
        action = UserInput()
        A = int(input("Which action do you want to make? 1 for press_button, 2 for enter pin"))
        if A == 1:
            action.pressButton()
            StateChange.systemActive(self)
        elif A == 2:
            action.enterPin(self)
            if action.enterPin(self) is True:
                self.state = "systemInactive"
                StateChange.systemInactive(self)
            else:
                StateChange.alarmRings(self)
        else:
            StateChange.alarmRings()

intruder = StateChange()
intruder.systemInactive()