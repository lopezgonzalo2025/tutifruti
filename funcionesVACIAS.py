import random

def unaAlAzar(abc):
    #letraElegida = random.choice(abc)
    #return letraElegida
    return "e"

def esCorrecta(palabraUsuario, letra, item, items, listaDeTodo):
    palabraUsuario = palabraUsuario.lower()
    if (palabraUsuario[0] == letra and palabraUsuario in listaDeTodo[items.index(item)]):
        return [10, 0] 
    return [0, -5]    


def juegaCompu(letraAzar, listaDeTodo):
    listaLetra = []
    resultado = []

    for idx in range(len(listaDeTodo)):
        resultado.append("...")

        for palabra in listaDeTodo[idx]:
            if palabra[0] == letraAzar:
                listaLetra.append(palabra)

        if len(listaLetra)>0:
            resultado.pop(-1)
            resultado.append(random.choice(listaLetra))
            listaLetra=[]
    return resultado


def cargarItems(listaDeTodo):
    listaDeTodoModificada = []
    opcion = ""    
    idx = 0
    for item in listaDeTodo:
        listaDeTodoModificada.append([])
        for string in item:
            for char in string:
                if char != ",":
                    opcion += char
                else:
                    listaDeTodoModificada[idx].append(opcion)
                    opcion = ""
        idx += 1
    return listaDeTodoModificada


def guardar_puntajes(puntajes):
    archivo = open("datos/historial.txt", "w")
    for nombre, puntaje, tiempo in puntajes:
        archivo.write(nombre+","+str(puntaje)+","+tiempo+"\n")
    archivo.close()


def recuperar_puntajes():
    puntajes = []
    historial = open("datos/historial.txt", "r")
    
    for linea in historial:
        nombre, puntaje, tiempo = linea.rstrip("\n").split(",")
        puntajes.append((nombre,int(puntaje),tiempo))
    historial.close()
    
    return puntajes








