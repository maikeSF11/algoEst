numeros= []
for i in range(10): 
    numeros=(input("Escolha um número")) 
    numeros.append(numeros)
soma= 0 
for numero in numeros:
    soma+= numero
    print("números:",numeros)
    print("Soma",soma)