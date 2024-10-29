my_dict = {
    "Timur":"ул.Пушкина,д.Колотушкина",
    "Iliy":"ул.Разбитых фонарей,д.16",
    'Bob': 'ул.Забвения,д.2'
}
print("Здравствуйте!!!")
inp = input("желаетеизменить список жми 1, желаете просмотреть жми 0:")
if inp == 1:
    name = input("введите имя для изменения адреса:")
    new_address = input("введите новый адрес:")
else:
    print("хорошо!")

for k,v in my_dict.items():
    print(f"{k}:{v}")
    if name in my_dict:
        my_dict[name] = new_address
    else:
     my_dict.setdefault(name, new_address)

print("хотити что-то удалить?")
inp1 = input("если да пиши 1, если нет пиши 0:")
if inp1 == 1:
    del my_dict[name]
