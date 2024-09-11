def get_costumer_information():
    name = input('Por favor ingresa tu nombre: ')
    dni = input('Por favor ingresa tu cédula: ')
    client = {
        "name": name,
        "dni": dni
    }
    return client


def add_to_basket(menu):
    for idx, item in enumerate(menu):
        print(f'{idx}. {item["name"]} - {item["price"]}')
    ans = 'n'
    order = []
    while ans == 'n':
        index = int(input('Por favor ingrese el número del elemento: '))
        qty = int(input('Por favor ingresa la cantidad de elementos a comprar: '))
        item = menu[index]
        order.append({
            "qty": qty,
            "name": item["name"],
            "price": item["price"]
        })
        ans = input('Termino de comprar (y/n)?: ')

    return order


def calculate_subtotal(order):
    subtotal = 0
    for item in order:
        subtotal += item["price"] * item["qty"]
    return subtotal


def calculate_tax(subtotal):
    return subtotal * 0.16
