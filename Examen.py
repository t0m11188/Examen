
computadores = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['ACER', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['ASUS', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['ASUS', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['ACER', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['ACER', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['DELL', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
                           }

stock = {
    '8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
    'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
                 }

def stock_marca():
    marca =input("Ingrese marca: ").upper()
    suma=0
    for clave, valor in computadores.items():
            for v in valor:
                if v==marca:
                    for klave, balor in stock.items():
                        for b in balor:
                            if klave==clave:
                                    print("El stock disponible de la marca", marca, "es de", balor[1], "unidades")
                                    return



def eliminar_producto():
    eliminado =input("Ingrese modelo de producto a eliminar: ").upper()
    if eliminado in computadores:
        for clave in computadores:
            if clave==eliminado:
                del computadores[eliminado]
                del stock[eliminado]
                print("Producto eliminado correctamente")
                return
    else:
        print("No se encontró el producto")
def menu():
    while True:
        print("\nMENÚ PRINCIPAL")
        print("=============================================")
        print("1. Stock marca.")
        print("2. Búsqueda por RAM y precio.")
        print("3. Eliminar producto.")
        print("4. Salir.")
        
        opcion = input("Seleccione una opción (1-4): ")
        
        if opcion == "1":
            stock_marca()
        if opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            print("Saliendo del menú....")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu()