# añadir la lista presentada
lista_eminencias = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes",
]
# definimos nombres de los 3 grupos existentes - posteriormente se usará para enlistar a sus representantes.
lista_magos = []
lista_cientificos = []
lista_otros = []

# creamos los criterios de selección mediante operadores lógicos
for eminencia in lista_eminencias:
    if eminencia == "Harry Houdini" or eminencia == "David Blaine" or eminencia == "Teller":
        lista_magos.append(eminencia)
    elif eminencia == "Newton" or eminencia == "Einstein" or eminencia == "Hawking":
        lista_cientificos.append(eminencia)
    else:
        lista_otros.append(eminencia)

# definimos prefijos solicitados
def hacer_grandioso(lista_magos):
    for i in range(len(lista_magos)):
        lista_magos[i] = "El gran " + lista_magos[i]
    return lista_magos

# definimos solicitud para imprimir nombres de las personas
def imprimir_nombres(lista_nombres):
    for persona in lista_nombres:
        print(persona)

# finalmente realizamos solicitudes de imprimir nombres, lista actualizada con los grandiosos magos
# y listas de cientificos y otros con las eminencias correspondientes
imprimir_nombres(lista_eminencias)
lista_magos = hacer_grandioso(lista_magos)
imprimir_nombres(lista_magos)
imprimir_nombres(lista_cientificos)
imprimir_nombres(lista_otros)