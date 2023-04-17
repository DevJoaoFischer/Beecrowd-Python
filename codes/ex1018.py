dinheiro = int(input())

print(dinheiro)

print(f"{dinheiro//100} nota(s) de R$ 100,00")
dinheiro = dinheiro %  100
print(f"{dinheiro//50} nota(s) de R$ 50,00")
dinheiro = dinheiro % 50
print(f"{dinheiro//20} nota(s) de R$ 20,00")
dinheiro = dinheiro % 20
print(f"{dinheiro//10} nota(s) de R$ 10,00")
dinheiro = dinheiro % 10
print(f"{dinheiro//5} nota(s) de R$ 5,00")
dinheiro = dinheiro % 5
print(f"{dinheiro//2} nota(s) de R$ 2,00")
dinheiro = dinheiro % 2
print(f"{dinheiro} nota(s) de R$ 1,00")

#
#dinheiro = int(input())

#notas = [100, 50, 20, 10, 5, 2, 1]


#for nota in notas:
 #   qtdNotas = dinheiro // nota
  #  dinheiro = dinheiro % nota
   # print(f"{qtdNotas} nota(s) de R$1 {nota},00 reais")























