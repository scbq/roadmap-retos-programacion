import math
'''
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 '''

 # Funcion basica  sin parametros ni retorno
def saludar():
    print('Hola!!!!!')
saludar()

#funcion con parametros
def sumar(a, b):
    print(a + b)
sumar(10, 10)

# Funcion con retorno
def area_circulo(radio):
    return math.pi * (radio ** 2)
resultado = area_circulo(10)
print("El área del círculo es: ", resultado)

# Función dentro de otra
def fuera(x):
    def adentro(y):
        return x + y
    return adentro
funcion_dentro = fuera(5)
print("Resultado de la función dentro de otra:", funcion_dentro(7))

# Función incorporada len()
texto = 'Hola a Todos'
print("La longitud del texto es: ", len(texto))

# Variables locales y globales
animal = 'Perro' #Variable global

def mostrar_animal():
    animal = 'Gato' # Variable local
    print(animal)
mostrar_animal() # Gato
print(animal) # Perro

# Ejercicio extra
def cadena_texto(texto1, texto2):
    cont = 0

    for i in range(1, 100):
        cadena = ''
        if i % 3 == 0:
            cadena += texto1
            cont +=1
        if i % 5 == 0:
            cadena += texto2
            cont += 1
        if cadena:
            print(cadena)
        else:
            print(i)
    return cont
respuesta = cadena_texto('Fizz', 'Buzz')
print("Contador de Fizz o Buzz: ", respuesta)