#tabuada do 7
#print("tabuada do 7:")
#for i in range(1, 11):
#    print("7 x ", i, "=", 7 * 1)

#tabuada do 8
#print("tabuada do 8:")
#for i in range(1, 11):
#    print("8 x ", i, "=", 8 * 1)

#tabuada do 9
#print("tabuada do 9:")
#for i in range(1, 11):
#    print("9 x ", i, "=", 9 * 1)


#codigo em python para exibir as tabuadas do 7,8 e 9
def tabuada(numero): 
    print(f"tabuada do {numero}:")
    for i in range (1,11):      
        print(f"{numero} x {i} = {numero*i}")
#exibindo as tabuadas
#tabuada(1)
#tabuada(2)
#tabuada(3)
#tabuada(4)
#tabuada(5)
#tabuada(6)
#tabuada(7)
#tabuada(8)
#tabuada(9)
#tabuada(10)


for i in range(1,101):
    tabuada(i)

#tabuada personalizada em python
def tabuada_personalizada(base, inicio, fim):
    print(f"tabuada do {base} de {inicio} a {fim}:")
    for j in range (inicio, fim + 1):
        print (f"{base} x {j} = {base * j}")


tabuada_personalizada(7,1,10)  
tabuada_personalizada(5,5,15)
