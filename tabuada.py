#-- tabuada automatica--
print("Bem vindo a tabuada automatica")
numero = int(input("Tabuada de qual numero? "))
print(f"---- Tabuada do numero {numero} ----")

for i in range(1,11):
    resultado = numero * i
    print(f" {numero} x {i} = {resultado}")
    print("-----------------------------")
print(":)")
#--v2--