def task1():
    n = input("Введите количество чисел: ")
    ipt_set = set(map(int, input(
        "Последовательность чисел через пробел: ").split(' ')))
    print(len(ipt_set))


def task2():
    fst_n = int(input(
        "Введите количество чисел в первой последовательности: "))
    fst_lst = [input(f"{i+1} число: ") for i in range(fst_n)]
    sec_n = int(input(
        "Введите количество чисел в первой последовательности: "))
    sec_lst = [input(f"{i+1} число: ") for i in range(sec_n)]
    res = len(set(fst_lst).intersection(set(sec_lst)))
    print(res)


def task3():
    ipt_list = list(map(int, input(
        "Последовательность чисел через пробел: ").split(' ')))
    set_for_check = set()
    for i in ipt_list:
        if i in set_for_check:
            print("YES")
        else:
            print("NO")
            set_for_check.add(i)


if __name__ == '__main__':
    # task1()
    # task2()
    task3()
