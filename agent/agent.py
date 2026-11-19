from .control import ControlState
from .night_clock import NightClock
from .executor import Executor

class Agent:
    def __init__(self,start_timestamp):
        self.start_timestamp = start_timestamp
        self.control_state = ControlState()
        self.night_clock = NightClock(start_timestamp)
        self.executor = Executor(self.control_state)

    def decide(self, observation):
        return None
