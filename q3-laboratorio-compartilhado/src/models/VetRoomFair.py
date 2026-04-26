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
        print(f"[{species}] {animal_id} ENTROU na sala.")

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
        print(f"[{species}] {animal_id} SAIU da sala.")