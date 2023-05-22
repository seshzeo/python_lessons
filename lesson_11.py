def fact(n):
    if n == 0 or n ==1:
        return 1
    return n * fact(n-1)

def task1():
    n = int(input("Введите натуральное целое число: "))
    factorial_n = fact(n)
    lst = []
    for i in range(factorial_n):
        lst.append(fact(factorial_n))
        factorial_n -= 1
    print(lst)


def task2():
    import os
    import collections
    keys = ["Вид питомца", "Возраст питомца", "Имя владельца"]
    pets = {1:{'Мухтар':{"Вид питомца": "Собака", "Возраст питомца": 9, "Имя владельца": "Павел"}},
            2:{'Каа':{"Вид питомца": "Питон", "Возраст питомца": 12, "Имя владельца": "Сергей"}},
            3:{'Сима':{"Вид питомца": "Кошка", "Возраст питомца": 2, "Имя владельца": "Ирина"}}}

    def pets_list(pets):        # упорялоченный принт БД 
        for key in pets.keys():
            print(f"{key}:")
            any_pet = get_pet(key)
            if not any_pet:
                print("Error. No such id exists")
            else:
                name = any_pet[0]
                print(f"\tИмя питомца: {name}")
                for key, value in zip(keys, list(any_pet[1:])):
                    if key == "Возраст питомца":
                        print(f"\t{key}: {value}{get_suffix(value)}")
                    else:
                        print(f"\t{key}: {value}")

    def get_suffix(age):        # возвращает корректный суффикс года
        if age > 10 and age < 19:
            return ' лет'
        else:
            if age % 10 > 4 or age % 10 == 0:
                return ' лет'
            elif age % 10 == 1:
                return ' год'
            else:
                return ' года'

    def get_pet(pet_id):        # возвращает список с параметрами из БД. Вспомогательная ф-я.
        if pet_id in pets.keys():
            result = []
            name = str(*(pets[pet_id].keys()))
            result.append(name)
            for el in keys:
                result.append(pets[pet_id][name][el])
            return result
        else:
            return False

    def push_pet(index, lst):   # вставка карточки питомца в БД. Вспомогательная ф-я.
        pets[index] = {lst[0]: {"Вид питомца":lst[1],
                          "Возраст питомца":int(lst[2]),
                          "Имя владельца":lst[3]}}
        
    def create():               # создать запись и добавить в бд
        last = collections.deque(pets, maxlen=1)[0]
        last +=1
        push_pet(last, [input("Имя питомца: "),
                        input("Вид питомца: "),
                        int(input("Возраст: ")),
                        input("Имя владельца: ")])
        print("\nПитомец добавлен")

    def read(pet_id):           # отображение инфы о питомце в определенном формате
        print_lst = get_pet(pet_id)
        if not print_lst:
            print("Error. No such id exists")
        else:
            print("Это ", print_lst[1], " по кличке \"", print_lst[0],
                  "\". Возраст: ", print_lst[2], get_suffix(print_lst[2]), '. Имя владельца: ',
                  print_lst[3], sep='')

    def update(pet_id):         # обновляет уже созданную запись
        chck_inx = get_pet(pet_id)
        if not chck_inx:
            print("Error. No such id exists")
        else:
            push_pet(pet_id, [input("Имя питомца: "),
                              input("Вид питомца: "),
                              int(input("Возраст: ")),
                              input("Имя владельца: ")])
            print("\nИнформация обновлена")

    def delete(pet_id):         # удаляет уже существующую запись
        chck_inx = get_pet(pet_id)
        if not chck_inx:
            print("Error. No such id exists")
        else:
            del pets[pet_id]
            print("\nПитомец удален")

    
    is_work = True
    while is_work:   
        print("БД ветклиники\n")
        print("1. Посмотреть БД")
        print("2. Добавить питомца")
        print("3. Посмотреть информацию о питомце")
        print("4. Обновить информацию о питомце")
        print("5. Удалить питомца из БД")
        print("\"stop\". Выход")
        ipt = input("[1/2/3/4/5/stop]: ")
        os.system("cls")
        if ipt == 'stop':
            print("Закрытие программы.")
            is_work = False
        elif ipt == '1':
            pets_list(pets)
        elif ipt == '2':
            create()
        elif ipt == '3':
            read(int(input("Введите id питомца: ")))
        elif ipt == '4':
            update(int(input("Введите id питомца: ")))
        elif ipt == '5':
            delete(int(input("Введите id питомца: ")))
        else:
            print("Некорректный ввод.")


if __name__ == '__main__':
    task2()