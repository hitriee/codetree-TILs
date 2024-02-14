class Product:
    def __init__(self, name='codetree', code='50'):
        self.name = name
        self.code = code

products = [Product(), Product(*input().split())]

for product in products:
    print(f'product {product.code} is {product.name}')