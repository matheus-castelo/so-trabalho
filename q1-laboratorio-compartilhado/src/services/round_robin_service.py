from collections import deque

def simular_rr(processos, quantum, context_switch):
    tempo = 0
    fila = deque()
    processos = [p.clone() for p in processos]
    finalizados = 0
    timeline = []
    atual = None
    q_restante = quantum

    while finalizados < len(processos):
        for p in processos:
            if p.arrival == tempo:
                fila.append(p)

        if atual is None and fila:
            atual = fila.popleft()
            q_restante = quantum

            if atual.start_time is None:
                atual.start_time = tempo

        if atual:
            atual.remaining -= 1
            q_restante -= 1
            timeline.append(atual.pid)

            if atual.remaining == 0:
                atual.finish_time = tempo + 1
                finalizados += 1
                atual = None
                tempo += context_switch
                continue

            if q_restante == 0:
                fila.append(atual)
                atual = None
                tempo += context_switch
                continue
        else:
            timeline.append("idle")

        tempo += 1

    return processos, timeline, tempo