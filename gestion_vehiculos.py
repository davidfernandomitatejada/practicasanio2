class Vehiculo:
    autos_creados = 0
    autos_registrados = []
    def __init__(self, marca, modelo, anio,velocidad):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad = velocidad
        Vehiculo.autos_registrados.append(self)
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Velocidad: {self.velocidad}"
    @classmethod
    def mostrar_autos(cls):
        return "\n".join(str(auto) for auto in cls.autos_registrados) or "No hay autos registrados."
    @staticmethod
    def velocidad_segura(velocidad):
        if velocidad > 0 and velocidad <= 100:
            print("Velocidad segura")
        else:
            print("Velocidad insegura")
    @classmethod
    def contar_autos(cls):
        for i in cls.autos_registrados:
            cls.autos_creados +=1
        return print(f"Total autos: {cls.autos_creados}")

auto1 = Vehiculo("Toyota", "Corolla", 2015, 120)
auto2 = Vehiculo("Hyundai", "Accent", 2018, 90)

print(Vehiculo.mostrar_autos())
Vehiculo.velocidad_segura(auto1.velocidad)
Vehiculo.velocidad_segura(auto2.velocidad)
Vehiculo.contar_autos()
