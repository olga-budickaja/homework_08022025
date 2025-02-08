# Завдання 3

# Створіть список товарів в інтернет-магазині.
# Серіалізуйте його за допомогою pickle та збережіть у JSON.

import pickle

products = [
    {
        'id': 'defd3242598',
        'name': 'Продукт 1',
        'article': 'M12345',
        'images': ['https://some_site.com/img1.png',
                   'https://some_site.com/img2.png',
                   'https://some_site.com/img3.png'],
        'description': 'Some description about this product',
        'categories': ['Категорія 1', 'Категорія 2'],
        'colors': ['Зелений', 'Сірий'],
        'sizes': ['S', 'M', 'L'],
        'price': 450,
        'sale_price': 0,
        'materials': ['Котон', 'Поліестер'],
        'brand': 'Brand1'
    },
    {
        'id': 'a23b6789cde',
        'name': 'Продукт 2',
        'article': 'X98765',
        'images': ['https://some_site.com/img4.png',
                   'https://some_site.com/img5.png'],
        'description': 'Another great product with amazing features',
        'categories': ['Категорія 3'],
        'colors': ['Червоний', 'Синій'],
        'sizes': ['XS', 'M', 'XL'],
        'price': 600,
        'sale_price': 550,
        'materials': ['Бавовна', 'Льон'],
        'brand': 'Brand2'
    },
    {
        'id': 'b56d982134a',
        'name': 'Продукт 3',
        'article': 'Y45678',
        'images': ['https://some_site.com/img6.png'],
        'description': 'Stylish and comfortable product for everyday use',
        'categories': ['Категорія 2', 'Категорія 4'],
        'colors': ['Чорний', 'Білий'],
        'sizes': ['S', 'L'],
        'price': 750,
        'sale_price': 700,
        'materials': ['Шкіра'],
        'brand': 'Brand1'
    },
    {
        'id': 'c91f8345d67',
        'name': 'Продукт 4',
        'article': 'Z32145',
        'images': ['https://some_site.com/img7.png',
                   'https://some_site.com/img8.png'],
        'description': 'Premium quality product for special occasions',
        'categories': ['Категорія 5'],
        'colors': ['Зелений', 'Сірий'],
        'sizes': ['M', 'L', 'XXL'],
        'price': 1200,
        'sale_price': 1100,
        'materials': ['Шовк', 'Поліестер'],
        'brand': 'Brand4'
    },
    {
        'id': 'e77g2438h56',
        'name': 'Продукт 5',
        'article': 'W65432',
        'images': ['https://some_site.com/img9.png'],
        'description': 'Eco-friendly and sustainable product',
        'categories': ['Категорія 1', 'Категорія 6'],
        'colors': ['Бежевий'],
        'sizes': ['XS', 'S', 'M'],
        'price': 350,
        'sale_price': 300,
        'materials': ['Бамбук', 'Органічний хлопок'],
        'brand': 'Brand4'
    }
]


with open("products.pkl", "wb") as file:
    pickle.dump(products, file)

with open("products.pkl", "rb") as file:
    loaded_data = pickle.load(file)

print(loaded_data)
