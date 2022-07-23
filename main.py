# Definir clase
class Perro:

    especie = "Mamífero" # Genera atributos de clase
    
    # Constructor (Genera atributos de INSTANCIA)
    def __init__(self, nombre, edad, nacionalidad): # Self es una variable que hace referencia al propio objeto
        
        # Atributos de instancia
        self.nombre = nombre # Siempre se usa "__init__" y "self" por defecto
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def ladrar(self): #Importante siempre el self en cada metodo
        print("Guau")
    
    def correr(self):
        print("Estoy corriendo")
    
    def comer(self):
        print("Estoy comiendo")
# Instanciar clase (crear objetos)
perrito1 = Perro("Balto", 10, "Venezolano")
perrito2 = Perro("Tasha", 8, "Venezolana")

# Acceder a los atributos
print(perrito1.nombre, perrito1.edad, perrito1.nacionalidad, perrito1.especie)
perrito1.comer()
perrito2.ladrar()