class NightClock:
    def __init__(self, start_timestamp):
        self.start_timestamp = start_timestamp

    def elapsed(self, current_timestamp):
        return current_timestamp - self.start_timestamp

    def end_status(self, current_timestamp):
        if self.elapsed(current_timestamp)<360:
            return False
        return True