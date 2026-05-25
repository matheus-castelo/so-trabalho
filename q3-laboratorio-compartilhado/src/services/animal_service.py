import time 
import logging

logger = logging.getLogger(__name__)

def animal_task(room,animal_data: dict) -> None:

    time.sleep(animal_data['arrival_time']*0.5)
    logger.info("%s(%s) chegou à clínica.", animal_data["id"], animal_data["species"])
    room.enter(animal_data['id'],animal_data['species'])
    try:
        time.sleep(animal_data['rest_duration']*0.5)
    finally:
        room.leave(animal_data['id'],animal_data['species'])