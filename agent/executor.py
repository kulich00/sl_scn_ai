from .control import ControlState
from .action import Action
import pydirectinput
class Executor:
    def __init__(self,control_state):
        self.control_state = control_state
        self.keyboard = {'left':'a', 'vent':'w', 'right':'d'}

    def door_action(self, action:Action):
        if action.kind == "close_door":
            desired_closed = True
        elif action.kind == "open_door":
            desired_closed = False
        else: raise ValueError(f"wrong door status{action.kind}")
        
        if self.control_state.need_door_toggle(action.target, desired_closed) == True:
            return self.keyboard[action.target]
        else: return None

    def execute_door_action(self, action:Action):
        key = self.door_action(action)
        if key is not None:
            self.press_key(key)
            self.control_state.record_door_toggle(action.target)
            return key
        else: return None 

    def press_key(self, key):
        pydirectinput.press(key)
