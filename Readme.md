# Proyecto final integrador Programación 1

Desarrollar en grupos de a 3 un sistema de altas, bajas y modificaciones para un problema en particular escrito en python utilizando los elementos vistos en clase durante el año con el libro "Introducción a la programación con python 3".
Se entrega como ejemplo un ABM para una agenda de contactos y otro de un Videoclub.

Ejemplos de sistemas:
- Stock de productos y proveedores
- registro de médicos y pacientes
- turno para una clínica odontológica privada
- registro de personajes y estadísticas de lol
- gestión de tareas y proyectos, fechas estados, asignaciones
- stock y ventas del día.
- turnero de centro estético
- Registro de selecciones de futbol en los distintos mundiales, con sus jugadores.


## Cronograma:
4 entregas y la defensa

### Entrega 1: Resumen de proyecto
Llenar formulario con:
+ Miembros del grupo
+ nombre del grupo
+ descripción del proyecto
+ funcionalidades

#### Ejemplo:

Descripción: Control de stock de un almacén:
Datos:
productos:
	- nombre producto
	- stock
	- precio de compra
	- precio de venta
	- proveedor
proveedores:
	- nombre
	- teléfono
	- dirección
ventas:
	- fecha
	- productos vendidos [(nombre producto,cantidad)]
	- monto total

Funcionalidades
- dar de alta un producto
- preguntar cuantos quedan
- agregar cantidades a un producto existente
- consultar precio
- hacer una venta (agrega la venta hecha con el monto y decrementar el stock del producto)

### Entrega 2: Entrega preliminar:
+ archivo zip con lo que se tenga hasta el momento
+ Documento contando que se tiene y que falta implementar (estado de situación del proyecto)
- que anda
- que no anda
- que falta implementar

### Entrega 3: Código fuente y documentación del proyecto
- Codigo fuente
- Documento de explicacion Readme con modo de uso

### Entrega 4 : Video
- Video de 10 minutos presentando el proyecto (link al video)
* opcional entregar presentacion si usan durante el video

### Defensa orales

# Recomentaciones para la implementación:
Entrega 1
- Usar el programa Agenda entenderla y documentarla (ponerles comentarios que expliquen que hace)
- Diseñar el programa de usteedes en base a los visto en la clase Agenda (clases y metodos necesarios)
- Entregar el borrador de proyecto

Entrega 2
- Armar el esqueleto de las clases que necesitan
- primero las clases mas sencillas del tipo de dato especifico y despues la de administracion (ej primero contacto y después agenda)
- ir usando el archivo test para ir probando el funcionamiento, pueden hacer un archivo de test por clase tambien

Entrega 3
- agregar descripcion de cada clase y metodo
- agregar los test de cada metodo
- corregir lo que no este funcionando
- modificar el menu para agregar nuevas funcionalidades

Entrega 4:
- armar una presentacion con una diapositiva por cada uno de los puntos mencionados
- repartir aprtes
- ensayar la presentacion y medir el tiempo
- grabar la presentacion con un meet y grabando la pantalla, por ejemplo con obs o vokoscreen

# Evaluación 

## Individual:
+ Cada une hace un reporte de avance semanal, que hice la semana pasada, que voy a hacer la que viene, que dificultades estoy teniendo.
+ Defensa oral:  Se le haran preguntas tanto del codigo como del teorico que utilizaron
+ Preguntas sobre lo visto en la materia usado en el proyecto (programas, funciones, listas, clases, etc).

## Entrega de código fuente:
Debe incluir:
Funcionalidades a Implementar:
1. Alta de datos: Los estudiantes deben permitir al usuario agregar nuevos datos al sistema. 
2. Baja de datos: Debe ser posible eliminar un dato existente en la lista.
3. Modificación de datos: Los usuarios deben poder editar la información de un dato, por ejemplo, para corregir un número de teléfono incorrecto (suponiendo que es un contacto).
4. Lectura y escritura de datos: Los contactos deben ser almacenados en un archivo tomar el ejemplo otorgado por el docente
5. Menú de usuario: Implementar un menú que permita al usuario seleccionar las operaciones deseadas de alta, baja, modificación, lectura y escritura de datos.
6. Validación de entrada: Asegurarse de que los datos ingresados por el usuario sean válidos y cumplan con ciertos criterios (por ejemplo, un número de teléfono válido no tiene letras).
7. Manejo de errores: Implementar un manejo de errores que evite bloqueos del programa y proporcione mensajes de error informativos al usuario.
8. Pruebas y aserciones: Incluir pruebas de funcionamiento con casos de prueba que cubran diferentes situaciones, y usar aserciones para verificar que las funciones operan como se espera.
9. Documentación del código: Proporcionar comentarios explicativos en el código para ayudar a otros a entender su funcionamiento.

