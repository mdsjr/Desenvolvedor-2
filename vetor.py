import json
import os

def analisar_faturamento(dados_json):
 
    faturamento_diario = [dia['valor'] for dia in dados_json]
    faturamento_diario_sem_zeros = [f for f in faturamento_diario if f > 0]

    if not faturamento_diario_sem_zeros:
        return "Nenhum dia com faturamento registrado."

    menor_faturamento = min(faturamento_diario_sem_zeros)
    maior_faturamento = max(faturamento_diario_sem_zeros)
    media_mensal = sum(faturamento_diario_sem_zeros) / len(faturamento_diario_sem_zeros)
    dias_acima_da_media = sum(1 for f in faturamento_diario_sem_zeros if f > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Carregar dados do arquivo JSON
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo_json = os.path.join(diretorio_atual, 'dados.json')

try:
    with open(caminho_arquivo_json, 'r') as arquivo_json:
        dados_json = json.load(arquivo_json)
except FileNotFoundError:
    print(f"Erro: Arquivo 'dados.json' não encontrado em: {caminho_arquivo_json}")
    exit()
except json.JSONDecodeError:
    print(f"Erro: Conteúdo do arquivo 'dados.json' não é um JSON válido.")
    exit()

resultado = analisar_faturamento(dados_json)

if isinstance(resultado, str):
    print(resultado)
else:
    menor, maior, dias_acima = resultado
    print(f"Menor faturamento: R$ {menor:.2f}")
    print(f"Maior faturamento: R$ {maior:.2f}")
    print(f"Dias acima da média: {dias_acima}")
