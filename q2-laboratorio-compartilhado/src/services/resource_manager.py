import threading

from src.utils.constants import MAX_DB_ACCESS

class ResourceManager:
    def __init__(self) -> None:
        self.compiler: threading.Lock = threading.Lock()
        self.database: threading.Semaphore = threading.Semaphore(MAX_DB_ACCESS)