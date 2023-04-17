x1, y1 = [float(valor) for valor in input().split()]
x2, y2 = [float(valor) for valor in input().split()]

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f"{distancia:.4f}")

# ** é a raiz quadrada
#esse float é um método de colocar os valores x1 e y2 como floats. -> passa float() e um parâmetro dentro para ele usar o for