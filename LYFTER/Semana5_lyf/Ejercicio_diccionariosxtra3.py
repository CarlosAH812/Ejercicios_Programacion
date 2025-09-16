products = [
    {"name": "Monitor", "category": "Electronic", "price": 200},
    {"name": "Teclado", "category": "Electronic", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electronic", "price": 25},
]

totals = {}

for product in products:
    category = product['category']
    price = product['price']
    
    if category in totals:
        totals[category] += price
    else:
        totals[category] = price

print(totals)