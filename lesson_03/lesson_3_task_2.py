from smartphone import Smartphone

# Объявляем переменную catalog - это список для хранения объектов
catalog = []

# Наполняем список пятью разными экземплярами класса Smartphone
catalog.append(Smartphone("Apple", "Iphone 13", "79961962345"))
catalog.append(Smartphone("Nokia", "3310", "79876541236"))
catalog.append(Smartphone("Samsung", "S24 Ultra", "79634521236"))
catalog.append(Smartphone("Huawei", "A33", "79865462312"))
catalog.append(Smartphone("Xiaomi", "Mi 11", "79635648974"))

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")