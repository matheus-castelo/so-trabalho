import threading
import logging 

logger = logging.getLogger(__name__)

class VetRoomStarvation:
    def __init__(self):
        self.door = threading.Lock()
        self.dog_lock = threading.Lock()
        self.cat_lock = threading.Lock()
        self.state_lock = threading.Lock()
        self.dog_count = 0
        self.cat_count = 0

    def enter(self,animal_id,species):
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
        self._log_state(f"{animal_id}({species}) ENTROU")
    
    def leave(self,animal_id,species):
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
        self._log_state(f"{animal_id}({species}) SAIU")    

    def _log_state(self, action):
        with self.state_lock:
            dogs = self.dog_count
            cats = self.cat_count

        if dogs > 0:
            state = f"CÃES NA SALA ({dogs})"
        elif cats > 0:
            state = f"GATOS NA SALA ({cats})"
        else:
            state = "VAZIA"
        logger.info("[%s] -> Estado: %s", action, state)