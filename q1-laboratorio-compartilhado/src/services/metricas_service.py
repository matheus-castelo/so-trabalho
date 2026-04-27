import statistics

def calcular_metricas(processos, janela):
    tempos_resposta = []
    tempos_retorno = []
    concluidos_ate_T = 0

    for p in processos:
        resposta = p.start_time - p.arrival
        retorno = p.finish_time - p.arrival

        tempos_resposta.append(resposta)
        tempos_retorno.append(retorno)

        if p.finish_time <= janela:
            concluidos_ate_T += 1

    return {
        "resp_media": statistics.mean(tempos_resposta),
        "resp_std": statistics.pstdev(tempos_resposta),
        "ret_media": statistics.mean(tempos_retorno),
        "ret_std": statistics.pstdev(tempos_retorno),
        "vazao": concluidos_ate_T / janela
    }