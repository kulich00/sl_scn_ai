class ControlState:
    def __init__(self):
        self.left_closed = False
        self.vent_closed = False
        self.right_closed = False
        self.tablet_open = False
        self.current_camera = None

    def door_status_text(self):
        if self.left_closed == False:
            left_text = 'Левая: Открыта'
        else:
            left_text = 'Левая: Закрыта'

        if self.vent_closed == False:
            vent_text = 'Вентиляция: Открыта'
        else:
            vent_text = 'Вентиляция: Закрыта'
        
        if self.right_closed == False:
            right_text = 'Правая: Открыта'
        else:
            right_text = 'Правая: Закрыта'

        return left_text +'|'+ vent_text +'|'+ right_text
    
    def camera_status_text(self):
        if self.tablet_open == True:
            camera_text = "Планшет: Открыт"
        else:
            camera_text = "Планшет: Открыт"
        return camera_text
    
    def need_door_toggle(self, door_side, desired_closed):
        current_close = {'left':self.left_closed,'vent':self.vent_closed,'right':self.right_closed}
        if door_side in current_close:
            if current_close[door_side] != desired_closed: return True
            else: return False

        else: raise ValueError(f"door_side is incorrect {door_side}")

    def record_door_toggle(self, door_side):
        if door_side == "left":
            self.left_closed = not self.left_closed
        elif door_side == "vent":
            self.vent_closed = not self.vent_closed
        elif door_side == "right":
            self.right_closed = not self.right_closed

        else: raise ValueError(f"wrong side {door_side}")