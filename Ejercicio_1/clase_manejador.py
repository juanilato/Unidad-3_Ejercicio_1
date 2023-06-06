import csv
from clase_facultad import Facultad
from clase_carrera import Carrera


class ManejaFacultades:
    __listaFacultades = []
    def agregaFacultad(self,facultad):
        self.__listaFacultades.append(facultad)
    def mostrarFacultades(self):
        for facultad in self.__listaFacultades:
            print(facultad)
    
    def carga(self):
        archivo = open("Facultades.csv")    
        reader = csv.reader(archivo, delimiter = ",")
        i = 1
        band = True
        for fila in reader:
            if int(fila[0]) == i:
                if band:
                    cadena = fila[3] + ", " + fila[4]
                    print(fila[1])
                    facultad = Facultad(int(fila[0]),fila[1], fila[2], cadena, fila[5])
                    self.agregaFacultad(facultad)
                    band = False
                else:
                    cadena = "titulo de " + fila[5] + ", " + fila[3]
                    carrera = Carrera(int(fila[1]),fila[2],fila[4], cadena)
                    facultad.ingresaCarrera(carrera)
            else:
                i += 1
                cadena = fila[3] + ", " + fila[4]
                facultad = Facultad(int(fila[0]),fila[1], fila[2], cadena, fila[5])
                self.agregaFacultad(facultad)
        del facultad
        archivo.close()
    def eliminaFacultad(self, codigo):
        del self.__lista[codigo-1]
        print("Se elimino la facultad")
    def buscaCod(self, codigo):
        i = 0
        while i < len(self.__listaFacultades) and self.__listaFacultades[i].getCod() != codigo:
            i += 1
        if i < len(self.__listaFacultades):
            cod = i
        else:
            cod = -1
        return cod
    
    def getFacultad(self, cod):
        return self.__listaFacultades[cod]
    
    def muestraDatos(self, cod, i):
        cadena = str(self.__listaFacultades[i].getCod()) + "."
        carrera = self.__listaFacultades[i].solicitaCarrera(cod)
        cadena += carrera.getCod() + " " + self.__listaFacultades[i].getNombre()
        cadena += " " + self.__listaFacultades[i].getLocalidad()
        print(cadena)

    def buscaNombreCarrera(self, nombre_carrera):
        i = 0
        band = False
        while i < len(self.__listaFacultades) and band == False:
            cod = self.__listaFacultades[i].buscaNombre(nombre_carrera)
            if cod != -1:
                band = True
            else:
                i += 1
        if band != False:
            self.muestraDatos(cod, i)    
        else:
            print("No se encontro la carrera solicitada")