from smartphone import Smartphone



catalog = [

    Smartphone("Apple", "iPhone 16", "+79111111114"),

    Smartphone("Samsung", "Galaxy S23", "+79222222225"),

    Smartphone("Xiaomi", "12 Ultra", "+79333333336"),

    Smartphone("Google", "Pixel 9 Pro", "+79444444447"),

    Smartphone("Huawei", "Pura 80", "+79555555559")

]
for phone in catalog:
    print(f"{phone.brand} --> {phone.model}. Телефон: {phone.phone_number}")