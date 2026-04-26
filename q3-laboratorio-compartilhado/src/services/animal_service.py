import time 

def animal_task(room,animal_data):
    time.sleep(animal_data['arrival_time']*0.1)
    print(f"{animal_data['id']}({animal_data['species']}) chegou na clinica.")
    room.enter(animal_data['id'],animal_data['species'])
    time.sleep(animal_data['rest_duration']*0.1)
    room.leave(animal_data['id'],animal_data['species'])