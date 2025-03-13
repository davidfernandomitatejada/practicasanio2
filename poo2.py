#ejercicio Empleados
class Empleado:
    empleados_registrados = [] 

    def __init__(self, nombre, edad, salario):
        self._nombre = nombre
        self._edad = edad if edad >= 18 else 18
        self._salario = salario if salario >= 0 else 0
        Empleado.empleados_registrados.append(self) 

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if valor >= 18:
            self._edad = valor
        else:
            raise ValueError("La edad debe ser mayor o igual a 18.")

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor >= 0:
            self._salario = valor
        else:
            raise ValueError("El salario no puede ser negativo.")

    def calcular_aporte_asegurado(self):
        return self._salario * 0.1271

    def calcular_liquido_pagable(self):
        return self._salario - self.calcular_aporte_asegurado()

    def calcular_aporte_patronal(self):
        return self._salario * 0.1671

    def __str__(self):
        return (f"Empleado: {self._nombre}, Edad: {self._edad}, Salario: {self._salario}, "
                f"Aporte Asegurado: {round(self.calcular_aporte_asegurado(),2)}, "
                f"Líquido Pagable: {round(self.calcular_liquido_pagable(),2)}, "
                f"Aporte Patronal: {round(self.calcular_aporte_patronal(),2)}")

    @classmethod
    def mostrar_empleados(cls):
        if not cls.empleados_registrados:
            print("No hay empleados registrados.")
        else:
            for empleado in cls.empleados_registrados:
                print(empleado)

empleado1 = Empleado("Juan Pérez", 25, 3000)
empleado2 = Empleado("Ana Gómez", 30, 3500)
empleado3 = Empleado("Luis Torres", 22, 2800)

empleado2.edad= 24
empleado3.salario = 3200
Empleado.mostrar_empleados()