import random

def mostrar_bienvenida_y_obtener_nombre():
    """Muestra el mensaje de bienvenida y solicita el nombre del jugador.

    Returns:
        str: Nombre del jugador ingresado por teclado.
    """
    print("-------------------------------------------")
    print("--- ¡BIENVENIDO A ADIVINA EL NÚMERO! ---")
    print("-------------------------------------------")
    
    nombre_jugador = input("Primero, ¿cuál es tu nombre?: ")
    
    print(f"\n¡Perfecto, {nombre_jugador}! Vamos a empezar.")
    print("Voy a pensar en un número del 1 al 100. Tienes 10 intentos para adivinarlo.")
    
    return nombre_jugador


def configurar_juego():
    """Genera la configuración inicial del juego.

    Returns:
        tuple: Número secreto (int) y número máximo de intentos (int).
    """
    numero_secreto = random.randint(1, 100)
    intentos_maximos = 10
    return numero_secreto, intentos_maximos


def obtener_numero_valido(intento_actual, intentos_maximos):
    """Solicita y valida que el jugador introduzca un número válido.

    Args:
        intento_actual (int): Número de intento actual.
        intentos_maximos (int): Número máximo de intentos permitidos.

    Returns:
        int: Número introducido por el jugador que esté entre 1 y 100.
    """
    while True:
        print(f"\n--- Intento {intento_actual} de {intentos_maximos} ---")
        try:
            respuesta_str = input("Introduce tu número: ")
            numero_elegido = int(respuesta_str)
            
            if 1 <= numero_elegido <= 100:
                return numero_elegido
            else:
                print("-> ¡Cuidado! El número debe estar entre 1 y 100.")
        except ValueError:
            print("-> Por favor, introduce un número válido.")


def comparar_y_dar_pista(numero_elegido, numero_secreto):
    """Compara el número elegido con el secreto y da una pista.

    Args:
        numero_elegido (int): Número introducido por el jugador.
        numero_secreto (int): Número secreto generado por el juego.

    Returns:
        bool: True si el número fue adivinado, False en caso contrario.
    """
    if numero_elegido < numero_secreto:
        print("-> Incorrecto. El número que pensé es más ALTO.")
        return False
    elif numero_elegido > numero_secreto:
        print("-> Te pasaste. El número que pensé es más BAJO.")
        return False
    else:
        return True


def mostrar_resultado_final(nombre_jugador, adivinado, numero_secreto, intentos_realizados):
    """Muestra el resultado final del juego.

    Args:
        nombre_jugador (str): Nombre del jugador.
        adivinado (bool): True si el jugador adivinó el número.
        numero_secreto (int): Número que debía adivinarse.
        intentos_realizados (int): Número de intentos que usó el jugador.
    """
    print("\n================================================")
    if adivinado:
        print(f"¡GENIAL, {nombre_jugador}! ¡Has ganado!")
        print(f"Adivinaste el número {numero_secreto} en {intentos_realizados} intentos.")
    else:
        print(f"¡Oh no, {nombre_jugador}! Se te acabaron los intentos.")
        print(f"El número secreto era el {numero_secreto}. ¡Mejor suerte la próxima!")
    print("================================================")
    print("\n¡Fin del juego!")


def jugar_adivinanza():
    """Ejecuta el flujo principal del juego 'Adivina el Número'.

    Orquesta las siguientes funcionalidades:
    - Mostrar bienvenida y obtener nombre.
    - Configurar número secreto e intentos.
    - Solicitar y validar intentos del jugador.
    - Comparar e informar pistas.
    - Mostrar resultado final.
    """
    nombre_jugador = mostrar_bienvenida_y_obtener_nombre()
    numero_secreto, intentos_maximos = configurar_juego()
    
    intentos_realizados = 0
    adivinado = False
    
    while intentos_realizados < intentos_maximos and not adivinado:
        numero_elegido = obtener_numero_valido(intentos_realizados + 1, intentos_maximos)
        intentos_realizados += 1
        adivinado = comparar_y_dar_pista(numero_elegido, numero_secreto)
        
        if adivinado:
            break
    
    mostrar_resultado_final(nombre_jugador, adivinado, numero_secreto, intentos_realizados)


if __name__ == "__main__":
    jugar_adivinanza()