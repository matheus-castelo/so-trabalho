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

    def acquire_compiler(self, stop_event: threading.Event) -> bool:
        """Adquire acesso exclusivo ao compilador com suporte a cancelamento."""
        while not stop_event.is_set():
            if self.compiler.acquire(timeout=0.2):
                return True
        return False

    def acquire_db(self, stop_event: threading.Event) -> bool:
        """Adquire acesso compartilhado ao banco de dados com suporte a cancelamento."""
        while not stop_event.is_set():
            if self.database.acquire(timeout=0.2):
                return True
        return False

    def release_db(self) -> None:
        """Libera acesso ao banco de dados."""
        self.database.release()

    def release_compiler(self) -> None:
        """Libera acesso exclusivo ao compilador."""
        self.compiler.release()