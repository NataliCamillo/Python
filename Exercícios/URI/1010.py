codigoPeca1,numeroPeca1,valorPeca1 = map(float, input().split(" "))
codigoPeca2,numeroPeca2,valorPeca2 =  map(float, input().split(" "))
total = ((numeroPeca1 * valorPeca1)+(numeroPeca2 * valorPeca2))
print (f"VALOR A PAGAR: R$ {total:.2f}")