#Realice un programa en Python que leer los datos (nombre, edad y sueldo) de n empleados 
#(máximo 10) e imprima los trabajadores con sueldo máximo y mínimo, así como la media de 
#los sueldos

from os import system
system("cls")

print("========================================================")
print("       D A T O S  D E  T R A B A J A D O R E S          ")
print("========================================================")

Datos = []
sueldos = []

cantidad = int(input('Ingrese la cantidad de personal: '))

# Validar que la cantidad sea válida (entre 1 y 10)
while cantidad < 1 or cantidad > 10:
    print('Cantidad no válida. Ingrese un número entre 1 y 10.')
    cantidad = int(input('Ingrese la cantidad de personal: '))

for _ in range(cantidad):
    nom = input('Ingrese el nombre: ')
    # Validar que el nombre no contenga números
    while any(char.isdigit() for char in nom):
        print("Error: El nombre no puede contener números.")
        nom = input('Ingrese el nombre: ')
    Datos.append(nom)
    
    # Validar que la edad sea un entero positivo
    while True:
        try:
            edad = int(input('Ingrese la edad: '))
            if edad < 0:
                print("Error: La edad debe ser un número positivo.")
            else:
                break
        except ValueError:
            print("Error: La edad debe ser un número entero.")
    Datos.append(edad)
    
    # Validar que el sueldo sea un entero positivo
    while True:
        try:
            sueldo = int(input('Ingrese el sueldo: '))
            if sueldo < 0:
                print("Error: El sueldo debe ser un número positivo.")
            else:
                break
        except ValueError:
            print("Error: El sueldo debe ser un número entero.")
    sueldos.append(sueldo)
    print("---")

maximo = max(sueldos)
minimo = min(sueldos)
media = sum(sueldos) / cantidad

# Imprimir los resultados con un formato adecuado
print(f'El sueldo máximo es de {maximo} y lo tiene el trabajador {Datos[sueldos.index(maximo) * 2]}')
print("---")
print(f'El sueldo mínimo es de {minimo} y lo tiene el trabajador {Datos[sueldos.index(minimo) * 2]}')
print("---")
print(f'El sueldo medio es de {media} ')
