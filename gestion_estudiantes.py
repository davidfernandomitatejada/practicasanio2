class Estudiante:
    estudiantes_matriculados = {} 

    def __init__(self, nombre, edad, grado, promedio):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.promedio = promedio  

        Estudiante.estudiantes_matriculados[nombre] = {
            "edad": edad,
            "grado": grado,
            "promedio": promedio
        }

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}, Promedio: {self.promedio}"

    @classmethod
    def mostrar_estudiantes(cls):
        if not cls.estudiantes_matriculados:
            return "No hay estudiantes registrados."
        
        return "\n".join(
            f"Nombre: {nombre}, Edad: {datos['edad']}, Grado: {datos['grado']}, Promedio: {datos['promedio']}"
            for nombre, datos in cls.estudiantes_matriculados.items()
        )

    @staticmethod
    def esta_aprobado(promedio):
        print("Aprobado" if promedio >= 51 else "Reprobado")

    @classmethod
    def contar_estudiantes(cls):
        print(f"Total estudiantes: {len(cls.estudiantes_matriculados)}") 
    
    @classmethod
    def actualizar_notas(cls, nombre, nuevas_notas):
        if nombre in cls.estudiantes_matriculados:
            cls.estudiantes_matriculados[nombre]["promedio"] = nuevas_notas
            print(f"El promedio de {nombre} ha sido actualizado a {nuevas_notas}")
        else:
            print(f"No se encontró al estudiante {nombre}")

    @classmethod
    def mejor_promedio(cls):
        if not cls.estudiantes_matriculados:
            print("No hay estudiantes registrados.")
            return

        mejor_nombre = None
        mejor_promedio = -1  

        for nombre, datos in cls.estudiantes_matriculados.items():
            if datos["promedio"] > mejor_promedio:
                mejor_promedio = datos["promedio"]
                mejor_nombre = nombre

        print(f"El mejor promedio es {mejor_promedio}, de {mejor_nombre}")

estudiante1 = Estudiante("ALex Moscoso", 16, "Noveno", 80)        
estudiante2 = Estudiante("Ana López", 12, "Sexto", 40)
estudiante3 = Estudiante("Carlos Gómez", 17, "Décimo", 60)

print(Estudiante.mostrar_estudiantes())

Estudiante.esta_aprobado(estudiante1.promedio)

Estudiante.contar_estudiantes()

Estudiante.actualizar_notas("Ana López", 70)

Estudiante.mejor_promedio()