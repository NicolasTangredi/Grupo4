import time as t

def actualizar(start_timer):
    """Devuelve un string con el tiempo transcurrido"""
    tiempo = t.time() - start_timer
    timer = 'Tiempo:' f'{round(tiempo // 60):02d}:{round(tiempo % 60):02d}'

    return timer
