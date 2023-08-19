#se definen atravez de parentesis ()
#RECUERDA QUE LAS TUPLAS SON INMUTABLES ES DECIR QUE SON PARECIDAS A UN CONST
my_new_tupla = ('sebas', 'san pedro', 16, 1.77, 16)
print(my_new_tupla.count(16))
print(type(my_new_tupla))

print(my_new_tupla.index(1.77))#me indica donde esta ese indice
print(my_new_tupla[1:3])

my_new_tupla_update = ('Juan', 'sebastian', 'lopez', 'hernandez', 16)
print(type(my_new_tupla_update))
my_new_tupla_update = list(my_new_tupla_update) 
my_new_tupla_update.insert(4, 'hola')
print(my_new_tupla_update)
my_new_tupla_update[5] = 17
print(my_new_tupla_update)

my_new_tupla.copy()
del my_new_tupla#esto sirve paraborrar completamente la variable que habiamos asignado como tupla
#print(my_new_tupla)NameError: name 'my_new_tupla' is not defined

