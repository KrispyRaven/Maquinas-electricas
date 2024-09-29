""""
Tarea programada Maquinas Electricas I
Integrantes del grupo: Noel Blandon Saborio (B61097) y Jimena Gonzalez Jimenez (B83443)
Este código sirve para solucionar circuitos magnéticos. 
"""
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
    print("\nSe necesita el valor de la corriente en A: ")
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


def calcular_solucion(datos): #esta es la función que hay que arreglar
    if datos:
        # Aquí se incluirían las fórmulas o cálculos necesarios para obtener la solución
        print("\n--- Solución Calculada ---")
        
        a_ec = datos["Valor A"][0] 
        b_ec = datos["Valor B"][0] 
        n1 = datos["n1"][0]
        n2  = datos["n2"][0]
        sl = datos["S_L"][0]
        sc = datos["S_C"][0]
        le = datos["LE"][0]
        l1 = datos["L1"][0]
        l2 = datos["L2"][0]
        l3 = datos["L3"][0]
        L = datos["A"][0]
        fa = datos["apilado"][0]
        i_value = datos["valor_i"][0]
        fe = datos["Flujo magnetico"][0]

  
        # Cálculo de h3
        b3 = fe / (sc * fa)
        h3 = b3 / (a_ec - b_ec * b3)  # Se despeja de la ecuación de la curva

        # Cálculo de ha (permeabilidad del aire)
        ha = 1 / (4 * math.pi * 10 ** -7)

        # Cálculo de fmmab (fuerza magnetomotriz en la parte central del núcleo)
        fmmab = (h3 * (a_ec - le) + ha * le)

        if datos["Corriente"][0] == 1:
            h1 = (n1 * i_value - fmmab) / l1
            b1 = (a_ec * h1) / (1 + b_ec * h1)
            f1 = b1 * sl * fa
            f2 = fe - f1
            b2 = f2 / (sl * fa)
            h2 = b2 / (a_ec - b_ec * b2)
            i2 = (h2 * i_value + fmmab) / n2
            print("El valor del flujo magnético del núcleo 1 es:", f1, "Wb")
            print("El valor del flujo magnético del núcleo 2 es:", f2, "Wb")
            print("El valor de I2 es:", i2, "A")
        else:
            h2 = (n2 * i_value - fmmab) / l2
            b2 = (a_ec * h2) / (1 + b_ec * h2)
            f2 = b2 * sl * fa
            f1 = fe - f2
            b1 = f1 / (sl * fa)
            h1 = b1 / (a_ec - b_ec * b1)
            i1 = (h1 * i_value + fmmab) / n1
            print("El valor del flujo magnético del núcleo 1 es:", f1, "Wb")
            print("El valor del flujo magnético del núcleo 2 es:", f2, "Wb")
            print("El valor de I1 es:", i1, "A")

"""
        #Paso 1: se calcula B3 y H3
        B3 = float(datos["Flujo magnetico"][0]) /(float(datos["S_C"][0])*float(datos["apilado"][0])) 
        H3 = B3/(datos["Valor A"][0]-datos["Valor A"][0]*B3)

        #Paso 2: se calcula la longitud efectiva del entrehierro y el campo magnético en el aire
        #campo magnético en el aire dado por:
        ha = 1 / (4 * math.pi * 10 ** -7)  
        #longitud efectiva del entrehierro dada por:
        L_Fe3 = datos["L3"][0] - datos["LE"][0]
        #densidad de flujo en el entrehierro
        #Ba = (float(datos["fe"][0])) / float(datos["S3"][0]) si ya tengo cómo calcular el campo magnético en el aire no necesito esto


        #Paso 3: cálculo de fmmab (fuerza magnetomotriz en la parte central del núcleo)
        fmmab = (H3 * (datos["Valor A"][0] - datos["LE"][0]) + ha * datos["LE"][0])
        
        #Paso 4: Cálculo de H1, flujo Φ1 y flujo en la segunda rama Φ2
        h1 = (datos["n1"][0]*datos["valor_i"][0]-fmmab)/datos["L1"][0]
        b1 =(datos["Valor A"][0] * h1) / (1 + datos["Valor B"][0] * h1)
        f1 = b1 * datos["S_L"][0] * datos["apilado"][0] #se usa S_L porque S1 = S2 = S_L
        f2 = float(datos["Flujo magnetico"][0]) - f1
        b2 = f2 / ( float(datos["S_L"][0]) * float(datos["apilado"][0]))
        #h2 = 202
        h2 = b2 / (float(datos["Valor A"][0]) - float(datos["Valor B"][0]) * b1) #ver después si fuese necesario

        #Paso 5: cálculo de la corriente I2
        i2 = (h2 * float(datos["valor_i"][0]) + fmmab) / float(datos["n2"][0])

        # Parte 1: Cálculo de B3 y H3
        #B3 = flujo_deseado / (S3 * factor_apilado)  # Densidad de flujo magnético en el entrehierro
        #H3 = 251  # Valor de H3 dado (extraído de tabla B-H)

        # Parte 2: Longitud efectiva del entrehierro y cálculo de Ha
        #L_Fe3 = L3 - La  # Longitud efectiva del entrehierro (m) (ya la tenemos)
        #Ba = flujo_deseado / S3  # Densidad de flujo en el entrehierro
        #Ha = Ba / mu0  # Campo magnético en el aire (entrehierro)
    
        # Parte 3: Fuerza Magnetomotriz (FMM) en la parte central
        #FMMaS = H3 * LE + Ha * La  # FMM total en el núcleo y entrehierro

        # Parte 4: Cálculo de H1, flujo Φ1 y flujo en la segunda rama Φ2
        #H1 = (n1 * valor_i - FMMaS) / L1  # Campo magnético H1
        #B1 = 1.1  # Valor de B1 de la tabla B-H (en T)
        #flujo1 = B1 * S1 * factor_apilado  # Flujo en la rama lateral 1 (Wb)
        #flujo2 = flujo_deseado - flujo1  # Flujo en la rama lateral 2 (Wb)
        #B2 = flujo2 / (S2 * factor_apilado)  # Densidad de flujo en la rama lateral 2
        #H2 = 202  # Valor de H2 dado (extraído de tabla B-H)

        # Parte 5: Cálculo de la corriente I2
        #i2 = (H2 * L2 + FMMaS) / n2  # Corriente en el secundario
        
        print(i2) # esta es mi respuesta
    else:
        print("No se han definido valores para calcular la solución.")
"""


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
