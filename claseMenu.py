from claseAlumno import Alumno
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1, 2:self.opcion2, 3:self.salir}

    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op,manejador):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))

        bandera=False
        while not bandera:
            if op == 1 or op == 2 or op== 3:
                bandera = True
            else:
                print('Opción no válida')
                op = int(input('Ingrese una opcion: '))
        func(manejador)

    def salir(self,manejador):
        print('Salir')

    def opcion1(self,manejador):
        anio = input('Ingrese el año: ')
        bandera = False
        while not bandera:
            if anio.isdigit():
                bandera = True
            else:
                anio = input('Error al ingresar año, intente denuevo: ')
        divi = input('Ingrese division: ')
        bandera = False
        while not bandera:
            if divi.isalpha():
                bandera = True
            else:
                divi = input('Error al ingresar año, intente denuevo: ')

        print('Alumno          Pocentaje ')
        for i in range(manejador.getLista()):

            alumno = manejador.getAlumno(i)
            if alumno.getAnio() == anio:
                if alumno.getDivision() == divi:
                    if Alumno.cantMaxInasistencia < alumno.getInasistencia():
                        porcentaje = (alumno.getInasistencia() * 100) / Alumno.totalClases
                        print('{}            {:.2f}%'.format(alumno.getNombre(), porcentaje))



    def opcion2(self,manejador):
        inasistencias = input('Ingrese nueva cantidad de inasistencias: ')
        bandera = False
        while not bandera:
            if inasistencias.isdigit():
                bandera = True
            else:
                inasistencias = input('Error al ingresar inasistencias, intente denuevo: ')
        Alumno.cantMaxInasistencia = int(inasistencias)
        print('Inasistencia maxima cambiada')