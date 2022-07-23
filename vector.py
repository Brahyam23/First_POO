
class Vector:

    def __init__(self, data: list):
        self.data = data

    def __str__(self):
        cadena = ""

        for num in self.data:
            cadena+= f"{num},"

        return f"Vector [{cadena}]"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, posicion):
        return self.data[posicion]

    def __setitem__(self, posicion, valor):
        self.data[posicion] = valor


    def __iter__(self):
        for value in self.data:
            yield f"Value: {value}"

vec = Vector([1,2])
