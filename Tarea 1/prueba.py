import math

def calcular_solucion(datos):
    if datos:
        # Datos iniciales
        N1 = datos["N1"]  # Número de espiras primarias
        N2 = datos["N2"]  # Número de espiras secundarias
        I1 = datos["I1"]  # Corriente en el primario
        S1 = datos["S1"]  # Área transversal de la rama lateral 1
        S2 = datos["S2"]  # Área transversal de la rama lateral 2
        S3 = datos["S3"]  # Área transversal del entrehierro
        L1 = datos["L1"]  # Longitud rama lateral 1
        L2 = datos["L2"]  # Longitud rama lateral 2
        L3 = datos["L3"]  # Longitud entrehierro
        La = datos["La"]  # Longitud del entrehierro
        flujo_deseado = datos["flujo_deseado"]  # Flujo en el entrehierro
        factor_apilado = datos["factor_apilado"]  # Factor de apilado

        # Cálculo de la densidad de flujo magnético en el entrehierro (B3)
        B3 = flujo_deseado / (S3 * factor_apilado) 

        # Buscamos el valor de H3 correspondiente a B3 (según la tabla)
        # Aquí debes interpolar o buscar en una tabla B-H para el material
        H3 = datos["H3"]  # Debe ser proporcionado o calculado

        # Permeabilidad del aire (para el entrehierro)
        mu0 = 4 * math.pi * 10 ** -7

        # Cálculo de la fuerza magnetomotriz (fmm) en la parte central del núcleo (FMM_ab)
        fmm_ab = H3 * (L3 + La / mu0)

        # Relación de la FMM con las corrientes en el circuito magnético
        fmm_total = N1 * I1 - fmm_ab

        # Cálculo de H1 y B1 en la rama lateral 1
        H1 = fmm_total / L1
        B1 = H1 / datos["mu_material"]  # Permeabilidad del material del núcleo
        flujo1 = B1 * S1 * factor_apilado

        # Cálculo de H2 y B2 en la rama lateral 2
        flujo2 = flujo_deseado - flujo1
        B2 = flujo2 / (S2 * factor_apilado)
        H2 = B2 / datos["mu_material"]

        # Finalmente, calculamos la corriente I2 en el secundario
        I2 = (H2 * L2 + fmm_ab) / N2

        # Mostrar el resultado final
        print("La corriente I2 es:", I2)
        print("El flujo en la rama lateral 1 es:", flujo1)
        print("El flujo en la rama lateral 2 es:", flujo2)
    else:
        print("No se han definido valores para calcular la solución.")

# Ejemplo de uso con los datos del problema
datos = {
    "N1": 100,  # espiras primarias
    "N2": 50,   # espiras secundarias
    "I1": 20,   # corriente primaria en A
    "S1": 0.01,  # área transversal en m^2
    "S2": 0.01,  # área transversal en m^2
    "S3": 0.02,  # área del entrehierro en m^2
    "L1": 1.10,  # longitud en m
    "L2": 1.10,  # longitud en m
    "L3": 0.30,  # longitud en m
    "La": 0.002,  # longitud del entrehierro en m
    "flujo_deseado": 0.02,  # flujo en el entrehierro en Wb
    "factor_apilado": 0.97,  # factor de apilado
    "H3": 160,  # campo magnético H3 en A/m (aproximado de la tabla)
    "mu_material": 1.6 * 10 ** -3  # permeabilidad relativa del material
}

calcular_solucion(datos)
