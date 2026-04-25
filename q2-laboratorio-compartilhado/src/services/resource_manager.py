import threading

from src.utils.constants import MAX_DB_ACCESS


class ResourceManager:
    def __init__(self):
        self.compiler = threading.Lock()
        self.database = threading.Semaphore(MAX_DB_ACCESS)

    def acquire_compiler(self):
        self.compiler.acquire()

    def acquire_db(self):
        self.database.acquire()

    def release(self):
        self.database.release()
        self.compiler.release()