my_dict = {
    "Timur":"ул.Пушкина,д.Колотушкина",
    "Iliy":"ул.Разбитых фонарей,д.16",
    'Bob': 'ул.Забвения,д.2'
}
print("Здравствуйте!!!")
inp = input("желаете изменить список жми 1, желаете просмотреть жми 0:")
inp = int(inp)
if inp == 1:
    name = input("введите имя для изменения адреса:")
    new_address = input("введите новый адрес:")
    if name in my_dict:
        my_dict[name] = new_address
    else:
        my_dict.setdefault(name, new_address)
    print(my_dict.items())
    '''
    for k,v in my_dict.items():

    print(f"{k}:{v}")
    '''
    print("желаете что-то удалить?")
    inp1 = input("если да пиши 1, если нет пиши 0:")
    inp1 = int(inp1)
    if inp1 == 1:
        name1 = input("введите имя которое хотите удалить:")
        del my_dict[name1]
    else:
        print("хорошо")
else:
    print("хорошо!")
print(my_dict.items())
