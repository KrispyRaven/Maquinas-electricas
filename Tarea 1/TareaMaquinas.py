""""
Tarea programada Maquinas Electricas I
Integrantes del grupo: Ana Carolina Mendez (B94808) y Jimena Sancho Cespedes (B87389)
En este codigo se puede encontrar la solucion a distintos problemas con respecto a los nucleos ferromagneticos,
y tomando encuenta sistemas con una permeabilidad constante y una que es variable 
"""
import math
import numpy as np

#Bloque realizado con chatgpt
def get_current_info(current_type):
    is_positive = None
    current_value = None
    
    if current_type == "I1":
        is_positive = True
        current_value_str = input("Ingrese el valor de I2 (en Amperios): ")
    elif current_type == "I2":
        is_positive = False
        current_value_str = input("Ingrese el valor de I1 (en Amperios): ")
    else:
        print("Por favor ingrese una opción válida ('I1' o 'I2').")
        exit()
    
    try:
        current_value = float(current_value_str)
        if current_value == 0:
            print("Por favor, ingrese un número distinto de cero para la corriente.")
            exit()
    except ValueError:
        print("Por favor, ingrese un número válido para la corriente.")
        exit()
    
    return current_value, is_positive

print("Hola usuario! Este programa te ayuda a resolver los distintos cálculos que puedes tener en un problema de núcleos ferromagnéticos. Por favor, lee con atención los datos que debes introducir.")

# Ingreso del número de vueltas de la bobina 1
int_str = input("Ingrese el valor de N1: ")
try:
    n1 = int(int_str)
except ValueError:
    print("Por favor, ingrese un número válido para el valor de N1: ")
    exit()

# Ingreso del número de vueltas de la bobina 2
int_str = input("Ingrese el valor de N2: ")
try:
    n2 = int(int_str)
except ValueError:
    print("Por favor, ingrese un número válido para el valor de N2: ")
    exit()

# Ingreso del factor de apilado
fa_str = input("Ingrese el valor del factor de apilado: ")
try:
    fa = float(fa_str)
except ValueError:
    print("Por favor, ingrese un número válido para el factor de apilado.")
    exit()

# Ingreso de SL (sección transversal del núcleo en metros cuadrados)
sl_str = input("Ingrese el valor de SL (sección transversal del núcleo en metros cuadrados): ")
try:
    sl = float(sl_str)
except ValueError:
    print("Por favor, ingrese un número válido para SL.")
    exit()

# Ingreso de SC (sección transversal de la columna central)
sc_str = input("Ingrese el valor de SC (sección transversal de la columna central): ")
try:
    sc = float(sc_str)  # Corregido: definir la variable 'sc'
except ValueError:
    print("Por favor, ingrese un número válido para SC.")
    exit()

# Ingreso de L (ancho del núcleo ferromagnético en metros)
L_str = input("Ingrese el ancho del núcleo ferromagnético (en metros cuadrados): ")
try:
    L = float(L_str)
except ValueError:
    print("Por favor, ingrese un número válido para L.")
    exit()

# Ingreso de l1 (ancho)
l1_str = input("Ingrese el ancho l1 del núcleo en metros: ")
try:
    l1 = float(l1_str)
except ValueError:
    print("Por favor, ingrese un número válido para l1.")
    exit()

# Ingreso de l2
l2_str = input("Ingrese el ancho l2 del núcleo en metros: ")
try:
    l2 = float(l2_str)
except ValueError:
    print("Por favor, ingrese un número válido para l2.")
    exit()

# Ingreso de l3
l3_str = input("Ingrese el ancho l3 del núcleo en metros: ")
try:
    l3 = float(l3_str)
except ValueError:
    print("Por favor, ingrese un número válido para l3.")
    exit()

# Ingreso de Le (longitud del entrehierro en metros)
le_str = input("Ingrese la longitud del entrehierro Le en metros: ")
try:
    le = float(le_str)
except ValueError:
    print("Por favor, ingrese un número válido para Le.")
    exit()

# Puntos de la curva H-B
bool2 = input("Seleccione 1 para dar ecuación de la curva H-B. Seleccione 2 para dar 2 puntos de la curva H-B: ")
if bool2 == "1":
    a_ec_str = input("Ingrese el valor de a de la ecuación: ")
    try:
        a_ec = float(a_ec_str)
    except ValueError:
        print("Por favor, ingrese un número válido para 'a'.")
        exit()
    b_ec_str = input("Ingrese el valor de b de la ecuación: ")
    try:
        b_ec = float(b_ec_str)
    except ValueError:
        print("Por favor, ingrese un número válido para 'b'.")
        exit()
    # Se forma la ecuación de H-B con los valores dados:
    print(f"La ecuación de la curva H-B del material ferromagnético es: B = ({a_ec} H) / (1 + {b_ec} H)")

elif bool2 == "2":
    par1 = input("Ingrese el primer punto de la curva (B,H): ")
    try:
        x1, y1 = map(float, par1.split(','))
    except ValueError:
        print("Favor ingrese un par ordenado válido.")
        exit()
    par2 = input("Ingrese el segundo punto de la curva (B,H): ")
    try:
        x2, y2 = map(float, par2.split(','))
    except ValueError:
        print("Favor ingrese un par ordenado válido.")
        exit()
    # Se crea la ecuación de la curva a partir de los 2 puntos:
    ec1 = np.array([[-1 * y1, x1 * y1], [-1 * y2, x2 * y2]])  # Coeficientes de la matriz 2x2
    ec2 = np.array([-x1, -x2])  # Constantes de la matriz
    sol = np.linalg.solve(ec1, ec2)  # Se resuelve la matriz
    a_ec = sol[0]
    b_ec = sol[1]
    print(f"La ecuación de la curva H-B del material ferromagnético es: B = ({a_ec} H) / (1 + {b_ec} H)")

else:
    print("Por favor seleccione alguna de las opciones.")
    exit()

bool_option = input("¿Desea calcular el valor de I1 ó I2? ").lower()

if bool_option in ["i1", "i2"]:
    i_value, i_is_positive = get_current_info(bool_option.upper())
else:
    print("Por favor ingrese una opción válida ('I1' o 'I2').")
    exit()

# Suponemos el valor de fe (fuerza magnetomotriz) y realizamos los cálculos finales
fe = 0.02  #
bool = True  # Asumimos un valor para 'bool'

# Cálculo de h3
b3 = fe / (sc * fa)
h3 = b3 / (a_ec - b_ec * b3)  # Se despeja de la ecuación de la curva

# Cálculo de ha (permeabilidad del aire)
ha = 1 / (4 * math.pi * 10 ** -7)

# Cálculo de fmmab (fuerza magnetomotriz en la parte central del núcleo)
fmmab = (h3 * (a_ec - le) + ha * le)

if not bool:
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