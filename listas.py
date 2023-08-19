#vamos a practicar a listas

lista_1 = ['sebastian', 'pablo', 'duvan', 'laura']
otra_lista = [16, 15, 17, 15, 16]

nombres = lista_1
edades = otra_lista

datos_personales = ['sebastian', 'lopez', 16, 1.77]
nombre, apellido, edad, altura = datos_personales

print(f'hola mi nombre es {nombre} y mido {altura}')



print(lista_1[1])
print(lista_1[-1])# va hacia atras, es decir da laura
#print(lista_1[-5]) no puede hacer eso pq da error, ya que excede el numero de strings dentro de la lista

print(f'Estos son los nombres que se encuentran en la lista:{nombres}')
print(nombres[0], edades[0])

print(otra_lista.count(15))#seala el numero de veces que este un mismo valor
#concatenar listas
print(lista_1 + otra_lista)

lista_1.append('pablo') #append es para poner mas elementos dentro de una lista siguiendo el orden anterior
print(lista_1)
lista_1.insert(0, ('willow'))#se utiliza para insertar un valor ya sea str o int en una posicion determinada por nosotros
print(lista_1)
lista_1.remove('sebastian')#como su nombre lo indica lo utilizamos para borrar un valor ya puesto en la tabla
print(lista_1)


lista_2 = ['celulares', 'pantallas', 'tablets', 1980, 1975, 2000]
lista_2.pop()#quita un valor de las listas y ponerlo en otra

valor_guardado = lista_2.pop(1) #podemos guardar elementos de las listas en variables
print(lista_2.pop(1))
print(valor_guardado)
print(lista_2)

lista_3 = [10, 20, 30, 40, 50, 60]

del lista_3[2] #para eliminar elementos y no volverlos a retonar como .pop
print(lista_3)

lista_4 = [2001, 2002, 2003, 2004]
lista_5 = lista_4.copy()# se usa para copiar todos los lementos de una tabla
lista_4.clear()
lista_4 = ['hola', 'como','estas']
print(lista_4, lista_5)

my_new_list = ['arroz', 'huevos', 'carne']
my_new_list.reverse()#lo pone la ordenacion diferente
print(my_new_list)

my_new_list.sort()#NORMALMENTE PONE LAS COSAS EN ORDEN ALFABETICO O de menor a mayor
print(my_new_list)

print(my_new_list[0:1])#para crear un tipo de sublistas
part_my_new_list = my_new_list[0:1]
print(type(part_my_new_list))





