import random

random.seed(42)

def simular_srtf(processos, context_switch):
    tempo = 0
    prontos = []
    processos = [p.clone() for p in processos]
    finalizados = 0
    atual = None
    timeline = []

    while finalizados < len(processos):
        for p in processos:
            if p.arrival == tempo:
                prontos.append(p)

        if prontos:
            menor = min(p.remaining for p in prontos)
            candidatos = [p for p in prontos if p.remaining == menor]
            escolhido = random.choice(candidatos)

            if atual != escolhido:
                if atual is not None:
                    tempo += context_switch
                atual = escolhido

            if atual.start_time is None:
                atual.start_time = tempo

            atual.remaining -= 1
            timeline.append(atual.pid)

            if atual.remaining == 0:
                atual.finish_time = tempo + 1
                prontos.remove(atual)
                finalizados += 1
                atual = None
        else:
            timeline.append("idle")

        tempo += 1

    return processos, timeline, tempo