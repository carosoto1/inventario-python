import datetime

# Definicion de la estructura de datos para el inventario
class Inventory:
    def __init__(self):
        self.inventory = []

# Funcion para añadir un nuevo articulo al inventario
    def add_item(self, name, quantity, price, type, size):
        item = {
            'name': name,
            'quantity': quantity,
            'price': price,
            'type': type,
            'size': size,
            'date': datetime.datetime.now()
        }
        self.inventory.append(item)

    # Funcion para actualizar la cantidad de un articulo existente
    def update_quantity(self, name, new_quantity):
        for item in self.inventory:
            if item['name'] == name:
                item['quantity'] = int(new_quantity)
                break
        print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Type: {item['type']}, Size: {item['size']}, Date: {item['date']}")

    # Funcion para buscar articulos especificos en el inventario
    def search_items(self, criteria, value):
        if criteria == 'name':
            return filter(lambda item: item['name'] == value, self.inventory)
        elif criteria == 'quantity':
            return filter(lambda item: item['quantity'] == value, self.inventory)
        elif criteria == 'price':
            return filter(lambda item: item['price'] == value, self.inventory)
        elif criteria == 'type':
            return filter(lambda item: item['type'] == value, self.inventory)
        elif criteria == 'size':
            return filter(lambda item: item['size'] == value, self.inventory)
        elif criteria == 'date':
            return filter(lambda item: item['date'] == value, self.inventory)
            
    # Funcion para ordenar el inventario por nombre, cantidad o precio
    def sort_inventory(self, key):
        if key == 'name':
            return sorted(self.inventory, key=lambda item: item[key])
        elif key == 'quantity':
            return sorted(self.inventory, key=lambda item: item[key])
        elif key == 'price':
            return sorted(self.inventory, key=lambda item: item[key])
        elif key == 'type':
            return sorted(self.inventory, key=lambda item: item[key])
        elif key == 'size':
            return sorted(self.inventory, key=lambda item: item[key])
        elif key == 'date':
            return sorted(self.inventory, key=lambda item: item[key])

    # Funcion anidada para generar un informe de inventario
    def generate_inventory_report(self):
        def calculate_value(item):
            return item['quantity'] * item['price']
        total_value = sum(calculate_value(item) for item in self.inventory)
        print("==== INVENTORY REPORT ====")
        for item in self.inventory:
            print(f"Name: {item['name']}")
            print(f"Quantity: {item['quantity']}")
            print(f"Price: {item['price']}")
            print(f"Type: {item['type']}")
            print(f"Size: {item['size']}")
            print(f"Date: {item['date']}")
            print("----------------")
        print(f"Total Value of Quantity * Price: {total_value}")

inventory = Inventory()

# Ciclo principal
while True:
    menu = """
        ======= MENU =========
        1. Add item
        2. Update quantity from item
        3. Search item
        4. Sort inventory
        5. Generate report of inventory
        6. Salir
        -----------------------------
        Enter your choice: """
    option = int(input(menu))
    if option == 1:
       inventory.add_item(
        input('Enter the name of the item: '),
        int(input('Enter the quantity of the item: ')),
        int(input('Enter the price of the item: ')),
        input('Enter the type of the item: '),
        int(input('Enter the size of the item: '))
       )
    elif option == 2:
        name_update = input('Enter the name of the item to update: ')
        quantity_update = input('Enter the new quantity of the item to update: ')
        inventory.update_quantity(name_update, quantity_update)
    elif option == 3:
        menu_search = """
        ======= Search item by ======
        1. Name
        2. Quantity
        3. Price
        4. Type
        5. Size
        6. Date
        -------------------------
        Enter your choice: """
        option_search = int(input(menu_search))
        if option_search == 1:
            name_search = input('Enter the name of the item to search: ')
            search_result = inventory.search_items('name', name_search)
            for item in search_result:
                print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Type: {item['type']}, Size: {item['size']}, Date: {item['date']}")
        elif option_search == 2:
            quantity_search = int(input('Enter the quantity of the item to search: '))
            search_result = inventory.search_items('quantity', quantity_search)
            for item in search_result:
                print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Type: {item['type']}, Size: {item['size']}, Date: {item['date']}")
        elif option_search == 3:
            price_search = int(input('Enter the price of the item to search: '))
            search_result = inventory.search_items('price', price_search)
            for item in search_result:
                print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Type: {item['type']}, Size: {item['size']}, Date: {item['date']}")
        elif option_search == 4:
            type_search = input('Enter the type of the item to search: ')
            search_result = inventory.search_items('type', type_search)
            for item in search_result:
                print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Type: {item['type']}, Size: {item['size']}, Date: {item['date']}")
        elif option_search == 5:
            size_search = int(input('Enter the size of the item to search: '))
            search_result = inventory.search_items('size', size_search)
            for item in search_result:
                print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Type: {item['type']}, Size: {item['size']}, Date: {item['date']}")
        elif option_search == 6:
            date_search = input('Enter the date of the item to search: ')
            search_result = inventory.search_items('date', date_search)
            for item in search_result:
                print(f"Name: {item['name']}, Quantity: {item['quantity']}, Price: {item['price']}, Type: {item['type']}, Size: {item['size']}, Date: {item['date']}")
    elif option == 4:
        menu_sort = """
        ===== Sort items by ====
        1. Name
        2. Quantity
        3. Price
        4. Type
        5. Size
        6. Date
        -------------------------
        Enter your choice: 
        """
        option_sort = int(input(menu_sort))
        if option_sort == 1:
            inventory_sorted = inventory.sort_inventory('name')
            print("Inventory sorted by name:")
            for item in inventory_sorted:
                print(f"Name: {item['name']}")
        elif option_sort == 2:
            inventory_sorted = inventory.sort_inventory('quantity')
            print("Inventory sorted by quantity:")
            for item in inventory_sorted:
                print(f"Quantity: {item['quantity']}")
        elif option_sort == 3:
            inventory_sorted = inventory.sort_inventory('price')
            print("Inventory sorted by price:")
            print(inventory_sorted)
            for item in inventory_sorted:
                print(f"Price: {item['price']}")
        elif option_sort == 4:
            inventory_sorted = inventory.sort_inventory('type')
            print("Inventory sorted by type:")
            for item in inventory_sorted:
                print(f"Type: {item['type']}")
        elif option_sort == 5:
            inventory_sorted = inventory.sort_inventory('size')
            print("Inventory sorted by size:")
            for item in inventory_sorted:
                print(f"Size: {item['size']}")
        elif option_sort == 6:
            inventory_sorted = inventory.sort_inventory('date')
            print("Inventory sorted by date:")
            for item in inventory_sorted:
                print(f"Date: {item['date']}")
    elif option == 5:
        inventory.generate_inventory_report()
    elif option == 6:
        break
    else:
        print('Invalid option. Please try again. \n')

