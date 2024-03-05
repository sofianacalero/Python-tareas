from os import system
system("cls")
print("============================================")
print("       B A N C O  I N D U S T R I A L       ")
print("============================================")

# Bucle para asegurar que se ingrese un nombre válido (sin números)
while True:
    nombre = input('Ingrese nombre completo: ')
    if nombre.isalpha():
        break
    else:
        print("Error: El nombre no puede contener números. Inténtelo de nuevo.")

# Bucle para asegurar que se ingrese un número de cédula válido (entero positivo)
while True:
    try:
        cedula = int(input('Ingrese el número de cédula: '))
        if cedula > 0:
            break
        else:
            print("Error: El número de cédula debe ser un entero positivo.")
    except ValueError:
        print("Error: Por favor, ingrese un número entero para la cédula.")

# Bucle para asegurar que se ingrese un ingreso mensual válido (número positivo)
while True:
    try:
        ingreso_mensual = float(input('Ingrese los ingresos mensuales: '))
        if ingreso_mensual >= 0:
            break
        else:
            print("Error: Los ingresos mensuales deben ser un número positivo.")
    except ValueError:
        print("Error: Por favor, ingrese un número para los ingresos mensuales.")

if ingreso_mensual >= 5000:
    print("-------------------------------------------")
    print("        ¡¡¡ Préstamo aprobado !!!") 
    print('   ¡Bienvenido a la consulta de crédito!')
    print("-------------------------------------------")
else:
    print("-------------------------------------------")
    print('Lo siento, el préstamo no ha sido aprobado')
    print("-------------------------------------------")
