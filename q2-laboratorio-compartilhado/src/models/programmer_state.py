from enum import Enum

class ProgrammerState(Enum):
    THINKING = "Pensando..."
    WAITING_DB = "Aguardando Banco de Dados..."
    WAITING_COMPILER = "Banco de Dados adquirido. Aguardando Compilador..."
    COMPILING = "COMPILANDO (Banco de Dados + Compilador)"
    RELEASING = "Liberou os recursos."
