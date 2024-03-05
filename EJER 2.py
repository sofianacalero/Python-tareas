from os import system
system("cls")

print("============================================")
print("             C O N V E R T I D O R          ")
print("============================================")

# Validar que el usuario ingrese un número entero para los grados Fahrenheit
while True:
    try:
        Fahrenheit = int(input('Ingrese los grados en Fahrenheit: '))
        break
    except ValueError:
        print("Error: Por favor, ingrese un número entero para los grados Fahrenheit.")

print('...')
celcius = (5/9)*(Fahrenheit-32)

print(f'En grados Celsius es: {celcius}\n')

print("============================================")
print('              Muchas gracias')
print("============================================")
