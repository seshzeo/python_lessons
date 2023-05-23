import random as rd

if __name__ == '__main__':
    x = int(input('x = '))
    y = int(input('y = '))

    def print_m(any_m):
        for el in any_m:
            print(*el)
        print()

    def sum_m(a_m, b_m):
        res_m = [[0 for i in range(y)] for i in range(x)]
        for i in range(x):
            for j in range(y):
                res_m[i][j] = a_m[i][j] + b_m[i][j]

        return res_m

    matrix_1 = [[rd.randint(-67, 178) for i in range(y)] for i in range(x)]
    matrix_2 = [[rd.randint(-67, 178) for i in range(y)] for i in range(x)]

    print('matrix_1:')
    print_m(matrix_1)
    print('matrix_2:')
    print_m(matrix_2)
    
    print('matrix_3:')
    print_m(sum_m(matrix_1,matrix_2))
