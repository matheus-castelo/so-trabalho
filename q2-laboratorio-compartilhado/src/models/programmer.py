import threading
import time
import random


class Programmer(threading.Thread):
    def __init__(self, programmer_id, resource_manager, display_service):
        super().__init__(name=f"Programador-{programmer_id}")
        self.programmer_id = programmer_id
        self.resource_manager = resource_manager
        self.display_service = display_service

    def run(self):
        while True:
            self.think()
            self.acquire_resources()
            self.compile_code()
            self.release_resources()

    def think(self):
        self.display_service.log(self.programmer_id, "Pensando...")
        time.sleep(random.uniform(1.0, 3.0))

    def acquire_resources(self):
        self.display_service.log(self.programmer_id, "Aguardando Compilador...")
        self.resource_manager.acquire_compiler()

        self.display_service.log(self.programmer_id, "Compilador adquirido. Aguardando Banco de Dados...")
        self.resource_manager.acquire_db()

    def compile_code(self):
        self.display_service.log(self.programmer_id, "COMPILANDO (Compilador + Banco de Dados)")
        time.sleep(random.uniform(2.0, 4.0))

    def release_resources(self):
        self.resource_manager.release()
        self.display_service.log(self.programmer_id, "Liberou os recursos.")