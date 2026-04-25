import threading

class ResourceManager:
    def __init__(self):
        self.compiler = threading.Lock()
        self.database = threading.Semaphore(2)

    def acquire_db(self):
        self.database.acquire()
        
    def acquire_compiler(self):
        self.compiler.acquire()

    def release(self):
        self.compiler.release()
        self.database.release()