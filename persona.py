class Persona:
    #Atributos de clase
    especie = "Humano"
    idioma = "Español"

    def __init__(self, genero, edad):
        self.genero = genero
        self.edad = edad
    
    def comer(self, platillo):
        print(f"Tengo {self.edad} años y estoy comiendo {platillo}")
    
    def dormir(self):
        print("Estoy durmiendo. No molestar.")

Brahyam = Persona("Masculino", 24)
Patricia = Persona("Femenino", 19)

print(Brahyam.edad)
print(Patricia.genero)

Brahyam.comer("arepa")
Patricia.dormir()

print(Brahyam.especie)
print(Patricia.idioma)
    