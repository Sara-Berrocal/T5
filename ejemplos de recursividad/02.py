#Suma de una lista
import os 
os.system("cls")

def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst [0] + sum_list(lst[1:])
print(sum_list([1, 2, 3, 4, 5,6]))
