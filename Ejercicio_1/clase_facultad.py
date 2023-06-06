


class Facultad:
    def __init__(self, codigo, nombre, direccion, localidad, telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carreras = []
    def __del__(self):
        for carrera in self.__carreras:
            del carrera
    def ingresaCarrera(self, carrera):
        self.__carreras.append(carrera)
    def getCod(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getLocalidad(self):
        return self.__localidad
    def __str__(self):
        cadena = self.__nombre + " "
        for carrera in self.__carreras:
            cadena += " \n"
            cadena += carrera.getNombre() + ", duración: "
            cadena += carrera.getDuracion()
        return cadena
    def buscaNombre(self, nombre_carrera):
        i = 0
        print(len(self.__carreras))
        while (i < len(self.__carreras)) and self.__carreras[i].getNombre() != nombre_carrera:
            i += 1
        if i < len(self.__carreras):
            cod = i
        else:
            cod = -1
        return cod
    def solicitaCarrera(self, cod):
        return self.__carreras[cod]