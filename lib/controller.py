from inputs import get_gamepad
import math
import threading


class Controller(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):
        self.left_joy_stick_y = 0
        self.left_joy_stick_x = 0
        self.right_joy_stick_y = 0
        self.right_joy_stick_x = 0
        self.left_trigger = 0
        self.right_trigger = 0
        self.left_bumper = 0
        self.right_bumper = 0
        self.a = 0
        self.x = 0
        self.y = 0
        self.b = 0
        self.left_thumb = 0
        self.right_thumb = 0
        self.back = 0
        self.start = 0
        self.left_dpad = 0
        self.right_dpad = 0
        self.up_dpad = 0
        self.down_dpad = 0

        self.__monitor_thread = threading.Thread(target=self.__monitor_controller, args=())
        self.__monitor_thread.daemon = True
        self.__monitor_thread.start()

    def __monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.left_joy_stick_y = event.state / Controller.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.left_joy_stick_x = event.state / Controller.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.right_joy_stic_y = event.state / Controller.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.right_joy_stick_x = event.state / Controller.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.left_trigger = event.state / Controller.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.right_trigger = event.state / Controller.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.left_bumper = event.state
                elif event.code == 'BTN_TR':
                    self.right_bumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.a = event.state
                elif event.code == 'BTN_NORTH':
                    self.y = event.state # previously switched with X
                elif event.code == 'BTN_WEST':
                    self.x = event.state # previously switched with Y
                elif event.code == 'BTN_EAST':
                    self.b = event.state
                elif event.code == 'BTN_THUMBL':
                    self.left_thumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.right_thumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.back = event.state
                elif event.code == 'BTN_START':
                    self.start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.left_dpad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.right_dpad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.up_dpad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.down_dpad = event.state
