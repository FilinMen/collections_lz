my_dict = {
    "Timur":"ул.Пушкина,д.Колотушкина",
    "Iliy":"ул.Разбитых фонарей,д.16",
    'Bob': 'ул.Забвения,д.2'
}
print("Здравствуйте!!!")
inp = input("изменить адресс жми 1, удаление записи жми 2, просмотр списка жми 0:")
inp = int(inp)
if inp == 1:
    print(my_dict)
    name = input("введите имя для изменения адреса:")
    new_address = input("введите новый адрес:")
    if name in my_dict: # проверка наналичие имени в списке
        my_dict[name] = new_address # замена адреса если имя оказалось в списке
        print(my_dict.items()) #вывод финального списка
    else:
        my_dict.setdefault(name, new_address) # если имени нет в списке, мы добовляем имя и адресс в конец списка
        print(my_dict.items()) #вывод финального списка
elif inp == 2:
    print(my_dict)
    name1 = input("введите имя которое хотите удалить:")
    del my_dict[name1] # удаляем элемент из списка
    print(my_dict.items()) #вывод финального списка
else:
    print("хорошо!")
    print(my_dict.items()) #вывод финального списка
    


