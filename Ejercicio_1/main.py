from clase_manejador import ManejaFacultades
from clase_menu import Menu


if __name__ == "__main__":
    manejador = ManejaFacultades()
    manejador.carga()
    menu = Menu(2)
    lista = ["Código  de una facultad (nombre de la facultad, nombre  y duración carreras)", "Nombre de una carrera, mostrar código, nombre y localidad"]
    
    menu.IngresaOpcion(lista)
    cantidad = menu.getCantidad()
    menu.Muestra()
    
    opcion = int(input("Ingrese opcion "))
    while opcion != (cantidad + 1):
        if opcion == 1:
            codigo = int(input("Ingrese código "))
            cod = manejador.buscaCod(codigo)
            if cod !=-1:
                facultad = manejador.getFacultad(cod)
                print(facultad)
            else:
                print("No se encuentra la facultad ")
        elif opcion == 2:
            nombre_carrera = input("Ingrese nombre de la carrera ")
            manejador.buscaNombreCarrera(nombre_carrera)
        else:
            print("Ingreso opcion incorrecta")
        menu.Muestra()
        opcion = int(input("Ingrese opcion "))

    