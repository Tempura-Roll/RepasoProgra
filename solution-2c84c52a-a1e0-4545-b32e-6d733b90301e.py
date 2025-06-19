def pregunta_1(lista:list[int])->dict:
    """
    Parametros:
        lista  (list[int]) :  lista de numeros enteros
    Retorna:
        dict : el diccionario de divisores y los numeros divisibles
    """
    resultado = {}
    for num in lista:
        for d in range(2,num+1):
            if num % d == 0:
                if d not in resultado:
                    resultado[d] = []
                resultado[d].append(num)
    return resultado


def pregunta_2(red_social: dict, nombre: str) -> list:
    """
    Parametros:
    - red_social (dict): Diccionario que representa la red social
    - nombre (str): Nombre del usuario.

    Retorno:
    - list: Lista de amigos en orden alfabetico.
    """
    if nombre not in red_social:
        return []
    amigos_directos = set(red_social[nombre])
    amigos_indirectos = set()

    for usuario, amigos in red_social.items():
        if nombre in amigos:
            amigos_indirectos.add(usuario)

    todos_los_amigos = amigos_directos.union(amigos_indirectos)
    return sorted(todos_los_amigos)


def pregunta_3(matriz: list[list[str]]) -> dict[str, int]:
    """
    Parametro:
        matriz (list[list[str]]): Una lista de listas de letras (caracteres).
    Retorna:
        dict[str, int]: Un diccionario donde las llaves son las letras y los valores son la cantidad de veces que aparece cada letra.
    """
    conteo = {}
    for fila in matriz:
        for letra in fila:
            conteo[letra] = conteo.get(letra,0)+1
    return conteo

def pregunta_4(reproducciones:dict[str, list[int]])->tuple:
    """
    Parametros:
        reproducciones (dict[str, list[int]]) : Diccionario con nombres de canciones y sus reproducciones semanales
    Retorna:
        tuple : Nombre de la cancion con el mayor promedio de reproducciones y su promedio
    """
    mayor_promedio = -1
    cancion_top = ""

    for cancion, lista in reproducciones.items():
        promedio = sum(lista)/len(lista)
        if promedio > mayor_promedio:
            mayor_promedio = promedio
            cancion_top = cancion

    return (cancion_top, round(mayor_promedio,2))