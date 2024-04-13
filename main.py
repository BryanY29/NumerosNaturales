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

    def calcular_mcm(self, a, b):
        """
        Calcula el mínimo común múltiplo (mcm) de dos números utilizando el MCD calculado.

        Args:
            a (int): El primer número.
            b (int): El segundo número.

        Returns:
            int: El mínimo común múltiplo de a y b.
        """
        mcd = self.calcular_mcd(a, b)
        return (a * b) // mcd if mcd != 0 else 0

# Crear una instancia de la clase CalculadoraMCD
calculadora = CalculadoraMCD()

# Solicitar al usuario que ingrese los números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

# Calcular y mostrar el MCD y el mcm utilizando los métodos de la instancia
print("El MCD de", numero1, "y", numero2, "es:", calculadora.calcular_mcd(numero1, numero2))
print("El mcm de", numero1, "y", numero2, "es:", calculadora.calcular_mcm(numero1, numero2))
