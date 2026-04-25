import threading
from src.utils.colors import Colors
from src.models.programmer_state import ProgrammerState

STATE_COLORS = {
    ProgrammerState.THINKING: Colors.THINKING,
    ProgrammerState.WAITING_COMPILER: Colors.WAITING,
    ProgrammerState.WAITING_DB: Colors.WAITING_DB,
    ProgrammerState.COMPILING: f"{Colors.COMPILING}{Colors.BOLD}",
    ProgrammerState.RELEASING: Colors.RELEASING,
}

class DisplayService:
    def __init__(self) -> None:
        self.console_lock = threading.Lock()
        self.available_colors = [
            Colors.P1, Colors.P2, Colors.P3, Colors.P4, Colors.P5
        ]

    def _get_programmer_color(self, programmer_id: int) -> str:
        index = (programmer_id - 1) % len(self.available_colors)
        return self.available_colors[index]

    def log(self, programmer_id: int, state: ProgrammerState) -> None:
        with self.console_lock:
            p_color = self._get_programmer_color(programmer_id)
            s_color = STATE_COLORS.get(state, Colors.RESET)
            print(f"{p_color}[Programador {programmer_id}]{Colors.RESET} Status: {s_color}{state.value}{Colors.RESET}", flush=True)