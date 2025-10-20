#CLASE 2 - Ejercicio 1
#NombreDeUsuario = input("Ingresa tu Nombre: ")
#EdadDeUsuario = input("Ingresa tu Edad: ")
#ProfesionDeUsuario = input ("Ingresa tu profesion: ")

#print("Hola " + NombreDeUsuario + ", tenés " + EdadDeUsuario + " años y tu profesion es " + ProfesionDeUsuario + ".")

#CLASE 2 - Ejercicio 2
#for i in range(2,21,2):
 #   print(i)

# Calculadora
#num1 = float(input("Ingresa el primer número: "))
#num2 = float(input("Ingresa el segundo número: "))
#operacion = input("Ingresa la operación (+, -, *, /): ")

#if operacion == '+':
#    resultado = num1 + num2
#elif operacion == '-':
#    resultado = num1 - num2
#elif operacion == '*':
#    resultado = num1 * num2
#elif operacion=='/':
#    if num2 != 0:
#        resultado = num1 / num2
#    else:
#        resultado = "error: división por cero"
#else:
#    resultado = "operación no válida"

#print(f"El resultado es: {resultado}")

# CLASE 3 - Ejercicio 1


def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

def calculadora_Simple(a, b, operacion):

    if operacion == '+':
       return sumar(a, b)
    elif operacion == '-':
        return restar(a, b)
    elif operacion == '*':
        return multiplicar(a, b)
    elif operacion == '/':
        return dividir(a, b)
    else:
         raise KeyError('La operación no es válida')
    

print("---Calculadora Simple---")
try:
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    operacion = input("Ingresa la operación (+, -, *, /): ")


    resultado = calculadora_Simple(a, b, operacion)
    print(f"El resultado es: {resultado}")
except ValueError:
    print("Error: Entrada inválida, por favor ingresa números válidos")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except KeyError as e:
    print(f"Error: {e}")