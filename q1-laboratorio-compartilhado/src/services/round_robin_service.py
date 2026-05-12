from collections import deque
from src.models.processo import Processo
from src.services.metricas_service import calcular_metricas
from src.utils.display import exibir_painel_resultados, animar_simulacao_detalhada
from src.utils.colors import Colors

def simular_rr(processos, quantum, context_switch):
    tempo = 0
    fila = deque()
    processos = [p.clone() for p in processos]
    finalizados = 0
    timeline_rica = []
    
    atual = None
    q_restante = 0
    troca_restante = 0 

    while finalizados < len(processos):
        for p in processos:
            if p.arrival == tempo:
                fila.append(p)

        if troca_restante > 0:
            timeline_rica.append({"tempo": tempo, "processo": "idle", "quantum": "-"})
            troca_restante -= 1
            tempo += 1
            continue 

        if atual is None and fila:
            atual = fila.popleft()
            q_restante = quantum
            if atual.start_time is None:
                atual.start_time = tempo

        if atual:
            atual.remaining -= 1
            q_restante -= 1
            
            timeline_rica.append({
                "tempo": tempo,
                "processo": atual.pid,
                "quantum": q_restante + 1
            })

            if atual.remaining == 0:
                atual.finish_time = tempo + 1
                finalizados += 1
                atual = None
                troca_restante = context_switch 
                
            elif q_restante == 0:
                fila.append(atual) 
                atual = None
                troca_restante = context_switch 
        else:
            timeline_rica.append({"tempo": tempo, "processo": "idle", "quantum": "-"})

        tempo += 1

    return processos, timeline_rica, tempo


def escalonamento_rr(json_data):
    metadata = json_data["metadata"]
    context_switch = metadata["context_switch_cost"]
    janela = metadata["throughput_window_T"]
    quantums = metadata["rr_quantums"]

    processos_base = []
    for p_data in json_data["workload"]["processes"]:
        processos_base.append(Processo(p_data["pid"], p_data["arrival_time"], p_data["burst_time"]))

    for q in quantums:
        proc_rr, timeline_rr, tempo_total_rr = simular_rr(processos_base, q, context_switch)
        
        metricas_rr = calcular_metricas(proc_rr, janela, timeline_rr, tempo_total_rr)
        
        exibir_painel_resultados(
            titulo=f"ROUND ROBIN (Quantum = {q})",
            cor_tema=Colors.CYAN,
            timeline_rica=timeline_rr,
            metricas=metricas_rr,
            tempo_total=tempo_total_rr,
            janela=janela
        )
        animar_simulacao_detalhada(timeline_rr, velocidade=0.04)