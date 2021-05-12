import csv
from claseAlumno import Alumno
class Manejador:
    __lista = []

    def __init__(self):
        self.__lista = []

    def CargarLista(self,archivo):
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                nombre = fila[0]
                anio = fila[1]
                division = fila[2]
                cantInasistencia = fila[3]
                if nombre.isalpha():
                    if anio.isdigit():
                        if division.isalpha():
                            if cantInasistencia.isdigit():
                                alumno = Alumno(nombre, anio, division, cantInasistencia)
                                self.__lista.append(alumno)
                                print('Alumno creado')
                            else:print('Datos incorrecto de alumno, no fue creado')
                        else:print('Datos incorrecto de alumno, no fue creado')
                    else:print('Datos incorrecto de alumno, no fue creado')
                else:print('Datos incorrecto de alumno, no fue creado')

        archivo.close()

    def LimpiarLista(self):
        self.__lista.clear()

    def getLista(self):
        return len(self.__lista)

    def getAlumno(self,i):
        return self.__lista[i]