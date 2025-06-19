def pregunta_1(texto: str) -> str:
    """
    Analiza el sentimiento de un texto sobre la Copa Mundial.

    Parametros:
    texto (str): Texto con varios comentarios.

    Retorna:
    str: Sentimiento del texto ('positivo', 'negativo' o 'neutro').
    """
    positivas = {"ganar", "excelente", "fantastico", "bueno", "asombroso", "amor", "increible"}
    negativas = {"perder", "malo", "terrible", "horrible", "odio", "pobre", "decepcionante"}

    palabras = texto.lower().split()
    pos_count = sum(palabra in positivas for palabra in palabras)
    neg_count = sum(palabra in negativas for palabra in palabras)

    if pos_count > neg_count:
        return 'positivo'
    elif neg_count > pos_count:
        return 'negativo'
    else:
        return 'neutro'


def pregunta_2(
    mapa: list[list[str]], fila: int, col: int, radio: int
) -> list[list[str]]:
    """
    Retorna el mapa despues de realizar la explosion segun el radio en la posicion de la fila y columna.
    Parametros:
        mapa  (list[list[str]]) :  El mapa
        fila  (int)             : El indice de la fila
        col   (int)             :  El indice de la columna
        radio (int)             : La longitud de la explosion
    Retorna:
        list[float] : La lista de respuesta
    """
    if mapa[fila][col] == '#':
        return mapa

    filas = len(mapa)
    columnas = len(mapa[0])

    def eliminar(f, c):
        if 0 <= f < filas and 0 <= c < columnas and mapa[f][c] != '#':
            mapa[f][c] = ' '

    eliminar(fila, col)

    for i in range(1, radio + 1):
        eliminar(fila - i, col)  # Arriba
        eliminar(fila + i, col)  # Abajo
        eliminar(fila, col - i)  # Izquierda
        eliminar(fila, col + i)  # Derecha

    return mapa


def pregunta_3(cursos: dict, codigo: int) -> list[str]:
    """
    Retorna una lista de cursos donde esta inscrito el codigo del estudiante
    Parametros:
        cursos  (dict) :  el diccionario de cursos y codigos de estudiantes
        codigo (int)   :  el codigo del estudiante a buscar
    Retorna:
        list[float] : La lista de respuesta
    """
    return [curso for curso, codigos in cursos.items() if codigo in codigos]


def pregunta_4(codigos: list[int]) -> list[list[int]]:
    """
    Aplica transformaciones a cada numero en la lista hasta que todos sean iguales a 1.

    Parametros:
        codigos (list[int]): Lista de numeros enteros que representan los codigos de desactivacion.

    Retorna:
        list[list[int]]: Lista de listas, cada una contiene la secuencia de transformaciones de un numero.
    """
    resultado = []

    for numero in codigos:
        secuencia = [numero]
        while numero != 1:
            if numero % 2 == 0:
                numero //= 2
            else:
                numero = numero * 3 + 1
            secuencia.append(numero)
        resultado.append(secuencia)

    return resultado