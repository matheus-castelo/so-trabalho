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
    def __init__(self):
        self.console_lock = threading.Lock()

        self.programmer_colors = {
            1: Colors.P1,
            2: Colors.P2,
            3: Colors.P3,
            4: Colors.P4,
            5: Colors.P5,
        }

    def log(self, programmer_id, state):
        with self.console_lock:
            p_color = self.programmer_colors.get(programmer_id, Colors.RESET)
            s_color = STATE_COLORS.get(state, Colors.RESET)

            print(f"{p_color}[Programador {programmer_id}]{Colors.RESET} Status: {s_color}{state.value}{Colors.RESET}")