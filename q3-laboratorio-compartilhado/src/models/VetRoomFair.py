import threading

class VetRoomFair:
    def __init__(self):
        self.door = threading.Lock()
        self.turnstile = threading.Lock()
        self.dog_lock = threading.Lock()
        self.cat_lock = threading.Lock()
        self.dog_count = 0
        self.cat_count = 0
    
    def enter(self, animal_id, species):
        with self.turnstile:
            if species == "DOG":
                with self.dog_lock:
                    if self.dog_count == 0:
                        self.door.acquire()
                    self.dog_count += 1
            else:
                with self.cat_lock:
                    if self.cat_count == 0:
                        self.door.acquire()
                    self.cat_count += 1
        self._print_room_state(f"{animal_id}({species}) ENTROU")

    def leave(self, animal_id, species):
        if species == "DOG":
            with self.dog_lock:
                self.dog_count -= 1
                if self.dog_count == 0:
                    self.door.release()
        else:
            with self.cat_lock:
                self.cat_count -= 1
                if self.cat_count == 0:
                    self.door.release()
        self._print_room_state(f"{animal_id}({species}) SAIU")

    def _print_room_state(self, action):
        if self.dog_count > 0:
            state = f"CÃES NA SALA ({self.dog_count})"
        elif self.cat_count > 0:
            state = f"GATOS NA SALA ({self.cat_count})"
        else:
            state = "VAZIA"
        
        print(f"[{action}] -> Estado da Sala: {state}")