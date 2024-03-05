from os import system
import random

system("cls")
print("=================================================")
print("                   T I E N D A          ")
print("=================================================")

def calcular_descuento(precio):
    numero_aleatorio = random.randint(1, 100)
    print("El número aleatorio escogido es:", numero_aleatorio)
    
    if numero_aleatorio < 60:
        descuento = 0.3  # 30% de descuento
    else:
        descuento = 0.5  # 50% de descuento
    
    monto_descuento = precio * descuento
    monto_final = precio - monto_descuento
    
    return monto_descuento, monto_final

def main():
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio >= 0:  # Verifica que el precio sea un número positivo
                break
            else:
                print("Error: Por favor, ingrese un precio válido mayor o igual a cero.")
        except ValueError:
            print("Error: Por favor, ingrese un precio válido.")
    
    descuento, monto_final = calcular_descuento(precio)
    
    print(f"El descuento aplicado es: {descuento:.2f}")
    print(f"El monto final a pagar es: {monto_final:.2f}")

if __name__ == "__main__":
    main()
