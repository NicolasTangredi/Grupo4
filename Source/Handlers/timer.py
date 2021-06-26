import time as t

def actualizar(start_timer):
    """Devuelve un string con el tiempo transcurrido"""
    tiempo = int(t.time() - start_timer)

    return tiempo

def se_termino_el_tiempo (start_timer,user_time) -> bool:
    """Devuelve True si se termino el tiempo o False si aun no se termina"""

    tiempo = int(t.time() - start_timer)
    if user_time == tiempo:
        return True
    else:
        return False

def tiempo_restante(start_timer,user_time) -> int:
    """devuelve el tiempo que sobro de la partida"""
    tiempo = int(t.time() - start_timer)
    time_left = user_time - tiempo
    return time_left

