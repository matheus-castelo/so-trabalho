import time
from src.utils.constants import NUM_PROGRAMMERS
from src.services.resource_manager import ResourceManager
from src.services.display_service import DisplayService
from src.models.programmer import Programmer

def main():
    print("Iniciando o trabalho no laboratório...")
    print("-" * 50)

    resource_manager = ResourceManager()
    display_service = DisplayService()

    programmers = []
    for i in range(1, NUM_PROGRAMMERS + 1):
        programmer = Programmer(i, resource_manager, display_service)
        programmer.daemon = True 
        programmers.append(programmer)

    for programmer in programmers:
        programmer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n" + "="*50)
        print("🛑 Dia de trabalho finalizado com sucesso! (Ctrl+C)")
        print("="*50 + "\n")

if __name__ == "__main__":
    main()