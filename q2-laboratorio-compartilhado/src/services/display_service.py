import threading

class DisplayService:
    def __init__(self):

        self.console_lock = threading.Lock()

    def log(self, programmer_id, status):
  
        with self.console_lock:
            print(f"[Programador {programmer_id}] Status: {status}")