#Son una secuencia de caracteres que forman un patron de busqueda, sirven para el procesamiento de datos
# ejemplo, corroborar un correo electronico, cadena de caracteres dentro de un texto, 
# numero de coincidencias dentro de un texto
#mas info "regular expresions in Python" en google

import re

cadena="Vamos a aprender expresiones regulares"

# Metodo search

textoAbuscar="aprender"


'''
if re.search(textoAbuscar,cadena) is not None:
    print("He encontrado 1 texto")

else :
    print("Sin resultados")

#print(re.search("aprender", cadena))
'''
'''
textoEncontrado = re.search(textoAbuscar, cadena)

print(textoEncontrado.start()) # Devuelve el primer lugar en la cadena donde comienza el texto encontrado

print(textoEncontrado.end()) # Devuelve donde finaliza

print(textoEncontrado.span()) # Devuelve los dos datos

print(re.findall(textoAbuscar, cadena))# Devuelve la palabra por la cantidad de veces que se repita 
'''
# METECARACTERES--------------- 
# Sirve por ejemplo cuando trabajamos con dominios, nombres de paginas, si alguno termina en .com o .ar.o .net por ejemplo etc.
# Anclas
'''
lista_nombres=['Ana Gomez',
                'Matia Martin',
                'Marcos Mele',
                'Maria Dias']

for elemento in lista_nombres:
    if re.findall('^Ana', elemento):   #El simbolo ^ controla cual de los elementos de la lista comienza con la palabra indicada
         print(elemento)

for elemento in lista_nombres:
    if re.findall('Mele$', elemento): # El simbolo $ busca el nombre pero por el que termina
         print (elemento)

for elemento in lista_nombres:
    if re.findall('[ñ]', elemento): # Busca y devuelve la palabra o cadena que contenga la ñ
        print(elemento)          

for elemento in lista_nombres:
    if re.findall('niñ[oa]s', elemento): # forma de buscar dos cosas 
        print(elemento)

for elemento in lista_nombres:
    if re.findall('cami[oó]n', elemento): # cuando buscamos una palabra que puede aparecer con tilde o sin
        print(elemento)        
'''
#  RANGOS (muy utiles para filtrar registros) ----------------------
'''
lista_nombres=['Ana',
                'Matias',
                'Lucas',
                'Elias',
                'Xanti']

for elemento in lista_nombres:
    if re.findall('[o-t]', elemento):   #buscar nombres que tengan letras en un rango entre la o y la t 
        print(elemento)

for elemento in lista_nombres:
    if re.findall('^[O-T]', elemento): # Busca con la letra que comienza. $ Para saber con cual termina
        print(elemento)
'''

# Funciones Match ---------------------------------------------------

  #( busca si hay coincidencias al comienzo de una cadena de texto, siempre busca al principio )
nombre1="Sandra Mirra"
nombre2="Maria Lopez"
nombre3="Antonio Gomez"

#es sensible a mayusculas y minusculas por eso usamos como 3er parametro re.ignorecase

if re.match("Sandra", nombre1, re.IGNORECASE):
    print("hemos encontrado el nombre")

else:
    print("no lo hemos encontrado") 


nombre4="Lara"
nombre5="Sara"

#if re.match(".ara", nombre1, re.IGNORECASE): busca reemplazando la primer letra


cadena1="Sandra Mirra"
cadena2="9874598"
cadena3="a9874598"

if re.match("\d", cadena2):   #busca un dugito en la cadena
    print("hemos encontrado el nombre")

else:
    print("no lo hemos encontrado") 



# Funcion Search -----------------------------------
#    (busca en toda la cadena de texto a ver si el patron se encuentra o no, no solo al principio)
# BUSCAR EN INTERNET POR MAS FUNCIONES DE BUSQUEDA EN CASO NECESARIO

nombre6="Sandro Mirra"
nombre7="Mariano Lopez"
nombre8="Antonia Gomez"



if re.search("Sandro ", nombre7): 
    print("hemos encontrado el nombre")

else:
    print("no lo hemos encontrado")
















