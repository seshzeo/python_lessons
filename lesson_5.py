def task1():
    ipt = int(input("Введите целое число: "))
    opt = []
    if ipt == 0:
        opt.append("Нулевое")
    else:
        if ipt > 0:
            opt.append("Положительное")
        elif ipt < 0:
            opt.append("Отрицательное")

        if ipt % 2 == 0:
            opt.append("четное")
        else:
            opt.append("нечетное")

    opt.append("число.")
    # По тз нужно дополнительно выводить строчку ниже, если условия подходят.
    # Странно кншн, если проверка уже есть выше
    if not ipt % 2 == 0:
        opt.append("Число не является четным.")

    print(' '.join(opt))


def task2():
    ipt = input(
        "Введите слово из мельньких латинсикх букв: ")
    vower_dic = {'a': 0, 'e': 0, 'i': 0, 'o': 0}
    is_vower_list = []
    vower_count = 0

    for char in ipt:
        for key in vower_dic.keys():
            if char == key:
                vower_count += 1
                vower_dic[key] += 1

    for key, value in vower_dic.items():
        if value == 0:
            print(key, ': False')
        else:
            print(key, value, sep=' : ')
    print("Количество гласных:", vower_count, "шт")
    print("Количество согласных:", len(ipt) - vower_count, "шт")


def task3():
    class Partner:
        def __init__(self, name, cash):
            self.name = name
            if cash > 0:
                self.cash = cash
            else:
                self.cash = 0

    min_invest_amount = float(input("Введите минимальную сумму инвестиций: "))
    partners_cash = 0
    he_may_invest = ''
    investers_ammount = 0
    result = ''

    partners = [Partner('Mike',float(input("Сколько долларов у Майкла?: "))),
                Partner('Ivan',float(input("Сколько долларов у Ивана?: ")))]

    for partner in partners:
        partners_cash += partner.cash
        if partner.cash >= min_invest_amount:
            he_may_invest = partner.name
            investers_ammount += 1

    if he_may_invest != '' and investers_ammount < 2:
        result = he_may_invest    
    elif investers_ammount >= 1:
        result = investers_ammount
    elif partners_cash >= min_invest_amount:
        result = 1
    else:
        result = 0
    print(result)

if __name__ == '__main__':
    # task1()
    # task2()
    task3()
