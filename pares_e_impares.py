par = []
impar = []

while True:
    dig_num = int(input("Digite os números: "))
    quer_continuar = str(input("Quer continuar: s/n ")).upper()

    if quer_continuar == "N".upper():
        break

    if dig_num % 2 == 0:
        par.append(dig_num)
    else:
        if dig_num % 2 != 0:
            impar.append(dig_num)

print(f"Numeros pares: {par}\nnumeros impares: {impar}")
