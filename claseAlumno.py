class Alumno:
    cantMaxInasistencia = 5
    totalClases = 120
    __nombre=0
    __anio=0
    __division=0
    __cantInasistencia=0


    def __init__(self,nombre,anio,division,cantInasistencia):
        self.__nombre = nombre
        self.__anio = anio
        self.__division = division
        self.__cantInasistencia = cantInasistencia

    def getInasistencia(self):
        return int(self.__cantInasistencia)
    def getNombre(self):
        return self.__nombre
    def getAnio(self):
        return self.__anio
    def getDivision(self):
        return self.__division

    @classmethod
    def getTotalClases(cls):
        return cls.totalClases

    @classmethod
    def getMaxInasistencia(cls):
        return cls.cantMaxInasistencia


