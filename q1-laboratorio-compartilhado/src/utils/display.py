import time
import sys
from src.utils.colors import Colors
from src.utils.formatters import extrair_timeline_simples

def exibir_painel_resultados(titulo, cor_tema, timeline_rica, metricas, tempo_total, janela):
    print(f"\n{cor_tema}{Colors.BOLD}=================================================={Colors.RESET}")
    print(f"{cor_tema}{Colors.BOLD}--- {titulo} ---{Colors.RESET}")
    print(f"{cor_tema}{Colors.BOLD}=================================================={Colors.RESET}\n")

    print(f"{Colors.YELLOW}{Colors.BOLD}[TIMELINE DE EXECUÇÃO ESTÁTICA]{Colors.RESET}")
    print(f" {extrair_timeline_simples(timeline_rica)}\n")

    print(f"{Colors.GREEN}{Colors.BOLD}[MÉTRICAS DE DESEMPENHO]{Colors.RESET}")
    print(f" {Colors.BOLD}• Tempo Total:{Colors.RESET}         {tempo_total} ticks")
    print(f" {Colors.BOLD}• T. Médio Resposta:{Colors.RESET}   {metricas['resp_media']:.2f} {Colors.MAGENTA}(+/- {metricas['resp_std']:.2f}){Colors.RESET}")
    print(f" {Colors.BOLD}• T. Médio Retorno:{Colors.RESET}    {metricas['ret_media']:.2f} {Colors.MAGENTA}(+/- {metricas['ret_std']:.2f}){Colors.RESET}")
    print(f" {Colors.BOLD}• Vazão (T={janela}):{Colors.RESET}        {metricas['vazao']:.4f} processos/tick")
    print(f" {Colors.BOLD}• Eficiência da CPU:{Colors.RESET}   {metricas['eficiencia']:.2f}%\n")

def animar_simulacao_detalhada(timeline_rica, velocidade=0.1):
    print(f"{Colors.YELLOW}{Colors.BOLD}[SIMULAÇÃO EM TEMPO REAL]{Colors.RESET}")
    
    for estado in timeline_rica:
        tempo_str = f"{estado['tempo']:02d}" 
        proc = estado['processo']
        
        if proc == "idle":
            proc_str = f"{Colors.RED}{Colors.BOLD}idle{Colors.RESET}"
        else:
            proc_str = f"{Colors.GREEN}{Colors.BOLD}{proc}{Colors.RESET}"

        linha = f" [ ⏱  {tempo_str} ] CPU: {proc_str:<15}"
        
        if "quantum" in estado:
            linha += f"| Quantum Restante: {estado['quantum']}"
            
        print(linha)
        time.sleep(velocidade) 
        
    print("\n")