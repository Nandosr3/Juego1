# Adivina el Número 🎲
¡Hola a todos del proyecto "Adivina tú Número!" Este es un juego cotidiano que desarrolla en Python, cuyo objetivo es determinar un número secreto que la computadora ha "creado" en un intervalo de 1 a 100.
## 🏛️ La arquitectura y la enfermedad del software
Este proyecto no solo es un juego, es una forma de demostrar un problema de software limpio y modular. La estructura del código parte de una de las prácticas más importantes de la programación, el Principio de Responsabilidad Única (SRP).Es decir, el programa lo hemos fragmentado en funciones especializadas, en el que cada función sólo tiene una misión. La arquitectura permite obtener ventajas importantes:-
- ✅ Claridad y legibilidad del código: es mucho más fácil de leer y entender el código
- 🔧 Mantenimiento sencillo: si tenemos que cambiar algo (un ejemplo, el mensaje de bienvenida) sólo hay que modificar lo que está en una función sin riesgo 
 de romper otras partes del programa
 -🐞 Detección de errores sencilla: si ocurre un error, es muy fácil ir y aislarlo en la función equivocada
- ♻️ Reutilización: cada función es una pieza de lego que podrios volver a reutilizar en un futuro 

## Diagrama de Flujo📊📊
Antes de redactar aquel "primer" código, se desarrolló la lógica de cada módulo. Como se muestra a continuación, también se muestra los esquemas de flujo asociados a cada función principal del programa.$1. Modelo Principal (El Dirigente del Juego) 
### 1. Modelo Principal (El Dirigente del Juego) 
Presenta el ritmo general del juego despues de la función jugar_adivinanza().
 Funcionalidad 1: Iniciar y establecer Funcionalidad 1: Inicialización y configuración 
### 2. Funcionalidad 1: Inicialización y configuración Funcionalidad 1 
Está relacionado con las funciones de matar_bienvenida_y_obtener_nombre() y configurar_juego().
 ### 3. Funcionalidad 2: Verificación de la Entrada del Usuario Funcionalidad: 
 Verificación de la Entrada del Usuario Funcionalidad 2 obtener_numero_valido ### 4. Funcionalidad 3: Lógica de comparación y pistas Funcionalidad Ejemplo del procedimiento de comparación_y_dar_pista().
 ### Funcionalidad 4: 4: Conclusión y resultados Funcionalidad 4: Finalización y conclusiones 
Graphicalmente representa la lógica de la función más_resultado_final().
