nome = input("coloque o nome no aluno")
idade = int(input("coloque a sua idade")) 
turma = input("qual turma pertence") 

if idade>=6:
    print(f"aluno cadastrado com sucesso {nome}, {idade} anos, turma {turma}")  
else:
    print("a crinaça ainda nao tem idade suficiente")
    