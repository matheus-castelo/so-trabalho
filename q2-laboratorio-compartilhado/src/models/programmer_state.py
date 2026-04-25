"""Enum que representa os estados possíveis de um programador na simulação."""

from enum import Enum


class ProgrammerState(Enum):
    """Estados do ciclo de vida de um programador no laboratório.

    Cada valor contém a mensagem em português exibida no terminal.
    """

    THINKING = "Pensando..."
    WAITING_DB = "Aguardando Banco de Dados..."
    WAITING_COMPILER = "Aguardando Compilador..."
    COMPILING = "Compilando..."
    RELEASING = "Liberando recursos..."
