import threading
from src.models.VetRoomFair import VetRoomFair
from src.models.VetRoomStarvation import VetRoomStarvation
from src.services.animal_service import animal_task

data = {
    "workload": {
        "animals": [
            {"id": "D01", "species": "DOG", "arrival_time": 0, "rest_duration": 5},
            {"id": "C01", "species": "CAT", "arrival_time": 1, "rest_duration": 4},
            {"id": "D02", "species": "DOG", "arrival_time": 2, "rest_duration": 6},
            {"id": "C02", "species": "CAT", "arrival_time": 3, "rest_duration": 2},
            {"id": "D03", "species": "DOG", "arrival_time": 4, "rest_duration": 3}
        ]
    }
}

def run_simulation(protocol_class,json_data):
    print(f"Iniciando simulação com:{protocol_class.__name__}")
    room = protocol_class()
    threads = []

    for animal_info in json_data['workload']['animals']:
        t = threading.Thread(target=animal_task, args=(room,animal_info))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Simulação finalizada.")

if __name__ == "__main__":
    run_simulation(VetRoomFair, data)