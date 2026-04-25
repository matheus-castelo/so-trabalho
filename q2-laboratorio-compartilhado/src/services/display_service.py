import threading

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    P1 = '\033[94m' 
    P2 = '\033[96m' 
    P3 = '\033[95m' 
    P4 = '\033[33m' 
    P5 = '\033[36m' 
    
    THINKING = '\033[90m' 
    WAITING = '\033[91m'  
    COMPILING = '\033[92m' 
    RELEASING = '\033[93m' 

class DisplayService:
    def __init__(self):
        self.console_lock = threading.Lock()
        
        self.programmer_colors = {
            1: Colors.P1,
            2: Colors.P2,
            3: Colors.P3,
            4: Colors.P4,
            5: Colors.P5
        }

    def log(self, programmer_id, status):
        with self.console_lock:
            p_color = self.programmer_colors.get(programmer_id, Colors.RESET)
            
            if "Pensando" in status:
                s_color = Colors.THINKING
            elif "Aguardando Banco" in status:
                s_color = Colors.WAITING
            elif "No Banco de Dados" in status:
                s_color = '\033[93m' 
            elif "COMPILANDO" in status:
                s_color = f"{Colors.COMPILING}{Colors.BOLD}"
            else:
                s_color = Colors.RELEASING
                
            print(f"{p_color}[Programador {programmer_id}]{Colors.RESET} Status: {s_color}{status}{Colors.RESET}")