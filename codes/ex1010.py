
peca1, qtd_peca1,preço_peca1 = input().split(" ")

peca2,qtd_peca2,preço_peca2 = input().split(" ")


valor_a_pagar = (int(qtd_peca1) * float(preço_peca1)) + (int(qtd_peca2) * float(preço_peca2))

print("VALOR A PAGAR: R$ %.2f" % valor_a_pagar)
