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
        """Inicializa o lock de console e o mapeamento de cores por programador."""
        self.console_lock: threading.Lock = threading.Lock()

        self.programmer_colors: dict[int, str] = {
            1: Colors.P1,
            2: Colors.P2,
            3: Colors.P3,
            4: Colors.P4,
            5: Colors.P5,
        }

    def log(self, programmer_id: int, state: ProgrammerState) -> None:
        """Exibe o status de um programador no terminal com cores.

        Args:
            programmer_id: Identificador numérico do programador.
            state: Estado atual do programador (ProgrammerState).
        """
        with self.console_lock:
            p_color: str = self.programmer_colors.get(programmer_id, Colors.RESET)
            s_color: str = STATE_COLORS.get(state, Colors.RESET)

            print(f"{p_color}[Programador {programmer_id}]{Colors.RESET} Status: {s_color}{state.value}{Colors.RESET}")