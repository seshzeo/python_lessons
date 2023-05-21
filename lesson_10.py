def task1():
    import os
    pets = {}
    def new_pet(pet_name, pet_breed, pet_age, owner_name):
        pets[pet_name] = {"Вид питомца":pet_breed,
                          "Возраст питомца":int(pet_age),
                          "Имя владельца":owner_name}
    def show_pets_dict():
        print(pets)
    def print_pet(pets, name):
        type_of_years = ' года'
        if pets[name]["Возраст питомца"] > 10 and pets[name]["Возраст питомца"] < 19:
            type_of_years = ' лет'
        else:
            if pets[name]["Возраст питомца"] % 10 > 4 or pets[name]["Возраст питомца"] % 10 == 0:
                type_of_years = ' лет'
            elif pets[name]["Возраст питомца"] % 10 == 1:
                type_of_years = ' год'

        print("Это ", pets[name]["Вид питомца"], " по кличке \"", name,
              "\". Возраст: ", pets[name]["Возраст питомца"], type_of_years, '. Имя владельца: ',
              pets[name]["Имя владельца"], sep='')

    is_work = True
    while is_work:   
        print("БД ветклиники\n")
        print("1. Посмотреть БД")
        print("2. Добавить питомца")
        print("3. Посмотреть информацию о питомце")
        print("4. Удалить питомца из БД")
        print("0. Выход")
        ipt = input("[1/2/3/4/0]: ")
        os.system("cls")
        if ipt == '0':
            print("Закрытие программы.")
            is_work = False
        elif ipt == '1':
            show_pets_dict()
        elif ipt == '2':
            name = input("Имя питомца: ")
            if name in pets.keys():
                print("Такой питомец уже есть в БД")
            else:
                breed = input("Вид питомца: ")
                age = int(input("Возраст: "))
                owner_name = input("Имя владельца: ")
                new_pet(name, breed, age, owner_name)
                print(f"{name} добавлен")
        elif ipt == '3':
            name = input("Введите имя питомца: ")
            if not name in pets.keys():
                print("Нет такого питомца в БД")
            else:
                print_pet(pets, name)
        elif ipt == '4':
            name = input("Имя питомца: ")
            if name in pets.keys():
                pets.pop(name)
                print(f"{name} удален")
            else:
                print("Нет такого питомца в БД")
        else:
            print("Некорректный ввод.")


def task2():
    a = int(input("Начальное значение: "))
    b = int(input("Конечное значение: "))
    ipt_dict = dict()
    it = 0
    if a >= b:
        it = -1
    else:
        it = 1
    for i in range(a, b+it, it):
        ipt_dict[i] = float(i**i)
    print(ipt_dict)


if __name__ == '__main__':
    # task1()
    task2()
