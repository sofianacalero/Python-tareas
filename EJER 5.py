from os import system
system("cls")
print("========================================================")
print("         P A G O  D E  T R A B A J A D O R E S          ")
print("========================================================")
def calcular_salario_bruto(nombre_empleado, dias_trabajados):
    tarifa_diaria = 300  
    horas_por_dia = 6  
    salario_bruto = dias_trabajados * tarifa_diaria
    return salario_bruto

def main():
    cantidad_empleados = int(input("Ingrese el numero de empleados: "))
    
    for i in range(cantidad_empleados):
        while True:
            nombre_empleado = input(f"Ingrese el nombre del empleado {i+1}: ")
            if not nombre_empleado.isnumeric():  # Verifica que no contenga números
                break
            else:
                print("Error: El nombre no puede contener números.")

        while True:
            try:
                dias_trabajados = int(input(f"Ingrese los días trabajados por {nombre_empleado}: "))
                if dias_trabajados >= 0 and dias_trabajados == int(dias_trabajados):  # Verifica que sea un entero positivo
                    break
                else:
                    print("Error: Por favor, ingrese un número entero positivo para los días trabajados.")
            except ValueError:
                print("Error: Por favor, ingrese un número entero para los días trabajados.")

        salario = calcular_salario_bruto(nombre_empleado, dias_trabajados)
        print(f"El salario bruto de {nombre_empleado} es: {salario} córdobas.")

if __name__ == "__main__":
    main()
