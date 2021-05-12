from claseManejador import Manejador
from claseMenu import  Menu
import csv
def test():
    print('test')
    archivo = open('Alumnos_test.csv')
    manejador.CargarLista(archivo)
    print('"Archivo Alumnos_test cargado"')
    manejador.LimpiarLista()  #se limpia la lista
    input()
if __name__ == '__main__':
    manejador = Manejador()
    p = input('Desea ejecutar test?  1:si  2:no  :')
    if p =='1':
        test()
    p = input('Desea cargar archivo Alumnos?  1:si  2:no  :')
    if p =='1':
        archivo = open('Alumnos.csv')
        manejador.CargarLista(archivo)
        print('"Archivo Alumnos cargado"')


    menu = Menu()
    bandera = False
    while not bandera:
        print("\n------------Menu------------\n1. Listar alumnos cuya cantidad de inasistencias supera la cantidad máxima de inasistencias permitidas \n2. Modificar la cantidad máxima de inasistencias permitidas.  \n3. Salir")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op, manejador)
        if op == 3:
            bandera = True


