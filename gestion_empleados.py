class Empleado:
    empleados_registrados = []
    contador_empleados = 0  # Atributo de clase para contar empleados

    def __init__(self, nombre, puesto, salario):
        self.__nombre = nombre
        self.__puesto = puesto
        self.__salario = salario
        Empleado.empleados_registrados.append(self) # Aumentar el contador de empleados

    def __str__(self):  # Método de instancia
        return f"Nombre: {self.__nombre}, Puesto: {self.__puesto}, Salario: {self.__salario}"

    def contar_empleados(self,cls,empleados_registrados):
        for i in empleados_registrados:
            cls.contador_empleados +=1
        return print(f"Total empleados: {cls.contador_empleados}")
    @staticmethod
    def es_salario_valido(salario):
        if salario > 0:
            print("Salario válido")
        else:
            print("Salario inválido")

    def aumentar_salario(self, porcentaje):
        while porcentaje > 0:
            self.__salario += self.__salario * porcentaje / 100
            return print(f"El salario de {self.__nombre} ha sido aumentado en un {porcentaje}% y su nuevo salario es de {self.__salario}")
        else:
            return print("El porcentaje debe ser mayor a 0")
    def promocionar(self, nuevo_puesto):
      self.__puesto = nuevo_puesto
      return print(f"{self.__nombre} ha sido promocionada a {nuevo_puesto}")
      
    @classmethod
    def mostrar_empleados(cls):
        return "\n".join(str(empleado) for empleado in cls.empleados_registrados) or "No hay empleados registrados."

# Crear empleados
emp1 = Empleado("Ana", "Desarrolladora", 2000)
emp2 = Empleado("Carlos", "Analista", 1500)
#mostrar empleados
Empleado.mostrar_empleados()
promocionar = emp1.promocionar("Gerente")
#aumentar salario
emp2.aumentar_salario(15)
# Validar salario
emp2.es_salario_valido(emp2._Empleado__salario)


# Contar empleados
emp1.contar_empleados(Empleado,Empleado.empleados_registrados)


