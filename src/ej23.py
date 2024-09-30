#
# Ejercicio 23
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro 
# correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
#


correo = input("Introduce tu correo electrónico: ")

posicion_arroba = correo.find('@')
nombre_usuario = correo[:posicion_arroba]

#nombre_usuario = correo.split('@')[0]

print(nombre_usuario + "@ceu.es")