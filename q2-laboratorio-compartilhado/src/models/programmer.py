import threading
import time
import random

from src.utils.constants import MIN_THINK_TIME, MAX_THINK_TIME, MIN_COMPILE_TIME, MAX_COMPILE_TIME
from src.models.programmer_state import ProgrammerState


class Programmer(threading.Thread):
    def __init__(self, programmer_id, resource_manager, display_service, stop_event):
        super().__init__(name=f"Programador-{programmer_id}")
        self.programmer_id = programmer_id
        self.resource_manager = resource_manager
        self.display_service = display_service
        self.stop_event = stop_event

    def run(self):
        while not self.stop_event.is_set():
            self.think()
            if self.stop_event.is_set():
                break
            self.acquire_resources()
            self.compile_code()
            self.release_resources()

    def think(self):
        self.display_service.log(self.programmer_id, ProgrammerState.THINKING)
        self.stop_event.wait(random.uniform(MIN_THINK_TIME, MAX_THINK_TIME))

    def acquire_resources(self):
        self.display_service.log(self.programmer_id, ProgrammerState.WAITING_COMPILER)
        self.resource_manager.acquire_compiler()

        self.display_service.log(self.programmer_id, ProgrammerState.WAITING_DB)
        self.resource_manager.acquire_db()

    def compile_code(self):
        self.display_service.log(self.programmer_id, ProgrammerState.COMPILING)
        self.stop_event.wait(random.uniform(MIN_COMPILE_TIME, MAX_COMPILE_TIME))

    def release_resources(self):
        self.resource_manager.release()
        self.display_service.log(self.programmer_id, ProgrammerState.RELEASING)