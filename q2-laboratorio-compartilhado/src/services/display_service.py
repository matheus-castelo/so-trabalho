import threading


class DisplayService:
    def __init__(self):
        self.console_lock = threading.Lock()

        self.programmer_colors = {
            1: '\033[94m',
            2: '\033[96m',
            3: '\033[95m',
            4: '\033[33m',
            5: '\033[36m',
        }

    def log(self, programmer_id, status):
        with self.console_lock:
            p_color = self.programmer_colors.get(programmer_id, '\033[0m')
            reset = '\033[0m'

            if "Pensando" in status:
                s_color = '\033[90m'
            elif "Aguardando Compilador" in status:
                s_color = '\033[91m'
            elif "Aguardando Banco" in status:
                s_color = '\033[93m'
            elif "COMPILANDO" in status:
                s_color = '\033[92m\033[1m'
            else:
                s_color = '\033[93m'

            print(f"{p_color}[Programador {programmer_id}]{reset} Status: {s_color}{status}{reset}")