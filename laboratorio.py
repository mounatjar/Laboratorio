class Laboratorio():
    def __init__ (self, productos):
        self.productos = productos
        return self.productos

class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def get_nombre(self):
        return self.nombre
        
    def get_precio(self):
        return self.precio

class Medicamento(Producto):
    def __init__(self, composicion, porcentaje):
        self.composicion = composicion
        self.porcentaje = porcentaje
        
    def get_composicion(self):
        return self.composicion
        
    def get_porcentaje(self):
        return self.porcentaje

prod1 = Producto("vacunas", 25)
prod2 = Producto("alcohol", 8)
medicam1 = Medicamento("Algidol", 25)
medicam2 = Medicamento("Aspirina", 35)
lista = [prod1, prod2, medi1, medi2]

