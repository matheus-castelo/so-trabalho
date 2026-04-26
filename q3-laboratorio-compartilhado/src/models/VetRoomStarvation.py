import threading

class VetRoomStarvation:
    def __init__(self):
        self.door = threading.Lock()
        self.dog_lock = threading.Lock()
        self.cat_lock = threading.Lock()
        self.dog_count = 0
        self.cat_count = 0