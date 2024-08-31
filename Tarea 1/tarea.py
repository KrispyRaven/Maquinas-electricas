def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Definir Valores")
    print("2. Mostrar valores")
    print("2. Mostrar solucion")
    print("3. Salir")
    
    
def pedir_opcion_num():
    while True:
        opcion = input("Seleccione una opción (1 o 2): ")
        if opcion in ["1", "2"]:
            return opcion
        else:
            print("Opción no válida, por favor seleccione 1 o 2")
    
def ingresar_datos():
    n1 = input("Ingrese el valor del numero de vultas para la bobina 1: ")
    n2 = input("Ingrese el valor del numero de vultas para la bobin")
    print("Cual corriente quiere definir. Prsiones 1 para I1 o 2 para I2:")
    choice = pedir_opcion_num()
    valor = input("Ingrese el valor de la corrinte en mA:")
    i1 = input("Ingrese el valor: ")
    ciudad = input("Ingrese su ciudad: ")
    # Aquí puedes agregar más campos según sea necesario
    return {"nombre": nombre, "edad": edad, "ciudad": ciudad}