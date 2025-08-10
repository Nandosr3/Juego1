# Adivina el Número
##🎲 Partida: Adivina el Número
¡Hola a todos del proyecto "Adivina tú Número!" Este es un juego cotidiano que desarrolla en Python, cuyo objetivo es determinar un número secreto que la computadora ha "creado" en un intervalo de 1 a 100.
##🏛️ La arquitectura y la enfermedad del software
Este proyecto no solo es un juego, es una forma de demostrar un problema de software limpio y modular. La estructura del código parte de una de las prácticas más importantes de la programación, el Principio de Responsabilidad Única (SRP).
Es decir, el programa lo hemos fragmentado en funciones especializadas, en el que cada función sólo tiene una misión. La arquitectura permite obtener ventajas importantes:
✅ Claridad y legibilidad del código: es mucho más fácil de leer y entender el código
🔧 Mantenimiento sencillo: si tenemos que cambiar algo (un ejemplo, el mensaje de bienvenida) sólo hay que modificar lo que está en una función sin riesgo 
 de romper otras partes del programa
🐞 Detección de errores sencilla: si ocurre un error, es muy fácil ir y aislarlo en la función equivocada
♻️ Reutilización: cada función es una pieza de lego que podrios volver a reutilizar en un futuro 
