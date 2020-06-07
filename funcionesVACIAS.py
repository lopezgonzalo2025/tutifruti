import random
import codecs


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


def cargarItems():
    print("en cargasItems")
    
    paises = (codecs.open("items/paises.txt",  "r", "utf-8").read()).split(",")
    colores = (codecs.open("items/colores.txt",  "r", "utf-8").read()).split(",")
    animales = (codecs.open("items/animales.txt",  "r", "utf-8").read()).split(",")
      
    listaDeTodo=[paises, colores, animales]
    
    return listaDeTodo
'''
    nombres=[]
    animales=[]
    colores=[]
    sustantivos_comunes=[]
    paises=[]
    marcas=[]
    cap_prov_arg=[]

    #Nombres
    nombres_txt=codecs.open("items/nombres.txt","r","utf-8")
    datos_nombres=nombres_txt.read()
    nombres.append(datos_nombres)
    nombres_txt.close()
    nombres=nombres[0].split(",")

    #Animales
    animales_txt=codecs.open("items/animales.txt","r","utf-8")
    datos_animales=animales_txt.read()
    animales.append(datos_animales)
    animales_txt.close()
    animales=animales[0].split(",")

    #Colores
    colores_txt=codecs.open("items/colores.txt","r","utf-8")
    datos_colores=colores_txt.read()
    colores.append(datos_colores)
    colores_txt.close()
    colores=colores[0].split(",")

    #Sustantivos
    sustantivos_comunes_txt=codecs.open("items/sustantivos comunes.txt","r","utf-8")
    datos_sustantivos_comunes=sustantivos_comunes_txt.read()
    sustantivos_comunes.append(datos_sustantivos_comunes)
    sustantivos_comunes_txt.close()
    sustantivos_comunes=sustantivos_comunes[0].split(",")

    #Paises
    paises_txt=codecs.open("items/paises.txt","r","utf-8")
    datos_paises=paises_txt.read()
    paises.append(datos_paises)
    paises_txt.close()
    paises=paises[0].split(",")

    #Marcas
    marcas_txt=codecs.open("items/marcas.txt","r","utf-8")
    datos_marcas=marcas_txt.read()
    marcas.append(datos_marcas)
    marcas_txt.close()
    marcas=marcas[0].split(",")

    #Capitales
    cap_prov_arg_txt=codecs.open("items/capitales y provincias Argentinas.txt","r","utf-8")
    datos_cap_pro_arg=cap_prov_arg_txt.read()
    cap_prov_arg.append(datos_cap_pro_arg)
    cap_prov_arg_txt.close()
    cap_prov_arg=cap_prov_arg[0].split(",")

    listaDeTodo=[nombres,colores,sustantivos_comunes,paises,marcas,cap_prov_arg]
    
    return listaDeTodo
'''