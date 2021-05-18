rango_inferior = int(input('Ingresa un rango inferior: '))
rango_superior = int(input('Ingresa un número mayor al anterior: '))
comparacion = int(input('Ingresa un número de comparación: '))

while (comparacion < rango_inferior) or (comparacion > rango_superior):
    print('El número ' + str(comparacion) + ' no está en el rango')
    comparacion = int(input('Prueba con otro número: '))
print( 'El número ' + str(comparacion) + ' sí está en el rango')