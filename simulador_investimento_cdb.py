#--simulador de cdb--
print("Bem vindo ao simulador de investimentos cdb! 🤑")

aporte = float(input("Quanto você vai depositar por mês? "))
juros = float(input("Qual é a taxa de juros atual da popança? "))#a taxa do cdb 1,24--
meses = int(input("Por quantos meses você vai investir? "))
juros_decimal = juros/100
total = 0

for mes in range (1, meses +1):
    total = total + aporte
    total = total + (total*juros_decimal)
    print(f"Mês {mes}: Saldo total = R$ {total}")
print(f"Ao final de {meses} meses, você terá o valor de R$:{total}")
