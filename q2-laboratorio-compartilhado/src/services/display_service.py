import threading

from src.utils.colors import Colors


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

    def log(self, programmer_id, status):
        with self.console_lock:
            p_color = self.programmer_colors.get(programmer_id, Colors.RESET)

            if "Pensando" in status:
                s_color = Colors.THINKING
            elif "Aguardando Compilador" in status:
                s_color = Colors.WAITING
            elif "Aguardando Banco" in status:
                s_color = Colors.WAITING_DB
            elif "COMPILANDO" in status:
                s_color = f"{Colors.COMPILING}{Colors.BOLD}"
            else:
                s_color = Colors.RELEASING

            print(f"{p_color}[Programador {programmer_id}]{Colors.RESET} Status: {s_color}{status}{Colors.RESET}")