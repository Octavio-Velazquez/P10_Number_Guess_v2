import random

texto = "\n--------Este programa te invita a que adivines el número------------------\n"
texto += "---------------------elegido de forma aleatoria---------------------------\n\n"
print(texto)

def rango_mayor():
    """Esta función determina el número mayor que se va a usar dentro del rango de búsqueda del número aleatorio."""
    while True:
        try:
            numero_max = int(input("Indica el número máximo dentro del rango: "))
            while numero_max <= 1:
                print("Error! El número tiene que ser mayor a 1.")
                numero_max = int(input("Indica el número máximo dentro del rango: "))
        except ValueError:
            print("Error! Por favor de solo indicar números!")
        else:
            return numero_max

def adivina():
    """Adivina el número!"""

    numero_aleatorio = random.randint(1, rango_mayor())
    count = 0

    while True:
        try:
            adivina_numero = int(input("Adivina el número: "))
            count += 1
        except ValueError:
            print("Error! Por favor de solo escribir números.")
        else:
            if adivina_numero == numero_aleatorio:
                print(f"Adivinaste el número {numero_aleatorio}! Lo hiciste en {count} intentos!")
                break
            elif adivina_numero > numero_aleatorio:
                print("El número que has indicado es mayor. Favor de intentarlo con un número menor.")
            else:
                print("El número que has indicado es menor. Favor de intentarlo con un número mayor.")

adivina()