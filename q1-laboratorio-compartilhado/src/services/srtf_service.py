import random
from src.models.processo import Processo
from src.services.metricas_service import calcular_metricas
from src.utils.display import exibir_painel_resultados, animar_simulacao_detalhada
from src.utils.colors import Colors

random.seed(42)

def simular_srtf(processos, context_switch):
    tempo = 0
    prontos = []
    processos = [p.clone() for p in processos]
    finalizados = 0
    timeline_rica = []
    
    atual = None
    ultimo_processo = None 
    troca_restante = 0

    while finalizados < len(processos):
        for p in processos:
            if p.arrival == tempo:
                prontos.append(p)

        if troca_restante > 0:
            timeline_rica.append({"tempo": tempo, "processo": "idle"})
            troca_restante -= 1
            tempo += 1
            continue

        if prontos:
            menor = min(p.remaining for p in prontos)
            candidatos = [p for p in prontos if p.remaining == menor]
            
            if atual is not None and atual in candidatos:
                escolhido = atual
            else:
                escolhido = random.choice(candidatos)

            if ultimo_processo is not None and ultimo_processo != escolhido.pid:
                troca_restante = context_switch
                ultimo_processo = None 
                
                timeline_rica.append({"tempo": tempo, "processo": "idle"})
                troca_restante -= 1
                tempo += 1
                continue

            atual = escolhido
            ultimo_processo = atual.pid

            atual = escolhido
            ultimo_processo = atual.pid
            
            if atual.start_time is None:
                atual.start_time = tempo

            atual.remaining -= 1
            timeline_rica.append({"tempo": tempo, "processo": atual.pid})

            if atual.remaining == 0:
                atual.finish_time = tempo + 1
                prontos.remove(atual)
                finalizados += 1
                atual = None
        else:
            timeline_rica.append({"tempo": tempo, "processo": "idle"})

        tempo += 1

    return processos, timeline_rica, tempo



def escalonamento_srtf(json_data, quer_animacao=False): # Parâmetro adicionado
    metadata = json_data["metadata"]
    context_switch = metadata["context_switch_cost"]
    janela = metadata["throughput_window_T"]

    processos_base = []
    for p_data in json_data["workload"]["processes"]:
        processos_base.append(Processo(p_data["pid"], p_data["arrival_time"], p_data["burst_time"]))

    proc_srtf, timeline_srtf, tempo_total_srtf = simular_srtf(processos_base, context_switch)
    metricas_srtf = calcular_metricas(proc_srtf, janela, timeline_srtf, tempo_total_srtf)
    
    exibir_painel_resultados(
        titulo="SHORTEST REMAINING TIME FIRST (SRTF)",
        cor_tema=Colors.BLUE,
        timeline_rica=timeline_srtf,
        metricas=metricas_srtf,
        tempo_total=tempo_total_srtf,
        janela=janela
    )
    
    if quer_animacao:
        animar_simulacao_detalhada(timeline_srtf, velocidade=0.04)