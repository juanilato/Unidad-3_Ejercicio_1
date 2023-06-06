


class Carrera:
    __fechaInicio = "01/03"
    def __init__(self, codigo, nombre, duracion, titulo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__duracion = duracion
        self.__titulo = titulo
    def getNombre(self):
        return self.__nombre
    def getCod(self):
        return str(self.__codigo)
    def getDuracion(self):
        return self.__duracion
    def __str__(self):
        cadena = str(self.__codigo) + " "
        cadena += self.__nombre + " "
        return cadena
