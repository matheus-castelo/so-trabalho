import threading

class ResourceManager:
    def __init__(self):
        self.compiler = threading.Lock()
        
        self.database = threading.Semaphore(2)

    def acquire(self, programmer_id):

        self.compiler.acquire()
        
        self.database.acquire()

    def release(self, programmer_id):

        self.database.release()
        
        self.compiler.release()