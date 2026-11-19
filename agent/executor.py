from .control import ControlState
from .action import Action
class Executor:
    def __init__(self,control_state):
        self.control_state = control_state
        self.keyboard = {'left':'a', 'vent':'w', 'right':'d'}

    def door_action(self, kind, target):
        if kind == "close_door":
            desired_closed = True
        elif kind == "open_door":
            desired_closed = False
        else: return ValueError(f"wrong door status{kind}")
        
        if self.control_state.need_door_toggle(target, desired_closed) == True:
            return self.keyboard[target]
        else: return None
        