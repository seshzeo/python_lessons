import math


class Cash_rgstr(object):
    __content_cache = 0.0

    def __init__(self):
        self.__content_cache = 0.0

    def top_up(self, cash_to_add):
        if cash_to_add < 0:
            raise ValueError("Cash to add can`t be < 0")
        else:
            self.__content_cache += cash_to_add

    def count_1000(self):
        print(int(self.__content_cache//1000))

    def take_away(self, cash_to_take):
        if cash_to_take > self.__content_cache:
            raise ValueError("Not enought cash")
        else:
            self.__content_cache -= cash_to_take

    def get_content_cash(self) -> float:
        return self.__content_cache


class Turtle(object):
    __x = 0
    __y = 0
    __step = 1

    # движение по координотной сетке с учетом, что [0, 0] в нижнем левом углу

    def __init__(self, x, y, step):
        self.__x = x
        self.__y = y
        self.__step = step

    def go_up(self):
        self.__y += self.__step

    def go_down(self):
        self.__y -= self.__step

    def go_left(self):
        self.__x -= self.__step

    def go_right(self):
        self.__x += self.__step

    def evolve(self):
        self.__step += 1

    def degrade(self):
        if self.__step <= 1:
            raise RuntimeError("Speed can`t be <=1")
        else:
            self.__step -= 1

    def count_moves(self, target_x, target_y):
        return (abs(target_x - self.__x)//self.__step)+(abs(target_y - self.__y)//self.__step)

    def get_pos(self) -> list:
        return [self.__x, self.__y]


def task1():
    any_cassa = Cash_rgstr()

    print(any_cassa.get_content_cash())
    any_cassa.top_up(10235)
    print(any_cassa.get_content_cash())
    any_cassa.count_1000()

    try:
        any_cassa.take_away(100000)  # exception
        print('Successfully')
        print(any_cassa.get_content_cash())

        any_cassa.top_up(-1200)  # exception
        print('Successfully')
        print(any_cassa.get_content_cash())

    except BaseException as e:
        print(e)


def task2():
    any_t = Turtle(10, 10, 2)
    print(any_t.count_moves(23, 23))
    print(any_t.get_pos())
    # any_t.go_down()
    # any_t.go_right()
    any_t.go_up()
    any_t.go_left()
    print(any_t.get_pos())


if __name__ == '__main__':
    task1()
    # task2()
