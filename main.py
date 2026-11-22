from agent.agent import Agent
from agent.executor import Executor
from agent.control import ControlState
from agent.action import Action
from perception.observer import observe
import time
class StartAgent:
    def __init__(self, timestamp):
        self.agent = Agent(timestamp)

    def movement(self, action:Action):
        self.agent.executor.execute_door_action(action)

    def cam_open(self, action:Action):
        self.agent
def main():
    time.sleep(5)
    num = observe().timestamp
    start = StartAgent(num)
    for door_side in start.agent.executor.keyboard:
        for kind in ["close_door", "close_door", "open_door"]:
            start.movement(Action(kind, door_side))
    

if __name__ == "__main__":
    main()