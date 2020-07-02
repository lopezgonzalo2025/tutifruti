import random
import codecs


def unaAlAzar(abc):
    letraElegida = random.choice(abc)
    return letraElegida


def esCorrecta(palabraUsuario, letra, item, items, listaDeTodo):
    palabraUsuario = palabraUsuario.lower()
    indiceDelItem = items.index(item)
    opcionesDelItem = listaDeTodo[indiceDelItem]

    if (palabraUsuario[0] == letra and palabraUsuario in opcionesDelItem):
        return 10
    return -5


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



def guardar_puntajes(puntajes):
    historial = open("datos/historial.txt", "w")
    for puntaje, tiempo in puntajes:
        historial.write(str(puntaje)+","+tiempo+"\n")
    historial.close()


def recuperar_puntajes():
    puntajes = []
    historial = open("datos/historial.txt", "r")

    for linea in historial:
        puntaje, tiempo = linea.rstrip("\n").split(",")
        puntajes.append((int(puntaje),tiempo))
    historial.close()

    return puntajes

def cargarItems(items):
    i = -1
    listaDeTodo=[]    
    for item in items:
        lista = []
        txtFile = codecs.open("items/" + str(item) + ".txt","r","utf-8")
        datosTxt = txtFile.read()
        lista.append(datosTxt)
        txtFile.close()
        lista = lista[0].split(',')
        listaDeTodo.append(lista)
        lista = []    
        
        #Print para ver prolijamente cada item por consola
        i += 1
        print(listaDeTodo[i])
        print("")
        print("")
        

    return listaDeTodo