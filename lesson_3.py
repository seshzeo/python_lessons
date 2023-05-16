def task1():
    pet_breed = 'пес'
    pet_age = 7
    pet_name = 'Арчи'

    prints = ["Введите вид питомца: ",
              "Введите его возраст: ", "А теперь кличку: "]
    pet_info = [pet_breed, pet_age, pet_name]

    for i in range(0, 3, 1):
        pet_info[i] = input(prints[i])

    pet_info[1] = int(pet_info[1])

    type_of_years = ' года'
    if pet_info[1] % 10 > 4 or pet_info[1] % 10 == 0:
        type_of_years = ' лет'
    elif pet_info[1] % 10 == 1:
        type_of_years = ' год'
    print("Это ", pet_info[0], " по кличке \"", pet_info[2],
          "\". Возраст: ", pet_info[1], type_of_years, '.', sep='')


def task2(question, sep, right_answee_list):
    user_answer_list = []
    answer = ''
    print(question)
    print(
        "или введите слово [конец] когда закончите")
    while True:
        answer = input()
        if answer == 'конец':
            break
        else:
            user_answer_list.append(answer)
            print('Следующий: ')
    print("Ваш ответ:", sep.join(user_answer_list))
    print("Правильный ответ:", sep.join(right_answee_list))


if __name__ == "__main__":
    # task1()

    rt_anw_lst = ['дриопитек', 'рамапитек', 'австралопитек', 'человек умелый',
                  'человек прямоходящий', 'неандертальский человек', 'неоантроп']
    task2("Введите этапы развития человечества ",
          ' => ', rt_anw_lst)
