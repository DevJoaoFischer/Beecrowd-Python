#a e b são bases e c altura
"""""
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
"""

A, B, C = input().split(" ")
TRIANGULO= (float(A))*(float(C)) / 2
CIRCULO = 3.14159 * (float(C)) ** 2
TRAPEZIO = ((float(A)) + (float(B))) * (float(C)) / 2
QUADRADO = (float(B)) ** 2
RETANGULO = (float(A)) * (float(B))

print("TRIANGULO: %.3f" % TRIANGULO)
print("CIRCULO: %.3f" % CIRCULO)
print("TRAPEZIO: %.3f" % TRAPEZIO)
print("QUADRADO: %.3f" % QUADRADO)
print("RETANGULO: %.3f" % RETANGULO)
