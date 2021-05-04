from .Handlers import elegir_datos
from .Componentes import menu_login


# programa principal
def run():

    elegir_datos.elegir_criterio()
    menu_login.start()
