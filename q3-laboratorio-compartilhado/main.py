# main.py
import threading
import json
import os
import time
import logging
from src.models.VetRoomFair import VetRoomFair
from src.models.VetRoomStarvation import VetRoomStarvation
from src.services.animal_service import animal_task

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)-10s] %(message)s",
    datefmt="%H:%M:%S",
)

def run_simulation(protocol_class, json_data: dict) -> None:
    logging.info("=== %s ===", protocol_class.__name__)
    room    = protocol_class()
    animals = json_data["workload"]["animals"]
    threads = [
        threading.Thread(
            target=animal_task,
            args=(room, animal),
            name=animal["id"],       
            daemon=True,
        )
        for animal in animals
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    logging.info("=== simulação encerrada ===\n")

if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "src", "data", "petshop.json")

    with open(json_path, encoding="utf-8") as f:
        json_data = json.load(f)

    run_simulation(VetRoomStarvation, json_data)
    time.sleep(0.2)     
    run_simulation(VetRoomFair, json_data)