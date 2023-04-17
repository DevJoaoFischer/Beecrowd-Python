nome = input()
salario_fixo = float(input())
vendas = float(input())
comissao = 15/100

total = salario_fixo + vendas * comissao

print("TOTAL = R$ %.2f" % total )