import numpy as np
from tabulate import *

lst = np.loadtxt("sol_lab4_input.txt", dtype='U', encoding='utf-8', delimiter=',')

camaro = round(float(lst[1][2]) * float(lst[1][3]) + float(lst[2][2]) * float(lst[2][3]) + float(lst[3][2]) * float(
    lst[3][3]) + float(lst[4][2]) * float(lst[4][3]) + float(lst[5][2]) * float(lst[5][3]), 2)

mustang = round(float(lst[1][2]) * float(lst[1][4]) + float(lst[2][2]) * float(lst[2][4]) + float(lst[3][2]) * float(
    lst[3][4]) + float(lst[4][2]) * float(lst[4][4]) + float(lst[5][2]) * float(lst[5][4]), 2)

charger = round(
    float(lst[1][2]) * float(lst[1][5]) + float(lst[2][2]) * float(lst[2][5]) + float(lst[3][2]) * float(
        lst[3][5]) + float(lst[4][2]) * float(lst[4][5]) + float(lst[5][2]) * float(lst[5][5]), 2)

challenger = round(float(lst[1][2]) * float(lst[1][6]) + float(lst[2][2]) * float(lst[2][6]) + float(lst[3][2]) * float(
    lst[3][6]) + float(lst[4][2]) * float(lst[4][6]) + float(lst[5][2]) * float(lst[5][6]), 2)

firebird = round(float(lst[1][2]) * float(lst[1][7]) + float(lst[2][2]) * float(lst[2][7]) + float(lst[3][2]) * float(
    lst[3][7]) + float(lst[4][2]) * float(lst[4][7]) + float(lst[5][2]) * float(lst[5][7]), 2)

coronet = round(float(lst[1][2]) * float(lst[1][8]) + float(lst[2][2]) * float(lst[2][8]) + float(lst[3][2]) * float(
    lst[3][8]) + float(lst[4][2]) * float(lst[4][8]) + float(lst[5][2]) * float(lst[5][8]), 2)

best_musclecar = {camaro: lst[0, 3], mustang: lst[0, 4], charger: lst[0, 5], challenger: lst[0, 6],
                  firebird: lst[0, 7], coronet: lst[0, 8]}
best_musclecar = best_musclecar.get(max(best_musclecar))

arr = lst.reshape(6, 9)
arr = np.delete(arr, 0, axis=0)
arr = np.delete(arr, [0,1], axis=1)
suma = arr.astype(float).sum(axis=0)

print(tabulate(headers=[lst[0][0], lst[0][1], lst[0][2], lst[0][3], lst[0][4], lst[0][5], lst[0][6], lst[0][7], lst[0][8]], tabular_data=[
    [lst[1][0], lst[1][1], lst[1][2], lst[1][3], lst[1][4], lst[1][5], lst[1][6], lst[1][7], lst[1][8]],
    [lst[2][0], lst[2][1], lst[2][2], lst[2][3], lst[2][4], lst[2][5], lst[2][6], lst[2][7], lst[2][8]],
    [lst[3][0], lst[3][1], lst[3][2], lst[3][3], lst[3][4], lst[3][5], lst[3][6], lst[3][7], lst[3][8]],
    [lst[4][0], lst[4][1], lst[4][2], lst[4][3], lst[4][4], lst[4][5], lst[4][6], lst[4][7], lst[4][8]],
    [lst[5][0], lst[5][1], lst[5][2], lst[5][3], lst[5][4], lst[5][5], lst[5][6], lst[5][7], lst[5][8]],
    ["Сума", '',suma[0], suma[1], suma[2], suma[3], suma[4], suma[5], suma[6]]
]))

print(f'Результат оцінки експертів - {best_musclecar}')
