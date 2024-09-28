import math

# Constantes
mu0 = 4 * math.pi * 10 ** -7  # Permeabilidad del vacío o aire (H/m)

def calcular_circuito_magnetico():
    # Parámetros del problema
    S1 = 0.01  # Área de la sección transversal de la rama lateral 1 (m^2)
    S2 = 0.01  # Área de la sección transversal de la rama lateral 2 (m^2)
    S3 = 0.02  # Área del entrehierro (m^2)
    L1 = 1.10  # Longitud de la rama lateral 1 (m)
    L2 = 1.10  # Longitud de la rama lateral 2 (m)
    L3 = 0.30  # Longitud del entrehierro (m)
    La = 0.002 # Longitud del entrehierro (m)
    flujo_deseado = 0.02  # Flujo en el entrehierro (Wb)
    factor_apilado = 0.97  # Factor de apilado

    N1 = 100  # Número de espiras en el primario
    N2 = 50   # Número de espiras en el secundario
    I1 = 20   # Corriente en el primario (A)

    # Parte 1: Cálculo de B3 y H3
    B3 = flujo_deseado / (S3 * factor_apilado)  # Densidad de flujo magnético en el entrehierro
    H3 = 251  # Valor de H3 dado (extraído de tabla B-H)

    # Parte 2: Longitud efectiva del entrehierro y cálculo de Ha
    L_Fe3 = L3 - La  # Longitud efectiva del entrehierro (m)
    Ba = flujo_deseado / S3  # Densidad de flujo en el entrehierro
    Ha = Ba / mu0  # Campo magnético en el aire (entrehierro)
    
    # Parte 3: Fuerza Magnetomotriz (FMM) en la parte central
    FMMaS = H3 * L_Fe3 + Ha * La  # FMM total en el núcleo y entrehierro

    # Parte 4: Cálculo de H1, flujo Φ1 y flujo en la segunda rama Φ2
    H1 = (N1 * I1 - FMMaS) / L1  # Campo magnético H1
    B1 = 1.1  # Valor de B1 de la tabla B-H (en T)
    flujo1 = B1 * S1 * factor_apilado  # Flujo en la rama lateral 1 (Wb)
    flujo2 = flujo_deseado - flujo1  # Flujo en la rama lateral 2 (Wb)
    B2 = flujo2 / (S2 * factor_apilado)  # Densidad de flujo en la rama lateral 2
    H2 = 202  # Valor de H2 dado (extraído de tabla B-H)

    # Parte 5: Cálculo de la corriente I2
    I2 = (H2 * L2 + FMMaS) / N2  # Corriente en el secundario

    # Resultados
    print(f"Densidad de flujo magnético B3: {B3} T")
    print(f"Campo magnético H3: {H3} A/m")
    print(f"Campo magnético en el aire Ha: {Ha} A/m")
    print(f"FMM total en el entrehierro y núcleo FMMaS: {FMMaS} A")
    print(f"Campo magnético H1: {H1} A/m")
    print(f"Flujo en la rama lateral 1: {flujo1} Wb")
    print(f"Flujo en la rama lateral 2: {flujo2} Wb")
    print(f"Corriente en el secundario I2: {I2} A")

# Llamada a la función
calcular_circuito_magnetico()
