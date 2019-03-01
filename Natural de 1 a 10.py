print("Comienzo")
print()
numero = int(input("Escriba un numero entre 1 y 10: "))
while numero < 1:
    print("Has escrito un numero fuera de 1 y 10")
    numero = int(input("Escriba un numero entre 1 y 10: "))


while numero > 10:
    print("Has escrito un numero mayor a 10")
    numero = int(input("Escriba un numero entre 1 y 10: "))

while numero < 10:
    print("Tu numero es positivo y esta entre 0 y 15, Gracias :D")
    numero = int(input("Escriba un numero entre 1 y 10: "))


print()
print("Final")