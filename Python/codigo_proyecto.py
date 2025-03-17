class ConvertidorMoneda:
    def __init__(self, tasa_cambio):
        self.tasa_cambio = tasa_cambio

    def convertir(self, monto):
        return monto * self.tasa_cambio

    def ajustar_tasa_cambio(self, nueva_tasa):
        self.tasa_cambio = nueva_tasa
 # esta clase fue agrega el 13/03& 26 por Antonio  Rodriguez
 # esto ejecuta a la mama de la mama de lamam
class Pizza:
    def __init__(self, nombre, ingredientes, precio, tamano="", convertidor=None):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.precio = precio
        self.tamano = tamano
        self.convertidor = convertidor
    
    def __str__(self):
        precio_convertido = self.convertidor.convertir(self.precio) if self.convertidor else self.precio
        return f"{self.nombre} ({self.tamano}): {', '.join(self.ingredientes)} - ${self.precio:.2f} o Bs{precio_convertido:.2f}"

    def calc_tamano(self):
        if self.tamano == "pequeña":
            self.precio += 1.0
        elif self.tamano == "mediana":
            self.precio += 2.5
        elif self.tamano == "familiar":
            self.precio += 3.0
        else:
            print("No se ha elegido una opción correcta")
            return    
class Orden:
    def __init__(self, cliente):
        self.cliente = cliente
        self.pizzas = []
    
    def agregar_pizza(self, pizza):
        pizza.calc_tamano()
        self.pizzas.append(pizza)

    def calcular_total(self):
        return sum(pizza.precio for pizza in self.pizzas)

    def __str__(self):
        descripcion_pizzas = "\n".join(str(pizza) for pizza in self.pizzas)
        return f"Orden para {self.cliente}:\n{descripcion_pizzas}\nTotal: ${self.calcular_total():.2f}"

def mostrar_menu2():
    print("1. Elegir una pizza")
    print("2. Ver elección")
    print("3. Salir")

class Venta:
    def __init__(self, tasa_cambio):
        self.menu = {
            "Margarita": Pizza("Margarita", ["Queso", "Tomate"], 2.50),
            "Pepperoni": Pizza("Pepperoni", ["Queso", "Pepperoni"], 4.00),
            "Hawaiana": Pizza("Hawaiana", ["Queso", "Jamón", "Piña"], 4.50)
        }
        self.convertidor_moneda = ConvertidorMoneda(tasa_cambio)
        for pizza in self.menu.values():
            pizza.convertidor = self.convertidor_moneda

    def mostrar_menu(self):
        print("Menú de Pizzas:")
        for nombre, pizza in self.menu.items():
            print(pizza)

    def crear_orden(self):
        cliente = input("Ingrese el nombre del cliente: ")
        orden = Orden(cliente)

        while True:
            mostrar_menu2()
            a = input("Seleccione: ")
            if a == "1":
                self.mostrar_menu()
                n = input("Seleccione una Pizza o escriba 'salir': ").casefold().capitalize()
                if n.lower() == "salir":
                    break
                if n in self.menu:
                    print("Menú de Tamaños: \n Pequeña: $1.0 \n Mediana: $2.5 \n Familiar: $3.0")
                    s = input("Ingrese el tamaño de su pizza (Pequeña/Mediana/Familiar): ")
                    pizza_seleccionada = self.menu[n]
                    pizza_seleccionada.tamano = s.lower()
                    orden.agregar_pizza(pizza_seleccionada)
                else:
                    print("Pizza no encontrada, intente de nuevo")
            elif a == "2":
                print(f"\n--- Pizzas Elegidas ---\n{orden}\n")
            elif a == "3":
                break
            
        print("\n--- Resumen de la Orden ---")
        print(orden)

    def mostrar_orden_convertida(self, orden):
        print("\n--- Resumen de la Orden en Otra Moneda ---")
        total_convertido = self.convertidor_moneda.convertir(orden.calcular_total())
        print(f"Total en otra moneda: Bs{total_convertido:.2f}")

    def ajustar_tasa_cambio(self, nueva_tasa):
        self.convertidor_moneda.ajustar_tasa_cambio(nueva_tasa)

venta = Venta(tasa_cambio=80.2)  # Por ejemplo, tasa de cambio inicial 1.2
venta.crear_orden()
orden = venta.crear_orden()
venta.mostrar_orden_convertida(orden)

# Para ajustar la tasa de cambio
venta.ajustar_tasa_cambio(80.2)
venta.mostrar_orden_convertida(orden)
