def task1():
    lst = [int(input(f"{i+1} число: "))
           for i in range(int(input("Введите количество чисел: ")))]
    lst.reverse()
    print(*lst)


def task2():
    # size не понадобился
    size = int(input("Введите количество чисел: "))
    ipt = list(map(int, input(
        "Введите последовательность чисел через пробел: ").split()))
    print(*(ipt[-1:]+ipt[:-1]))


def task3():
    boat_count = 0
    boat_capacity = int(
        input("Укажите вместимость одной лодки: "))
    fishermens_number = int(
        input("Укажите количество рыбаков: "))
    fishermens_weight = [
        int(input(f"Вес {i+1} рыбака: ")) for i in range(fishermens_number)]
    while fishermens_weight:
        tmp = fishermens_number+1
        sum_weight = 0
        for j in range(1, len(fishermens_weight)):
            if fishermens_weight[0] > boat_capacity or fishermens_weight[j] > boat_capacity:
                tmp = fishermens_number+2
                print(
                    "Лодка не может выдержать одного из рыбаков.")
                print("Всех перевезти не получится.")
                break
            if fishermens_weight[0]+fishermens_weight[j] > sum_weight and fishermens_weight[0]+fishermens_weight[j] <= boat_capacity:
                sum_weight = fishermens_weight[0]+fishermens_weight[j]
                tmp = j
        if tmp == fishermens_number+2:
            break
        if tmp == fishermens_number+1:
            fishermens_weight.pop(0)
        else:
            fishermens_weight.pop(tmp)
            fishermens_weight.pop(0)
        boat_count += 1
    if tmp != fishermens_number+2:
        print(boat_count)


if __name__ == '__main__':
    # task1()
    # task2()
    task3()
