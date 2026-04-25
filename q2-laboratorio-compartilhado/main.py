"""Ponto de entrada da simulação do laboratório compartilhado.

Cria os recursos compartilhados, instancia os programadores e
executa a simulação em loop infinito até Ctrl+C.
"""

import threading
import time
from src.utils.constants import NUM_PROGRAMMERS
from src.services.resource_manager import ResourceManager
from src.services.display_service import DisplayService
from src.models.programmer import Programmer


def main() -> None:
    """Inicializa e executa a simulação do laboratório compartilhado."""
    print("Iniciando o trabalho no laboratório...")
    print("-" * 50)

    resource_manager: ResourceManager = ResourceManager()
    display_service: DisplayService = DisplayService()
    stop_event: threading.Event = threading.Event()

    programmers: list[Programmer] = []
    for i in range(1, NUM_PROGRAMMERS + 1):
        programmer = Programmer(i, resource_manager, display_service, stop_event)
        programmer.daemon = True
        programmers.append(programmer)

    for programmer in programmers:
        programmer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n" + "=" * 50)
        print("🛑 Encerrando... Aguardando programadores finalizarem.")
        print("=" * 50)
    finally:
        stop_event.set()

        for programmer in programmers:
            programmer.join(timeout=5)

        alive_threads = [p.name for p in programmers if p.is_alive()]

        print("\n" + "=" * 50)
        if alive_threads:
            print(f"⚠️ Aviso: As seguintes threads não encerraram corretamente: {', '.join(alive_threads)}")
        else:
            print("✅ Dia de trabalho finalizado com sucesso!")
        print("=" * 50 + "\n")


if __name__ == "__main__":
    main()