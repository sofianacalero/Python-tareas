class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "No se puede dividir por cero."

def obtener_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Por favor, ingrese un número entero válido.")

def main():
    num1 = obtener_numero("Ingrese el primer número entero: ")
    num2 = obtener_numero("Ingrese el segundo número entero: ")
    
    calculadora = Calculadora(num1, num2)
    
    print("Suma:", calculadora.suma())
    print("Resta:", calculadora.resta())
    print("Multiplicación:", calculadora.multiplicacion())
    print("División:", calculadora.division())

if __name__ == "__main__":
    main()
