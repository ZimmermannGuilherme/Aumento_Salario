salario = abs(float(input('Qual o seu salário atual? ')))

taxa_15 = salario * (0.15)
taxa_12 = salario * (0.12)
taxa_10 = salario * (0.10)
taxa_7 = salario * (0.07)

novo_15 = salario + taxa_15
novo_12 = salario + taxa_12
novo_10 = salario + taxa_10
novo_7 = salario + taxa_7

if salario <= 1600.00:
  print(f'''Novo salário: R${novo_15:.2f}
  Resjuste ganho: R${taxa_15:.2f}
  Em percentual: 15%''')

elif (salario >= 1600.01) and (salario <= 2400.00):
  print(f'''Novo salário: R${novo_12:.2f}
  Resjuste ganho: R${taxa_12:.2f}
  Em percentual: 12%''')

elif (salario >= 2400.01) and (salario <= 4000.00):
  print(f'''Novo salário: R${novo_10:.2f}
  Resjuste ganho: R${taxa_10:.2f}
  Em percentual: 10%''')

elif salario >= 4000.01:
  print(f'''Novo salário: R${novo_7:.2f}
  Resjuste ganho: R${taxa_7:.2f}
  Em percentual: 7%''')