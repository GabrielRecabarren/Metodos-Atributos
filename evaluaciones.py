from pizza import Pizza  # Importar la clase Pizza del archivo pizza.py

# Requerimiento 5.a: Mostrar los atributos de clase de la clase importada sin crear una instancia de ella
print("Atributos de la clase Pizza:")
print("Precio:", Pizza.precio)
print("Tamaño:", Pizza.tamano)

# Requerimiento 5.b: Verificar si "salsa de tomate" está presente en una lista de ingredientes sin crear una instancia de la clase
print("¿'salsa de tomate' está presente en la lista de ingredientes?")
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

# Requerimiento 5.c: Crear una instancia de la clase importada y solicitar ingredientes y tipo de masa al usuario
mi_pedido = Pizza()
mi_pedido.realizar_pedido()

# Requerimiento 5.d: Mostrar los ingredientes, el tipo de masa y si la pizza es válida de la instancia creada en el paso anterior
print("Ingredientes vegetales:", mi_pedido.vegetal_1, ",", mi_pedido.vegetal_2)
print("Ingrediente proteico:", mi_pedido.proteico)
print("Tipo de masa:", mi_pedido.tipo_masa)
print("¿Es una pizza válida?", mi_pedido.es_valida)

# Requerimiento 5.e: Verificar si la instancia de la clase Pizza creada en el paso 5.c es válida
print("¿La pizza creada es válida?", mi_pedido.es_valida)
