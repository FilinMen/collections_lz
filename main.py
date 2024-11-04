# Словарь с именами и адресами
address_book = {
    "Дмитрий": "ул. Ленина, д. 1",
    "Тимур": "ул. Пушкина, д. 2",
    "Флувдия": "ул. Лермонтова, д. 3"
}

# Ввод имени и нового адреса с клавиатуры
name = input("Введите имя для обновления адреса: ")
new_address = input("Введите новый адрес: ")

# Обновление адреса в словаре
if name in address_book:
    address_book[name] = new_address
    print(f"Адрес для {name} обновлен на {new_address}.")
else:
    print(f"Контакт {name} не найден в адресной книге.")

# Ввод имени для удаления его данных
name = input("Введите имя для удаления: ")
del address_book[name]

# Печать обновленного словаря
print("Обновленная адресная книга:")
for name, address in address_book.items():
    print(f"{name}: {address}")