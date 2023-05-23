def list_print(any_lst):
    if any_lst:
        print(any_lst.pop(0))
        list_print(any_lst)
    else:
        print("Конец списка")


if __name__ == '__main__':
    my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    list_print(my_list)
