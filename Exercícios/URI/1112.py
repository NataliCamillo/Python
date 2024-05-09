pi = 3.14159
A,B,C = map(float, input().split(" "))
triangulo = ((A*C)/2)
circulo = (pi*(C**2))
trapezio = (((A+B)* C)/2)
quadrado = (B*B)
retangulo = (A*B)
print(f"TRIANGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapezio:.3f}\nQUADRADO: {quadrado:.3f}\nRETANGULO: {retangulo:.3f}")