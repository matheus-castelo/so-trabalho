"""Modelo do programador que executa em thread própria no laboratório."""

import threading
import random

from src.utils.constants import MIN_THINK_TIME, MAX_THINK_TIME, MIN_COMPILE_TIME, MAX_COMPILE_TIME
from src.models.programmer_state import ProgrammerState


class Programmer(threading.Thread):
    """Representa um programador que alterna entre pensar e compilar.

    Cada programador executa em uma thread independente, adquirindo
    acesso exclusivo ao compilador e compartilhado ao banco de dados
    antes de compilar. O ciclo se repete até que o stop_event seja sinalizado.
    """

    def __init__(
        self,
        programmer_id: int,
        resource_manager: "ResourceManager",
        display_service: "DisplayService",
        stop_event: threading.Event,
    ) -> None:
        """Inicializa o programador.

        Args:
            programmer_id: Identificador numérico único do programador.
            resource_manager: Gerenciador de recursos compartilhados.
            display_service: Serviço de exibição de status no terminal.
            stop_event: Evento de parada cooperativa entre threads.
        """
        super().__init__(name=f"Programador-{programmer_id}")
        self.programmer_id = programmer_id
        self.resource_manager = resource_manager
        self.display_service = display_service
        self.stop_event = stop_event

    def run(self) -> None:
        """Executa o ciclo principal: pensar → adquirir → compilar → liberar."""
        while not self.stop_event.is_set():
            self.think()
            if self.stop_event.is_set():
                break
            self.acquire_resources()
            self.compile_code()
            self.release_resources()

    def think(self) -> None:
        """Simula o programador pensando por um tempo aleatório."""
        self.display_service.log(self.programmer_id, ProgrammerState.THINKING)
        self.stop_event.wait(random.uniform(MIN_THINK_TIME, MAX_THINK_TIME))

    def acquire_resources(self) -> None:
        """Adquire compilador (exclusivo) e banco de dados (compartilhado).

        A ordem de aquisição é compilador primeiro, depois banco de dados,
        para evitar deadlocks por hold-and-wait.
        """
        self.display_service.log(self.programmer_id, ProgrammerState.WAITING_COMPILER)
        self.resource_manager.acquire_compiler()

        self.display_service.log(self.programmer_id, ProgrammerState.WAITING_DB)
        self.resource_manager.acquire_db()

    def compile_code(self) -> None:
        """Simula a compilação do código por um tempo aleatório."""
        self.display_service.log(self.programmer_id, ProgrammerState.COMPILING)
        self.stop_event.wait(random.uniform(MIN_COMPILE_TIME, MAX_COMPILE_TIME))

    def release_resources(self) -> None:
        """Libera banco de dados e compilador na ordem inversa da aquisição."""
        self.resource_manager.release()
        self.display_service.log(self.programmer_id, ProgrammerState.RELEASING)