from os import system
system("cls")
Datos=[]
sueldos=[]

print("========================================================")
print("       D A T O S  D E  T R A B A J A D O R E S          ")
print("========================================================")
cantidad= int(input('Ingrese la cantidad de personal: '))
if cantidad <=10:
    for x in range (cantidad):
        nom= str(input('Ingrese el nombre: '))
        Datos.append(nom)
        edad= int(input('Ingrese la edad: '))
        Datos.append(edad)
        sueldo= int(input('Ingrese el sueldo: '))
        sueldos.append((sueldo))
        print("---")
while cantidad > 10:
    print('No es una cantidad valida')
    cantidad= int(input('Ingrese la cantidad de personal: '))
while cantidad == 0:
    print('No es una cantidad valida')
    cantidad= int(input('Ingrese la cantidad de personal: '))
'''
else:
    print('No es una cantidad valida')
    cantidad>10
if cantidad == 0:
    print('No hay datos')
elif cantidad <= 10:
    print(Datos)
'''
maximo = max(sueldos)
minimo = min(sueldos)
media = sum(sueldos) / cantidad
    # Imprimimos los resultados con un formato adecuado
print(f'El sueldo máximo es de {maximo} y lo tiene el trabajador {Datos[sueldos.index(maximo) * 3]}')
print("---")
print(f'El sueldo mínimo es de {minimo} y lo tiene el trabajador {Datos[sueldos.index(minimo) * 3]}')
print("---")
print(f'El sueldo medio es de {media} ')
