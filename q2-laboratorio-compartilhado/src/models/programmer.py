import threading
import random

from src.utils.constants import MIN_THINK_TIME, MAX_THINK_TIME, MIN_COMPILE_TIME, MAX_COMPILE_TIME
from src.models.programmer_state import ProgrammerState

class Programmer(threading.Thread):
    def __init__(
        self,
        programmer_id: int,
        resource_manager,
        display_service,
        stop_event: threading.Event,
    ) -> None:
        super().__init__(name=f"Programador-{programmer_id}")
        self.programmer_id = programmer_id
        self.resource_manager = resource_manager
        self.display_service = display_service
        self.stop_event = stop_event

    def run(self) -> None:
        def log_wait_compiler():
            self.display_service.log(self.programmer_id, ProgrammerState.WAITING_COMPILER)

        while not self.stop_event.is_set():
            self.think()
            if self.stop_event.is_set():
                break
            
            self.display_service.log(self.programmer_id, ProgrammerState.WAITING_DB)
            with self.resource_manager.use_resources(self.stop_event, log_wait_compiler) as acquired:
                if acquired and not self.stop_event.is_set():
                    self.compile_code()
            
            self.display_service.log(self.programmer_id, ProgrammerState.RELEASING)

    def think(self) -> None:
        self.display_service.log(self.programmer_id, ProgrammerState.THINKING)
        self.stop_event.wait(random.uniform(MIN_THINK_TIME, MAX_THINK_TIME))

    def compile_code(self) -> None:
        self.display_service.log(self.programmer_id, ProgrammerState.COMPILING)
        self.stop_event.wait(random.uniform(MIN_COMPILE_TIME, MAX_COMPILE_TIME))