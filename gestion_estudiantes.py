class Estudiante:
    estudiantes_matriculados = {} 

    def __init__(self, nombre, edad, grado, notas):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.notas = notas
        self.promedio = sum(notas)/len(notas)  

        Estudiante.estudiantes_matriculados[nombre] = {
            "edad": edad,
            "grado": grado,
            "notas": notas,
            "promedio":self.promedio 
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
    def esta_aprobado(nombre):
        if nombre in Estudiante.estudiantes_matriculados:
            if Estudiante.estudiantes_matriculados[nombre]["promedio"] >= 60:
                print(f"El estudiante {nombre} ha sido aprobado")
            else:
                print(f"El estudiante {nombre} no ha sido aprobado")
        else:
            print(f"El estudiante {nombre} no está registrado")


    @classmethod
    def contar_estudiantes(cls):
        print(f"Total estudiantes: {len(cls.estudiantes_matriculados)}") 
    
    @classmethod
    def actualizar_notas(cls, nombre, nuevas_notas):
        if nombre in cls.estudiantes_matriculados:
            nuevo_promedio = sum(nuevas_notas) / len(nuevas_notas)
            cls.estudiantes_matriculados[nombre]["notas"] = nuevas_notas
            cls.estudiantes_matriculados[nombre]["promedio"] = nuevo_promedio
            print(f"El promedio de {nombre} ha sido actualizado a {nuevo_promedio}")
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

estudiante1 = Estudiante("ALex Moscoso", 16, "Noveno", [80,60,70])        
estudiante2 = Estudiante("Ana López", 12, "Sexto", [40,60,67])
estudiante3 = Estudiante("Carlos Gómez", 17, "Décimo", [55,80,70])

print(Estudiante.mostrar_estudiantes())

Estudiante.esta_aprobado("Ana López")

Estudiante.contar_estudiantes()

Estudiante.actualizar_notas("Ana López",[70,60,80] )

Estudiante.mejor_promedio()