from pprint import pprint

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

    def get_products(self):     # Считывает всю информацию из файла
        file = open(self.__file_name, 'r', encoding='utf-8')
        all_products = file.read()
        file.close()
        return all_products

    def add(self, *products):
        current_products = self.get_products()  # Текущие продукты в файле
        for product in products:                # Проверка продукта на наличие его в файле
            if product.name in current_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a', encoding='utf-8')
                file.write(f'{product}\n')
                current_products += product.name


if __name__ == "__main__":
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())