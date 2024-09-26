class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        prod = open(self.__file_name, 'r')
        read_ = prod.read()
        prod.close()
        return read_

    def add(self, *products):
        get = self.get_products()
        prod = open(self.__file_name, 'a')
        for product in products:
            if str(product) not in get:
                prod.write(f'{str(product)}\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')
        prod.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
