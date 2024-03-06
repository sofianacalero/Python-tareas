def cordoba_to_dollar(amount):
    return amount / 36.82  # Tipo de cambio actualizado de córdoba a dólar

def dollar_to_cordoba(amount):
    return amount * 36.82

def euro_to_cordoba(amount):
    return amount * 39.97  # Tipo de cambio actualizado de euro a córdoba

def cordoba_to_euro(amount):
    return amount / 39.97

def main():
    while True:
        print("\nSeleccione la operación que desea realizar:")
        print("1. Córdoba a Dólar")
        print("2. Dólar a Córdoba")
        print("3. Euro a Córdoba")
        print("4. Córdoba a Euro")
        print("5. Salir")

        choice = input("Ingrese el número de la operación deseada: ")

        if choice == "1":
            amount = input("Ingrese la cantidad de córdobas: ")
            if amount.isdigit():
                amount = float(amount)
                print(f"{amount} córdobas son aproximadamente {cordoba_to_dollar(amount):.2f} dólares")
            else:
                print("Por favor, ingrese un número válido.")
        elif choice == "2":
            amount = input("Ingrese la cantidad de dólares: ")
            if amount.isdigit():
                amount = float(amount)
                print(f"{amount} dólares son aproximadamente {dollar_to_cordoba(amount):.2f} córdobas")
            else:
                print("Por favor, ingrese un número válido.")
        elif choice == "3":
            amount = input("Ingrese la cantidad de euros: ")
            if amount.isdigit():
                amount = float(amount)
                print(f"{amount} euros son aproximadamente {euro_to_cordoba(amount):.2f} córdobas")
            else:
                print("Por favor, ingrese un número válido.")
        elif choice == "4":
            amount = input("Ingrese la cantidad de córdobas: ")
            if amount.isdigit():
                amount = float(amount)
                print(f"{amount} córdobas son aproximadamente {cordoba_to_euro(amount):.2f} euros")
            else:
                print("Por favor, ingrese un número válido.")
        elif choice == "5":
            print("Gracias por utilizar el sistema de cambio de moneda.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
