import numpy as np
import math


def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Definir Valores")
    print("2. Mostrar Valores")
    print("3. Mostrar Solución")
    print("4. Salir")


def pedir_num_vueltas(n_num):
    while True:
        try:
            n1 = int(input(f"Ingrese un valor positivo para N{n_num}: "))
            if n1 > 0:
                return n1
            else:
                print("Por favor, ingrese un número mayor que 0.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def elegir_entre_dos(n1, n2):
    while True:
        try:
            opcion = int(input(f"Elija entre {n1} o {n2}: "))
            if opcion == n1 or opcion == n2:
                return opcion  # Devolver la opción elegida si es válida
            else:
                print(f"Por favor, ingrese {n1} o {n2}.\n")
        except ValueError:
            print("Por favor, ingrese un número válido.\n")


def elegir_en_rango(min_valor, max_valor):
    while True:
        try:
            opcion = float(input(f"Elija un número entre {min_valor} y {max_valor}: "))
            if min_valor <= opcion <= max_valor:
                return opcion  # Devolver la opción elegida si está dentro del rango
            else:
                print(f"Por favor, ingrese un número entre {min_valor} y {max_valor}.\n")
        except ValueError:
            print("Por favor, ingrese un número válido.\n")


def pedir_numero_positivo():
    while True:
        try:
            numero = float(input("Ingrese un número: "))
            if numero > 0:
                return numero
            else:
                print("El número debe ser positivo. Inténtelo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


def pedir_corriente(choice):
    while True:
        try:
            current = float(input(f"Ingrese el valor de la corriente {choice}: "))
            return current
        except ValueError:
            print("Por favor, ingrese un número válido para el valor de N1.")


def solicitar_flotante(mensaje):
    """Solicita al usuario un número flotante y maneja excepciones de entrada inválida."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")


def solicitar_par_ordenado(mensaje):
    """Solicita al usuario un par ordenado (B, H) y maneja excepciones de entrada inválida."""
    while True:
        try:
            x, y = map(float, input(mensaje).split(','))
            return x, y
        except ValueError:
            print("Favor ingrese un par ordenado válido en el formato B,H.")


def resolver_ecuacion_puntos(x1, y1, x2, y2):
    """Resuelve la ecuación de la curva H-B a partir de dos puntos dados."""
    ec1 = np.array([[-y1, x1 * y1], [-y2, x2 * y2]])
    ec2 = np.array([-x1, -x2])
    sol = np.linalg.solve(ec1, ec2)
    return sol[0], sol[1]


def curva():

    print("\nSeleccione 1 para dar ecuación de la curva H-B. Seleccione 2 para dar 2 puntos de la curva H-B: ")
    opcion = elegir_entre_dos(1, 2)

    if opcion == 1:
        a_ec = solicitar_flotante("Ingrese el valor de A de la ecuación: ")
        b_ec = solicitar_flotante("Ingrese el valor de B de la ecuación: ")
        print(f"La ecuación de la curva H-B del material ferromagnético es: B = ({a_ec} H) / (1 + {b_ec} H)")
        return a_ec, b_ec

    elif opcion == 2:
        x1, y1 = solicitar_par_ordenado("Ingrese el primer punto de la curva (B,H): ")
        x2, y2 = solicitar_par_ordenado("Ingrese el segundo punto de la curva (B,H): ")
        a_ec, b_ec = resolver_ecuacion_puntos(x1, y1, x2, y2)
        print(f"La ecuación de la curva H-B del material ferromagnético es: B = ({a_ec} H) / (1 + {b_ec} H)")
        return a_ec, b_ec


def ingresar_datos():
    print("\nSe necesita el valor del número de vueltas para la bobina 1: ")
    n1 = pedir_num_vueltas(1)
    print("\nSe necesita el valor del número de vueltas para la bobina 2: ")
    n2 = pedir_num_vueltas(2)
    print("\n¿Cuál corriente desea definir?")
    choice_i = elegir_entre_dos(1, 2)
    print("\nSe necesita el valor de la corriente en mA: ")
    valor_i = pedir_corriente(choice_i)
    print("\nIngrese el factor de apilado de las láminas del núcleo ferromagnético (0 o 1):")
    apilado = elegir_en_rango(0, 1)
    print("\nSe necesita el área de la sección transversal de la columna central S_C")
    S_C = pedir_numero_positivo()
    print("\nSe necesita el área de la sección transversal del resto del circuito S_L")
    S_L = pedir_numero_positivo()
    print("\nSe necesita el ancho A, que es el mismo para todo el circuito")
    A = pedir_numero_positivo()
    print("\nSe necesita la longitud L1, correspondiente a la sección izquierda")
    L1 = pedir_numero_positivo()
    print("\nSe necesita la longitud L2, correspondiente a la sección derecha")
    L2 = pedir_numero_positivo()
    print("\nSe necesita la longitud L3, correspondiente a la altura donde se encuentra el entrehierro")
    L3 = pedir_numero_positivo()
    print("\nSe necesita la longitud LE, correspondiente al ancho del entrehierro")
    LE = pedir_numero_positivo()
    fe = solicitar_flotante("Se necesita el flujo magnetico deseado por el entrehierro:")
    a_ecuacion, b_ecuacion = curva()

    return {
        "n1":[n1, "espiras"], "n2": [n2, "espiras"], "Corriente": [choice_i, "Bobina" ], "valor_i": [valor_i,"A"], 
        "apilado": [apilado,""], "S_C": [S_C, "metros cuadrados"], "S_L": [S_L,"metros cuadrados"], "A": [A,"m"], 
        "L1": [L1,"m"], "L2": [L2,"m"], "L3": [L3,"m"], "LE": [LE,"m"],"Flujo magnetico":[fe,"Wb"], "Valor A": [a_ecuacion, ""],
        "Valor B": [b_ecuacion, ""]
    }


def mostrar_datos(datos):
    if datos:
        print("\n--- Valores Definidos ---")
        for key, value in datos.items():
            # value[0] es el valor y value[1] es la unidad o descripción
            valor, unidad = value
            print(f"{key}: {valor} {unidad}")
    else:
        print("No se han definido valores aún.")


def calcular_solucion(datos):
    if datos:
        # Aquí se incluirían las fórmulas o cálculos necesarios para obtener la solución
        print("\n--- Solución Calculada ---")
        # Ejemplo de cálculo simple (modificar según tus necesidades)
        B3 = float(datos["Flujo magnetico"][0]) /(float(datos["S_C"][0])*float(datos["apilado"][0])) 
        H3 = B3/(datos["Valor A"][0]-datos["Valor A"][0]*B3)
        # Cálculo de ha (permeabilidad del aire)
        ha = 1 / (4 * math.pi * 10 ** -7)  
        
        # Cálculo de fmmab (fuerza magnetomotriz en la parte central del núcleo)
        fmmab = (H3 * (datos["Valor A"][0] - datos["LE"][0]) + ha * datos["LE"][0])
        
        h1 = (datos["n1"][0]*datos["valor_i"][0]-fmmab)/datos["L1"][0]
        b1 =(datos["Valor A"][0] * h1) / (1 + datos["Valor B"][0] * h1)
        f1 = b1 * datos["S_L"][0] * datos["apilado"][0]
        f2 = float(datos["Flujo magnetico"][0]) - f1
        b2 = f2 / ( float(datos["S_L"][0]) * float(datos["apilado"][0]))
        h2 = b2 / (float(datos["Valor A"][0]) - float(datos["Valor B"][0]) * b1)
        i2 = (h2 * float(datos["valor_i"][0]) + fmmab) / float(datos["n2"][0])
        
        print(i2)
    else:
        print("No se han definido valores para calcular la solución.")


def main():
    datos = {}
    while True:
        mostrar_menu()
        opcion = elegir_en_rango(1, 4)
        
        if opcion == 1:
            datos = ingresar_datos()
        elif opcion == 2:
            mostrar_datos(datos)
        elif opcion == 3:
            calcular_solucion(datos)
        elif opcion == 4:
            print("Saliendo del programa.")
            break


if __name__ == "__main__":
    main()
