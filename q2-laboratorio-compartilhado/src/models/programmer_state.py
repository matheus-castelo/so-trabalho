from enum import Enum


class ProgrammerState(Enum):
    """Represents the possible states of a programmer in the simulation."""

    THINKING = "Pensando..."
    WAITING_COMPILER = "Aguardando Compilador..."
    WAITING_DB = "Compilador adquirido. Aguardando Banco de Dados..."
    COMPILING = "COMPILANDO (Compilador + Banco de Dados)"
    RELEASING = "Liberou os recursos."
