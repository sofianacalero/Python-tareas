from os import system
system("cls")
print("===============================================================")
print("                     R E S T A U R A N T E          ")
print("===============================================================")
print('                           M E N U')
print('---------------------------------------------------------------')

menu = {
    "Pollo Frito": {"precio": 150, "tiempo_espera": "20 minutos"},
    "Sopa de Tortilla": {"precio": 120, "tiempo_espera": "15 minutos"},
    "Filete de Salmón": {"precio": 200, "tiempo_espera": "25 minutos"},
    "Ensalada César": {"precio": 100, "tiempo_espera": "10 minutos"}
}

print("Menú:")
for plato, detalles in menu.items():
    print(f"{plato}: ${detalles['precio']} - Tiempo de espera: {detalles['tiempo_espera']}")


while True:
    pedido = input("\n¿Qué platillo te gustaría degustar? Ingresa el nombre del plato: ")

    if pedido in menu:
        print(f"\nPedido exitoso: Has solicitado {pedido}. ¡Disfruta tu comida!")
        break
    else:
        print("\nLo siento, ese platillo no está disponible en nuestro menú. Por favor, elige otro.")
