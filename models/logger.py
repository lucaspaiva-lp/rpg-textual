import os
from datetime import datetime


class Logger:
    """
    Logger simples e persistente.
    Guarda eventos em memória e também grava em arquivo.
    Compatível com exportação/importação via JSON.
    """

    def __init__(self):
        self.eventos: list[str] = []

        self.dir = "logs"
        os.makedirs(self.dir, exist_ok=True)

        data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.arquivo = os.path.join(self.dir, f"log_{data}.txt")

        with open(self.arquivo, "a", encoding="utf-8") as f:
            f.write("=====================================\n")
            f.write("   INÍCIO DA SESSÃO DO JOGO\n")
            f.write(f"   {datetime.now()}\n")
            f.write("=====================================\n\n")

    # ----------------------------------------------
    #            MÉTODO PRINCIPAL DE LOG
    # ----------------------------------------------
    def log(self, mensagem: str, tipo="SISTEMA"):
        linha = f"[{datetime.now().strftime('%H:%M:%S')}] [{tipo}] {mensagem}"
        self.eventos.append(linha)
        with open(self.arquivo, "a", encoding="utf-8") as f:
            f.write(linha + "\n")

    # ----------------------------------------------
    #              TIPOS DE LOG
    # ----------------------------------------------
    def log_batalha(self, mensagem: str):
        self.log(mensagem, tipo="BATALHA")

    # ----------------------------------------------
    #         EXPORTAÇÃO E IMPORTAÇÃO
    # ----------------------------------------------
    def exportar(self) -> list[str]:
        return list(self.eventos)

    def importar(self, lista_logs: list[str]):
        if isinstance(lista_logs, list):
            self.eventos = list(lista_logs)

    # ----------------------------------------------
    #                 LEITURA
    # ----------------------------------------------
    def listar_eventos(self) -> list[str]:
        return self.eventos
