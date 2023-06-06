


class Facultad:
    __carreras = []

    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
    def __del__(self):
        for carrera in self.__carreras:
            del carrera
    def ingresaCarrera(self, carrera):
        self.__carreras.append(carrera)

    def getNombre(self):
        return self.__nombre
    def __str__(self):
        cadena = self.__nombre + " "
        cadena += self.__direccion + " "
        cadena += self.__localidad + " "
        cadena += self.__telefono + " "
        for carrera in self.__carreras:
            cadena += carrera.getNombreFacultad() + " "
            cadena += " \n"
            cadena += carrera.getNombre()
        return cadena