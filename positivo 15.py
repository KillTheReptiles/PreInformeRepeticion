print("Comienzo")
print()
numero = int(input("Escriba un numero menor y positivo a 15: "))
while numero < 0:
    print("Has escrito un numero negativo")
    numero = int(input("scriba un numero menor y positivo a 15: "))


while numero > 15:
    print("Has escrito un numero positivo mayor a 15")
    numero = int(input("scriba un numero menor y positivo a 15: "))

print("Tu numero es positivo y esta entre 0 y 15, Gracias :D!")
print()
print("Final")