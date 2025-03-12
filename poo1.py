#Ejercicio 1
class Estudiante:
    def __init__(self, nombre, edad, curso, calificacion):
        self.__nombre = nombre
        self.__edad = edad
        self._curso = curso
        self.__calificacion = calificacion if 0 <= calificacion <= 100 else None

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def del_nombre(self):
        print("Eliminando el nombre...")
        del self.__nombre

    def mostrar_info(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"

    def asignar_calificacion(self, nueva_calificacion):
        self.__calificacion = nueva_calificacion

    def obtener_calificacion(self):
        return self.__calificacion

# Ejemplo de uso:
estudiante1 = Estudiante("Juan", 20, "Matemáticas", 85)
print(estudiante1.mostrar_info())
print("Calificación:", estudiante1.obtener_calificacion())

estudiante1.asignar_calificacion(90)
print("Nueva calificación:", estudiante1.obtener_calificacion())

# Eliminar el nombre
estudiante1.del_nombre()

#Ejercicio 2
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if 0 <= monto <= self.__saldo:
            self.__saldo -= monto

    def mostrar_saldo(self):
        return self.__saldo

# Ejemplo de uso:
cuenta1 = CuentaBancaria("Ana", 1000)
print("Saldo inicial:", cuenta1.mostrar_saldo())

cuenta1.depositar(500)
print("Saldo después del depósito:", cuenta1.mostrar_saldo())

cuenta1.retirar(300)
print("Saldo después del retiro:", cuenta1.mostrar_saldo())