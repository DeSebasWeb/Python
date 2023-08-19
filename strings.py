vaso = 'hola'
vasoa_2 = 'como estas'
print(vaso,vasoa_2)

#para hacer  un salto de lineas se debe hacer con \n

print('Hola como estas, esto es un string con saltos de linea\nahora si es un salto de linea ')
#tabulacion de un string \t

print('\t hola tabulador')
#formateo de strings 
nombre = 'sebas' #para strings es %s
edad = 16 # para valores int se pone %d
colegio = "San Pedro"

#hay dos maneras

print('Hola , mi nombre es {} tengo {} años, y soy del colegio {}'.format(nombre, edad, colegio))
print('hola, mi nombre es %s, tengo %d años, y soy del colegio %s' %(nombre, edad, colegio))
print(f'hola mi nombre es {nombre} y tengo {edad} años, actualmente estudio en el colegio {colegio}')
print(type(f'{edad}'))
#desempaquetado de caracteres 

#si intentamos poner en dos variables solo un valor, se va a distribuir por carcacteres cada variable, es decir :

dos_variables = 'hola'
a, b, c, d = dos_variables

#print(a, b) si dejo esto asi da error, entonces debemos crear una variable para cada caracter

print(a, b, c, d)

#division
division_variables = dos_variables[1:3]
print(division_variables)

division_variables_2 = dos_variables[1:]
print(division_variables_2)

resta_variable = dos_variables[-3]
print(resta_variable)

#reverso de strings

reverso_dos_variables = dos_variables[::-1]
print(reverso_dos_variables)

#funciones

print(dos_variables.capitalize())#poner la primera en mayuscula
print(dos_variables.upper())#pone todo en mayuscula

print(dos_variables.count('hola '))#VER COMO FUNCIONA ESTA FUNCION 

print(dos_variables.isnumeric())# nos dice si la cadena de texto es un numero y lo representa en la terminar como un valor bool
print('54'.isnumeric())
print('CADENA'.lower())#poner todo en minuscula
print('CAdena'.lower().isupper())#utilizamos el is para preguntarle a la consola si esta en mayuscula o minuscula, depende de lo que necesitemos
print(dos_variables.startswith('h'))#con este se pregunta si el string empieza con una h

