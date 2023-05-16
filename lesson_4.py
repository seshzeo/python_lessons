def task1():
    a = float(input("Первая сторона прямоугольника: "))
    b = float(input("Вторая сторона прямоугольника: "))
    print("Площадь равна ", a*b)


def task2():
    ipt = input("Введите пятизначное целое число: ")
    ipt_arr = []
    for i in ipt:
        ipt_arr.append(int(i))

    print(((ipt_arr[3]**ipt_arr[4])*ipt_arr[2])/(ipt_arr[0]-ipt_arr[1]))


if __name__ == '__main__':
    # task1()
    task2()
