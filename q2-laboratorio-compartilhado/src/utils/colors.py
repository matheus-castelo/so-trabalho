"""Códigos de cores ANSI para saída colorida no terminal."""


class Colors:
    """Constantes de escape ANSI para colorir a saída do terminal.

    Attributes:
        RESET: Reseta todas as formatações.
        BOLD: Aplica negrito ao texto.
        P1-P5: Cores de identidade para cada programador.
        THINKING: Cor para o estado de pensamento (cinza).
        WAITING: Cor para o estado de espera (vermelho).
        WAITING_DB: Cor para espera do banco de dados (amarelo).
        COMPILING: Cor para o estado de compilação (verde).
        RELEASING: Cor para o estado de liberação (amarelo).
    """

    RESET = '\033[0m'
    BOLD = '\033[1m'

    # Programmer identity colors
    P1 = '\033[94m'   # Blue
    P2 = '\033[96m'   # Cyan
    P3 = '\033[95m'   # Magenta
    P4 = '\033[33m'   # Yellow
    P5 = '\033[36m'   # Teal

    # State colors
    THINKING = '\033[90m'       # Gray
    WAITING = '\033[91m'        # Red
    WAITING_DB = '\033[93m'     # Yellow
    COMPILING = '\033[92m'      # Green
    RELEASING = '\033[93m'      # Yellow
