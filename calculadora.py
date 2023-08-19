operacion = input('que operacion vamos a hacer hoy? ')
operaciones_1 =  operacion

a = input('valor 1 ')
b = input('valor 2 ')
numeros = [int(a), int(b)]

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
operaciones = (suma, resta, multiplicacion, division)


if suma == 'suma':
    s = operaciones.pop(0)


