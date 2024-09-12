"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
"""
#Apesar de ser uma opção mais demorada o registro de todos os valores como float ao invés de trazê-los no "total" isso possibilita maior versatilidade ao código, caso os valores precisem ser trocados.
sp= float(67836.43)
rj= float(36678.66)
mg= float(29229.88)
es= float(27165.48)
outros= float(19849.53)

total= sp + rj + mg + es + outros

percentual_sp= (sp * 100)/total
percentual_rj= (rj * 100)/total
percentual_mg= (mg * 100)/total
percentual_es= (es * 100)/total
percentual_outros= (outros * 100)/total

print(f"Percentual de São Paulo: {percentual_sp:.2f}%")
print(f"Percentual de Rio de Janeiro: {percentual_rj:.2f}%")
print(f"Percentual de Minas Gerais: {percentual_mg:.2f}%")
print(f"Percentual de Espírito Santo: {percentual_es:.2f}%")
print(f"Percentual Outros: {percentual_outros:.2f}%")