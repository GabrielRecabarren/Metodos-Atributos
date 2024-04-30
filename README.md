# Métodos y Atributos

En este desafío validamos nuestros conocimientos en clases, métodos, atributos estáticos y no estáticos.

## Autogestión de Pedidos de Pizza
 
Este programa en Python permite a los clientes autogestionar sus pedidos de pizza. La aplicación permite a los usuarios ordenar una pizza personalizada eligiendo tres ingredientes y el tipo de masa. El precio de todas las pizzas es de $10.000 y el tamaño es familiar.

## Características

- Permite ordenar una pizza personalizada con tres ingredientes y el tipo de masa.
- Los ingredientes pueden ser vegetales o proteicos.
- Los tipos de masa pueden ser tradicional o delgada.
- Valida los ingredientes y el tipo de masa ingresados por el usuario.
- Informa si la pizza ordenada es válida o no.
- Implementa Programación Orientada a Objetos.

## Requerimientos

1. **Creación de la clase Pizza**: Se crea una clase `Pizza` en el archivo `pizza.py` con los atributos necesarios para representar una pizza y realizar un pedido.

2. **Método para validar un elemento**: Se agrega un método estático `validar_elemento` en la clase `Pizza` que permite validar si un elemento está presente en una lista de casos posibles.

3. **Método para realizar un pedido**: Se añade un método `realizar_pedido` en la clase `Pizza` que solicita al usuario ingresar los ingredientes y el tipo de masa para realizar el pedido.

4. **Validación del pedido**: Se evalúa si el pedido realizado es válido verificando que los ingredientes y el tipo de masa estén dentro de las opciones posibles.

5. **Evaluaciones en el archivo `evaluaciones.py`**:
    - Se muestran los atributos de clase de la clase `Pizza`.
    - Se verifica si el elemento "salsa de tomate" está presente en una lista de ingredientes.
    - Se crea una instancia de la clase `Pizza` y se solicitan los ingredientes y el tipo de masa al usuario.
    - Se muestra en pantalla los ingredientes, el tipo de masa y si la pizza es válida.
    - Se muestra si la clase `Pizza` es una pizza válida o no.

## Uso

1. Ejecutar el archivo `evaluaciones.py` para interactuar con el programa y realizar pedidos de pizza.
2. Seguir las instrucciones en pantalla para ingresar los ingredientes y el tipo de masa deseados.
3. El programa mostrará los detalles del pedido y si la pizza es válida.

## Autor

[Gabriel Recabarren](https://github.com/gabrielrecabarren).