"""Serviço de exibição de status dos programadores no terminal com cores ANSI."""

import threading

from src.utils.colors import Colors
from src.models.programmer_state import ProgrammerState


STATE_COLORS: dict[ProgrammerState, str] = {
    ProgrammerState.THINKING: Colors.THINKING,
    ProgrammerState.WAITING_COMPILER: Colors.WAITING,
    ProgrammerState.WAITING_DB: Colors.WAITING_DB,
    ProgrammerState.COMPILING: f"{Colors.COMPILING}{Colors.BOLD}",
    ProgrammerState.RELEASING: Colors.RELEASING,
}


class DisplayService:
    """Serviço thread-safe para exibição de status no terminal.

    Utiliza um Lock interno para garantir que as mensagens de log
    não se sobreponham quando múltiplas threads escrevem simultaneamente.
    """

    def __init__(self) -> None:
        """Inicializa o lock de console e a lista de cores disponíveis."""
        self.console_lock: threading.Lock = threading.Lock()
        
        self.available_colors: list[str] = [
            Colors.P1,
            Colors.P2,
            Colors.P3,
            Colors.P4,
            Colors.P5,
        ]

    def _get_programmer_color(self, programmer_id: int) -> str:
        """Retorna uma cor da paleta dinamicamente usando módulo."""
        index = (programmer_id - 1) % len(self.available_colors)
        return self.available_colors[index]

    def log(self, programmer_id: int, state: ProgrammerState) -> None:
        """Exibe o status de um programador no terminal com cores.

        Args:
            programmer_id: Identificador numérico do programador.
            state: Estado atual do programador (ProgrammerState).
        """
        with self.console_lock:
            p_color: str = self._get_programmer_color(programmer_id)
            s_color: str = STATE_COLORS.get(state, Colors.RESET)

            print(f"{p_color}[Programador {programmer_id}]{Colors.RESET} Status: {s_color}{state.value}{Colors.RESET}", flush=True)