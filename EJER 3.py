from os import system
system("cls")
print("============================================")
print("       B A N C O  I N D U S T R I A L       ")
print("============================================")

nombre= str(input('Ingrese nombre completo: '))
cedula= int(input('Ingrese el numero de cedula: '))
ingreso_mensual= float(input('Ingrese los ingresos mensuales: '))
if ingreso_mensual >= 5000:

 print("-------------------------------------------")
 print("        ¡¡¡ Prestamo aprobado !!!") 
 print('   ¡Bienvenido a la consulta de credito!')
 print("-------------------------------------------")
else:
 print("-------------------------------------------")
 print('Lo siento, el prestamo no ha sido aprobado')
 print("-------------------------------------------")
 ingreso_mensual <5000