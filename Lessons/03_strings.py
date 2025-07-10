# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea" # \n salto de linea
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"  # \t tabulacion
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
# {} are the placeholders using .format

print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age)) 
# "%s" are the placeholders using %
# "%d" para enteros

print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")
# este ultimo es inferencia de datos, la f es para formatear las variables

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3] # de caracter 1 a 3, sin contar la 3
print(language_slice)

language_slice = language[1:] # de caracteres sin contar la 0 hasta el final
print(language_slice)

language_slice = language[-2] # solo la penultima (la 2 desde el final)
print(language_slice)

language_slice = language[0:6:2] # seleccionar caracteres que va mostrar ordenadamente
print(language_slice)

# Reverse

reversed_language = language[::-1] # al reves
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t")) # contar las t's
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo
