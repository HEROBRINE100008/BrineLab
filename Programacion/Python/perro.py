class Perro:
    # Método constructor para inicializar los atributos
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    # Método (comportamiento)
    def ladrar(self):
        return "¡Guau!"

# Creando un objeto (instancia)
mi_perro = Perro("Rex", "Pastor Alemán")

# Accediendo a los atributos y métodos
print(mi_perro.nombre)  # Imprime: Rex
print(mi_perro.ladrar())  # Imprime: ¡Guau!

