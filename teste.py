#--Criando un teste com pontuação--
print("Teste seus conhecimentos sobre ciências 🧪")
pontos = 0

#-- questão 1--

print("1-Qual é a formula da água??💧")
print("\n a)H2O \n b)CO2 \n c)AL")
resposta1 = input("Digite a resposta: ").lower()

if resposta1 == "a":
    print("correta ✅")
    pontos = pontos + 1
else:
    print("você errou ❌")

#--questão 2--

print("2-O sol é: ")
print(" a) satélite \n b) estrela \n c) asteroide")
resposta2 = input("Digite a resposta: ").lower()

if resposta2 == "b":
    print("você acertou ✅")
    pontos = pontos + 1
else:
    print("você errou ❌")

#-- Questão 3--

print("3- ")
print(" a)  \n b)  \n c) ")
resposta2 = input("Digite a resposta: ").lower()

if resposta2 == "b":
    print("você acertou ✅")
    pontos = pontos + 1
else:
    print("você errou ❌")
    print("Fim do questionario")
print(f"Total de pontos: {pontos}")
