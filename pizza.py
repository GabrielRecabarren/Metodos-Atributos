from ingredientes import ingredientes_carne, ingredientes_vegetales, tipos_masa  # Importar las listas de ingredientes y tipos de masa

class Pizza:
    precio = 10000  # Precio de todas las pizzas
    tamano = "familiar"  # Tamaño de todas las pizzas

    def __init__(self):
        self.proteico = None  # Inicializar el ingrediente proteico como nulo
        self.vegetal_1 = None  # Inicializar el primer ingrediente vegetal como nulo
        self.vegetal_2 = None  # Inicializar el segundo ingrediente vegetal como nulo
        self.tipo_masa = None  # Inicializar el tipo de masa como nulo
        self.es_valida = None  # Inicializar la validez del pedido como nula

    @staticmethod
    def validar_elemento(elemento, valores_posibles):
        """Método estático para validar si un elemento está presente en una lista de valores posibles."""
        return elemento in valores_posibles

    def realizar_pedido(self):
        
        """Método para realizar un pedido de pizza."""
        
        print("Ingredientes disponibles:")
        print("Proteicos:", ingredientes_carne)
        print("Vegetales:", ingredientes_vegetales)
        print("Tipos de masa:", tipos_masa)
        self.proteico = input("Ingrese el ingrediente proteico: ")  # Solicitar al usuario el ingrediente proteico
        self.vegetal_1 = input("Ingrese el primer ingrediente vegetal: ")  # Solicitar al usuario el primer ingrediente vegetal
        self.vegetal_2 = input("Ingrese el segundo ingrediente vegetal: ")  # Solicitar al usuario el segundo ingrediente vegetal
        self.tipo_masa = input("Ingrese el tipo de masa (tradicional/delgada): ")  # Solicitar al usuario el tipo de masa
        
        # Validar si el pedido es válido
        if (self.validar_elemento(self.proteico, ingredientes_carne) and
            self.validar_elemento(self.vegetal_1, ingredientes_vegetales) and
            self.validar_elemento(self.vegetal_2, ingredientes_vegetales) and
            self.validar_elemento(self.tipo_masa, tipos_masa)):
            self.es_valida = True  # Si el pedido es válido, establecer la validez como verdadera
        else:
            self.es_valida = False  # Si el pedido no es válido, establecer la validez como falsa
