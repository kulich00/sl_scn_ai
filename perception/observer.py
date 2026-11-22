from .observation import Observation
import time

def observe():
    return Observation(timestamp = time.monotonic(), frame = None, audio = None)
