import random

def unaAlAzar(abc):
    letraElegida = random.choice(abc)
    return letraElegida
    # return "a"

def esCorrecta(palabraUsuario, letra, item, items, listaDeTodo):
    if (palabraUsuario[0] == letra and palabraUsuario in listaDeTodo[items.index(item)]):
        return 10 
    return -5    


def juegaCompu(letraAzar, listaDeTodo, nivel):
    seguir = True
    resultado = []
    chances = 0
    for lista in listaDeTodo:
        seguir=True
        resultado.append("...")
        while seguir == True and chances <= nivel:
        # Segun el nivel la pc tiene más o menos posibilidades de encontrar la palabra correcta
            palabra=random.choice(lista)
            chances += 1
            if palabra[0] == letraAzar and seguir == True:
                resultado.pop(-1)
                resultado.append(palabra)
                seguir=False
    return resultado





