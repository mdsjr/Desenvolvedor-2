def calcular_percentual_representacao(faturamento_estados):
  

    total_faturamento = sum(faturamento_estados.values())
    percentual_representacao = {}

    for estado, faturamento in faturamento_estados.items():
        percentual = (faturamento / total_faturamento) * 100
        percentual_representacao[estado] = round(percentual, 2)

    return percentual_representacao



faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53,
}


percentuais = calcular_percentual_representacao(faturamento_estados)


for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")