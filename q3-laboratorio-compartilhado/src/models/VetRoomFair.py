import threading
import logging

logger = logging.getLogger(__name__)


class VetRoomFair:

    def __init__(self):
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)

        self.current_species = None

        self.dog_count = 0
        self.cat_count = 0

        self.waiting_dogs = 0
        self.waiting_cats = 0

        self.next_turn = None

    def enter(self, animal_id, species):
        with self.cond:
            if species == "DOG":
                self.waiting_dogs += 1
                while (
                    self.current_species == "CAT"
                    or (self.waiting_cats > 0 and self.next_turn != "DOG")
                ):
                    self.cond.wait()
                self.waiting_dogs -= 1
                self.dog_count += 1
                self.current_species = "DOG"
            else:
                self.waiting_cats += 1
                while (
                    self.current_species == "DOG"
                    or (self.waiting_dogs > 0 and self.next_turn != "CAT")
                ):
                    self.cond.wait()
                self.waiting_cats -= 1
                self.cat_count += 1
                self.current_species = "CAT"

        self._log_state(f"{animal_id}({species}) ENTROU")

    def leave(self, animal_id, species):
        with self.cond:
            if species == "DOG":
                self.dog_count -= 1
                if self.dog_count == 0:
                    self.current_species = None
                    self.next_turn = "CAT" if self.waiting_cats > 0 else "DOG"
                    self.cond.notify_all()
            else:
                self.cat_count -= 1
                if self.cat_count == 0:
                    self.current_species = None
                    self.next_turn = "DOG" if self.waiting_dogs > 0 else "CAT"
                    self.cond.notify_all()

        self._log_state(f"{animal_id}({species}) SAIU")

    def _log_state(self, action):
        with self.cond:
            dogs = self.dog_count
            cats = self.cat_count

        if dogs > 0:
            state = f"CÃES NA SALA ({dogs})"
        elif cats > 0:
            state = f"GATOS NA SALA ({cats})"
        else:
            state = "VAZIA"

        logger.info("[%s] -> Estado: %s", action, state)