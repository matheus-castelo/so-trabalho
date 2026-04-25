class Colors:
    """ANSI color codes for terminal output."""

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
