"""
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
"""

import json

with open('arquivo.json', 'r') as file:
    dados = json.load(file)

# Extrair os valores de faturamento (faturamento não pode ser 0)
valores = [valor for valor in dados.values() if valor > 0]

if valores== False:
    print("Não há faturamento para calcular.")

else:

    menor_f = min(valores)
    maior_f = max(valores)

    media_mensal = sum(valores) / len(valores)

    dias_maior_media = sum(1 for valor in valores if valor > media_mensal) #número de dias com faturamento superior a média

    print("Menor valor de faturamento: ",menor_f)
    print("Maior valor de faturamento: ", maior_f)
    print(f"Ocorreram {dias_maior_media} dias de faturamento acima da média")
