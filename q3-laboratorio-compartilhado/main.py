import threading
import json
import os
import time
from src.models.VetRoomFair import VetRoomFair
from src.models.VetRoomStarvation import VetRoomStarvation
from src.services.animal_service import animal_task

def run_simulation(protocol_class):
    print(f"--- Iniciando simulação com: {protocol_class.__name__} ---")
    
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, "src", "data", "petshop.json")

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        print(f"ERRO: Arquivo não encontrado em {json_path}")
        return

    room = protocol_class()
    threads = []
    
    time_unit = json_data['workload'].get('time_unit', 'ticks')
    animals = json_data['workload']['animals']

    for animal_info in animals:
        t = threading.Thread(target=animal_task, args=(room, animal_info))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("--- Simulação finalizada com sucesso ---")

if __name__ == "__main__":
    run_simulation(VetRoomStarvation)