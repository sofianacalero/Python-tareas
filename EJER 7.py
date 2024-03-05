from os import system
system("cls")
print("\n" + "="*22 + " EMPLEADOS DE LA FABRICA " + "="*22 + "\n")

def calcular_jornal(nombre, dias_trabajados, domingos_trabajados, turno_semana, turno_domingo):
    # las tarifas por día y por turno, 
    tarifa_diurno_semana = 3000
    tarifa_nocturno_semana = 4000
    tarifa_diurno_domingo = 500
    tarifa_nocturno_domingo = 750

    total_devengado = 0

    # aqui se calcula por días trabajados en la semana
    if turno_semana == "diurno":
        total_devengado += min(dias_trabajados, 6) * tarifa_diurno_semana
    elif turno_semana == "nocturno":
        total_devengado += min(dias_trabajados, 6) * tarifa_nocturno_semana

    # Calcular por domingos trabajados
    if turno_domingo == "diurno":
        total_devengado += min(domingos_trabajados, 4) * tarifa_diurno_domingo
    elif turno_domingo == "nocturno":
        total_devengado += min(domingos_trabajados, 4) * tarifa_nocturno_domingo

    return total_devengado

nombre = input("Ingrese nombre y apellido del empleado: ")
print("---")


while True:
    turno_semana = input("Ingrese el turno trabajado en la semana (diurno/nocturno): ")
    if turno_semana.lower() in ["diurno", "nocturno"]:
        break
    else:
        print("Error: El turno debe ser 'diurno' o 'nocturno'. Inténtelo de nuevo.")
print("---")


while True:
    try:
        dias_trabajados = int(input("Ingrese la cantidad de días trabajados en la semana: "))
        if dias_trabajados <= 6:
            break
        else:
            print("Error: La cantidad de días trabajados no puede ser más de 6. Inténtelo de nuevo.")
    except ValueError:
        print("Error: Por favor, ingrese un número entero para la cantidad de días trabajados.")

print("---")


while True:
    turno_domingo = input("Ingrese el turno trabajado los domingos (diurno/nocturno): ")
    if turno_domingo.lower() in ["diurno", "nocturno"]:
        break
    else:
        print("Error: El turno debe ser 'diurno' o 'nocturno'. Inténtelo de nuevo.")
print("---")


while True:
    try:
        domingos_trabajados = int(input("Ingrese la cantidad de domingos trabajados en la semana: "))
        if domingos_trabajados <= 4:
            break
        else:
            print("Error: La cantidad de domingos trabajados no puede ser más de 4. Inténtelo de nuevo.")
    except ValueError:
        print("Error: Por favor, ingrese un número entero para la cantidad de domingos trabajados.")

print("---")

total_devengado = calcular_jornal(nombre, dias_trabajados, domingos_trabajados, turno_semana, turno_domingo)
print(f"Total devengado: {total_devengado} Córdobas")
print("*******************************************************************")
print("                             ¡Gracias!   ")
print("*******************************************************************")
