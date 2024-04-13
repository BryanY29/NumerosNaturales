
class CalculadoraMCD:
    def calcular_mcd(self, a, b):
        """
        Calcula el máximo común divisor (MCD) de dos números utilizando el algoritmo de Euclides.

        Args:
            a (int): El primer número.
            b (int): El segundo número.

        Returns:
            int: El máximo común divisor de a y b.
        """
        while b != 0:
            a, b = b, a % b
        return a

# Crear una instancia de la clase CalculadoraMCD
calculadora = CalculadoraMCD()

# Solicitar al usuario que ingrese los números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Calcular y mostrar el MCD utilizando el método de la instancia
print("El MCD de", numero1, "y", numero2, "es:", calculadora.calcular_mcd(numero1, numero2))
