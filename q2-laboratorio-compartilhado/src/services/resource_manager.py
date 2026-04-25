import threading
from contextlib import contextmanager
from src.utils.constants import MAX_DB_ACCESS

class ResourceManager:
    def __init__(self) -> None:
        self.compiler = threading.Lock()
        self.database = threading.Semaphore(MAX_DB_ACCESS)

    @contextmanager
    def use_resources(self, stop_event, wait_compiler_cb=None):
        db_acquired = False
        compiler_acquired = False
        try:
            while not stop_event.is_set():
                if self.database.acquire(timeout=0.2):
                    db_acquired = True
                    break
            
            if db_acquired and not stop_event.is_set():
                if wait_compiler_cb:
                    wait_compiler_cb()
                while not stop_event.is_set():
                    if self.compiler.acquire(timeout=0.2):
                        compiler_acquired = True
                        break
            
            yield db_acquired and compiler_acquired
        finally:
            if compiler_acquired:
                self.compiler.release()
            if db_acquired:
                self.database.release()