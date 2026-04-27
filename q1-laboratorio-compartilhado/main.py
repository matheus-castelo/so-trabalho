from src.models.processo import Processo
from src.services.srtf_service import simular_srtf
from src.services.round_robin_service import simular_rr
from src.services.metricas_service import calcular_metricas


def main():
    processos_base = [
        Processo("P01", 0, 5),
        Processo("P02", 1, 17),
        Processo("P03", 2, 3),
        Processo("P04", 4, 22),
        Processo("P05", 6, 7),
    ]

    context_switch = 1
    janela = 100
    quantums = [1, 2, 4, 8, 16]

    print("\n===== SRTF =====")
    proc_srtf, timeline_srtf, tempo_total_srtf = simular_srtf(processos_base, context_switch)
    metricas_srtf = calcular_metricas(proc_srtf, janela)

    print("Timeline:", timeline_srtf)
    print("Métricas:", metricas_srtf)
    print("Tempo total:",tempo_total_srtf)

    print("\n===== ROUND ROBIN =====")
    for q in quantums:
        print(f"\n--- Quantum = {q} ---")
        proc_rr, timeline_rr, tempo_total_rr = simular_rr(processos_base, q, context_switch)
        metricas_rr = calcular_metricas(proc_rr, janela)

        print("Timeline:", timeline_rr)
        print("Métricas:", metricas_rr)
        print("Tempo total:",tempo_total_rr)

if __name__ == "__main__":
    main()