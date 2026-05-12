import json
from src.services.srtf_service import escalonamento_srtf
from src.services.round_robin_service import escalonamento_rr
from src.utils.colors import Colors

def main():
    caminho_arquivo = "src/data/processos.json"

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados_entrada = json.load(f)
    except FileNotFoundError:
        print(f"{Colors.RED}{Colors.BOLD}Erro crítico: O arquivo '{caminho_arquivo}' não foi encontrado.{Colors.RESET}")
        return


    escolha = input(f"{Colors.CYAN}{Colors.BOLD}Deseja ativar a animação em tempo real? (s/N): {Colors.RESET}").lower()
    quer_animacao = True if escolha == 's' else False

    print(f"\n{Colors.GREEN}{Colors.BOLD}[✓] Dados carregados com sucesso! Iniciando simulações...{Colors.RESET}\n")

    escalonamento_srtf(dados_entrada, quer_animacao)
    escalonamento_rr(dados_entrada, quer_animacao)

if __name__ == "__main__":
    main()