Condiciones
+ no debería encontrarse errores graves (por error grave se entiende por errores que detengan el funcionamiento del programa
+ Las funciones deben tener definidos los tipos de entrada y de salida
+ tiene que haber un test por método.
* punto extra en el trabajo si testean todo con asserts
* punto extra si relacionan los datos (como hace el videoclub del libro, que socio alquilo que película) 

## Entrega de video:
El video de presentación del proyecto-laboratorio de programación debe ser una herramienta efectiva para evaluar el trabajo final integrador de los estudiantes. Aquí hay una lista de elementos que deberían estar presentes en ese video:

Introducción :
    Nombre del proyecto y de los integrantes del grupo.
    Breve resumen del problema del mundo real que están abordando.

Contexto del problema :
    Explicación detallada del problema del mundo real que eligieron.
    ¿Por qué es importante resolver este problema?
    Descripción de cómo se enfrenta este problema en la vida real.

Funcionalidades del sistema :
    Demostración de las operaciones de altas, bajas y modificaciones en el sistema.
    Ejemplos concretos de cómo se utilizan las clases y métodos.
    Mostrar cómo se resuelve el problema del mundo real con estas funcionalidades.

Demostración en Vivo (si es posible) :
    Ejecución en vivo del sistema para mostrar su funcionamiento real.
    Ejemplo práctico que ilustre cómo resolver un problema del mundo real con el sistema.
    
Diseño de clases :
    Presentación de las clases y estructuras de datos utilizadas en el proyecto.
    Explicación de cómo estas clases se relacionan entre sí.
    Diagrama de clases o pseudocódigo para visualizar la estructura del programa.

Código y Programación :
    Breve revisión del código fuente relevante.
    Explicación de al menos una parte del código que sea crítica para la funcionalidad del sistema.
    Destacar buenas prácticas de programación utilizadas en el proyecto.

Pruebas y Resultados :
    Muestra de casos de prueba y resultados obtenidos.
    Discusión sobre cómo se garantiza que el sistema funcione correctamente.
    Manejo de errores y validación de datos.

Retos y Desafíos :
    Discusión sobre los desafíos encontrados durante el desarrollo.
    Cómo se abordaron y resolvieron estos desafíos.

Conclusiones :
    Resumen de los logros alcanzados con el proyecto.
    Reflexiones sobre lo aprendido durante el proceso.
    Posibles mejoras o ampliaciones futuras del sistema.

Agradecimientos :
    Agradecimiento al profesor y a cualquier persona o recurso que haya sido de ayuda durante el proyecto.

## Criterios de Evaluación grupal del código y la presentación:
* Diseño y estructura del código: Se evaluará la organización del código, incluyendo la modularidad, el uso de clases y estructuras de datos, y la claridad del diseño.
* Funcionalidades del sistema: Los estudiantes deben implementar correctamente las operaciones de alta, baja y modificación de datos, así como la lectura y escritura de datos en un archivo.
* Interfaz de usuario: Deben desarrollar un menú de usuario que permita al usuario realizar todas las operaciones de manera intuitiva.
* Manejo de errores: El programa debe manejar errores de entrada del usuario y de operación, proporcionando mensajes de error claros y evitando bloqueos graves del programa.
* Pruebas y validación: Deben realizar pruebas exhaustivas de las funciones y operaciones del programa, incluyendo la validación de datos y el uso de aserciones (asserts) para verificar el comportamiento correcto del programa.
* Documentación: Se espera que el código esté debidamente comentado y que se proporcione documentación que explique el funcionamiento general del sistema y cómo se utilizan las clases y métodos.
* Presentación del proyecto: El video de presentación debe ser claro, conciso y cumplir con los elementos mencionados en la lista proporcionada, incluyendo una introducción adecuada, contexto del problema y una demostración en vivo si es posible.
