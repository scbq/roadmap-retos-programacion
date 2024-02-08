# Ejemplos de operadores aritméticos
num1 = 10
num2 = 3

# Suma
print('---- SUMA ----')
print(num1 + num2)
print('--------------')

# Resta
print('---- resta ----')
print(num1 - num2)
print('--------------')

# Multiplicación
print('---- MULTIPLICACIÓN ----')
print(num1 * num2)
print('--------------')

# División
print('---- DIVISIÓN ----')
print(num1 / num2)
print('--------------')

# Modulo
print('---- MODULO ----')
print(num1 % num2)
print('--------------')

# Exponente
print('---- EXPONENTE ----')
print(num1 ** num2)
print('--------------')


# Operadores Lógicos
valor_logico1 = True
valor_logico2 = False

print(valor_logico1 and valor_logico2) # AND
print(valor_logico1 or valor_logico2) # OR
print(not valor_logico1)               # NOT

# Operadores de comparación
a = 10
b = 5

print(a > b) # Mayor que
print(a < b) # Menor que
print(a <= b) # Menor o igual que
print(a >= b) # Mayor o igual que
print(a == b) # Igual que
print(a != b) # No es igual a

# Estructura condicional IF - ELIF - ELSE
x = int(input('Ingrese un número entero: '))

if x > 0:
  print("Positivo")  
elif x < 0:
  print("Negativo")
else:
  print("Cero")

# Estructura repetitiva FOR
frutas = ["Manzana", "Pera", "Naranja"]

for fruta in frutas:
  print(fruta)

# Estructura repetitiva WHILE
cont = 0

while cont < 5:
  print(cont)
  cont += 1
