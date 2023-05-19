def task1():
    n = int(input("Введите количество чисел: "))
    count_of_zero_number = 0
    for i in range(n):
        if int(input(f'{i+1} число: ')) == 0:
            count_of_zero_number += 1
    print("Количество чисел равных нулю в последовательности:",
          count_of_zero_number)


def task2():
    n = int(input("Введите натуральное число: "))
    count_of_nat_div = 0
    for i in range(1, n+1):
        if n % i == 0:
            count_of_nat_div += 1
        if i % 1000000 == 0:
            print('Loading', i)
    print("Количество натуральных делителей числа:", count_of_nat_div)

def task3():
    a = int(input("Введите первое целое число: "))
    b = int(input("Второе целое число: "))
    for i in range(a,b+1):
        if i % 2 == 0:
            print(i, end=' ')

if __name__ == '__main__':
    # task1()
    # task2()
    task3()