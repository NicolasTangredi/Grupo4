import PySimpleGUI as sg

def crear():

    Titulo = lambda text: sg.Text(text, font=('', 16))
    layout = [
        [Titulo("como jugar: ")],
        [sg.Text(
            """
            para jugar debera abrir el tablero de juego haciendo click en la
            boton "JUGAR", esto abrira el tablero de juego.
            una vez que estas listo se puede comenzar a jugar al clickear "Comenzar" 
            """
        )],
        [Titulo("Dificultades: ")],
        [sg.Text(
            """
            - FACIL: El tablero de juego sera pequeño, hay tiempo de sobra para encontrar las coincidencias y
                los elementos estan en parejas de solo 2 elementos. Pero los puntos por coincidencia sera de
                solo 10 puntos
            
            - MEDIO: El tablero de juego tiene un tamaño aceptable, el tiempo de juego es solo el suficiente y
                los elementos siguen siendo parejas de 2. En esta dificultad los puntos por coincidencia se 
                aumentan a 20
            
            - DIFICIL: El tablero es de un tamaño mayor, el tiempo de juego sera escaso y los elementos
                estan en parejas de 3. Pero los puntos por coincidencia son 30, que es lo mas alto posible 
            """
        )],
        [Titulo("Como se calculan los puntos?")],
        [sg.Text(
            """
            Las puntuaciones se calculan como los puntos que suma el jugador multiplica 
            por la cantidad total de aciertos, a esto se le suma el tiempo 
            sobrante en el cronometro

            La puntos sumados durante el juego depende de la dificultad elegida por el jugador 
            y cada equivocacion resta uno, dos o tes puntos a medida que aumenta la dificultad.

            funcion: total_aciertos * punt_total + tiempo_sobrante
            """
        )],
        [sg.Ok(auto_size_button=False)]
    ]

    return sg.Window("Ayuda", layout=layout)