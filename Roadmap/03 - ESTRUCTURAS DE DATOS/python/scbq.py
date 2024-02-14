import re

'''
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
'''
# # Listas
# numeros = [5, 2, 8, 3, 7]
# numeros.append(6) # Inserción
# numeros.insert(2, 9) # Inserción en posición específica
# numeros.pop(0) # Borrar elemento
# numeros.remove(3) # Eliminar elemento
# numeros.sort() # Ordena la lista

# print(numeros)

# # Conjuntos
# s = {1, 5, True, 'Texto'}
# s.add(10)
# s.discard(5)

# print(s)

# # Diccionario
# productos = {'Camiseta': 15, 'Pantalon': 27, 'Zapatos': 42}
# productos['Chaqueta'] = 22 # Agregar  nuevo producto
# del productos['Camiseta'] # Eliminar producto existente
# productos['Pantalon'] += 3 # Modificar producto
# print(productos)


# Función mostrar menú
def mostrar_menu():
    print('AGENDA TELEFÓNICA')
    print('-----------------')
    print('1. Añadir Contacto')
    print('2. Buscar Contacto')
    print('3. Actualizar Contacto')
    print('4. Eliminar Contacto')
    print('5. Mostrar Todos Los Contactos')
    print('0. Salir')

# Función elegir opción
def elegir_opcion():
    opcion = int(input('Ingrese una opción: '))

    try:
        opcion = int(opcion)
    except:
        print('Debe ingresar un número')
        return elegir_opcion()
    
    if opcion < 0 or opcion > 5:
        print('Opción inválida')
        return elegir_opcion
    
    return opcion

# Función menú principal
def main():
    ejecutando = True

    while ejecutando:
        mostrar_menu()
        opcion = elegir_opcion()

        if int(opcion) == 1:
            nombre = input('Ingrese el nombre: ')
            telefono = input('Ingrese el teléfono: ')
            anadir_contacto(nombre,telefono)

        elif opcion == 2:
            nombre = input( "Buscar por nombre: ")
            encontrado  = buscar_contacto(nombre)

            if encontrado:
                print('Información de contacto: ')
                print(encontrado)

            else:
                print('No se encontró el contacto')
            

        elif opcion == 3:
            actualizar_contacto(contactos)

        elif opcion == 4:
            eliminar_contacto(contactos)

        elif opcion == 5:
            mostrar_contactos(contactos)

        elif opcion == 0:
            ejecutando = False

        else:
            print('Opción incorrecta, vuelva a intentarlo.')

    print('Hata pronto!')

# Función añadir contacto
def anadir_contacto(nombre, telefono):
    
    telefono = validar_telefono()
    
    contactos.append({
         "Nombre": nombre,
         "Telefono": telefono  
    })
    
    print("Contacto agregado!")

#Función Buscar Contacto
def buscar_contacto(nombre):
    resultados = []
    for c in contactos:
        if c['Nombre'].lower() == nombre.lower():
            resultados.append(c)

    if len(resultados) > 0:
        return resultados
    
    return 'No se encontraron contactos'

# Función Actualizar Contacto
def actualizar_contacto(contactos):

    nombre = input("Nombre contacto a modificar: ")

    for contacto in contactos:
        if contacto["Nombre"].lower() == nombre.lower():

            nuevo_tel = validar_telefono()
            
            contacto["Telefono"] = nuevo_tel
            print("Contacto actualizado")
            
            return

    print("No existe contacto con ese nombre")

# Función validar número de teléfono
def validar_telefono():

    while True:
        numero = input("Número teléfono: ")
        if re.match("\d{11}", numero): 
            return numero
        else:
            print("Formato incorrecto, ingrese 11 dígitos")
    

# Función eliminar Contacto
def eliminar_contacto(contactos):

    nombre = input("Ingrese el nombre del contacto a eliminar: ")

    for i, contacto in enumerate(contactos):
        
        if contacto['Nombre'].lower() == nombre.lower():
            
           # Pedir confirmación 
           eliminar = input("¿Confirma que desea eliminar el contacto? (S/N): ")
           if eliminar.upper() == "S":

               del contactos[i]  
               print("Se eliminó el contacto")
               return

    print("No existe un contacto con ese nombre")

# Función mostrar contactos
def mostrar_contactos(contactos):
    print('Contactos'.center(50, '-'))
    for c in contactos:
        telefono = c.get('Telefono', '')
        nombre = c.get('Nombre', '')
        print(f'| {nombre:<30} | {telefono:>10} |')
    print('-'*50)

# Tu agenda de contactos
contactos = []

main()
