from enum import Enum

class ProgrammerState(Enum):
    THINKING = "Pensando..."
    WAITING_DB = "Aguardando Banco de Dados..."
    WAITING_COMPILER = "Aguardando Compilador..."
    COMPILING = "Compilando..."
    RELEASING = "Liberando recursos..."
