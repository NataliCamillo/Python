codigo,quantidade =map (int, input().split(" "))
preco=0
if (codigo == 1):
    preco = float(4.00)
elif (codigo == 2):
     preco = float(4.50)
elif (codigo == 3):
   preco = float(5.00)
elif (codigo == 4):
   preco = float(2.00)
elif (codigo == 5):
 preco = float(1.50)   
total=float(quantidade * preco)
print("Total: R$ %.2f"%total)
                                
    