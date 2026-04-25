"""Gerenciador de recursos compartilhados do laboratório (compilador e banco de dados)."""

import threading

from src.utils.constants import MAX_DB_ACCESS


class ResourceManager:
    """Controla o acesso concorrente ao compilador e ao banco de dados.

    O compilador é um recurso exclusivo (Lock), enquanto o banco de dados
    permite até MAX_DB_ACCESS acessos simultâneos (Semaphore).
    """

    def __init__(self) -> None:
        """Inicializa os primitivos de sincronização."""
        self.compiler: threading.Lock = threading.Lock()
        self.database: threading.Semaphore = threading.Semaphore(MAX_DB_ACCESS)

    def acquire_compiler(self) -> None:
        """Adquire acesso exclusivo ao compilador (bloqueante)."""
        self.compiler.acquire()

    def acquire_db(self) -> None:
        """Adquire acesso compartilhado ao banco de dados (bloqueante)."""
        self.database.acquire()

    def release(self) -> None:
        """Libera banco de dados e compilador na ordem inversa da aquisição."""
        self.database.release()
        self.compiler.release()