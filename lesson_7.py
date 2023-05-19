def task1():
    ipt = input("Введите строку без пробелов: ")
    ipt = ipt.lower()
    mirror = ipt[::-1]
    if ipt == mirror:
        print('yes')
    else:
        print('no')


def task2():
    ipt = (input("Введите строку: ")).split()
    print(' '.join(ipt))


if __name__ == '__main__':
    # task1()
    task2()
