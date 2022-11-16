""" En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce. """

from functools import reduce

list_numbers = []

for x in range(1, 101):
    list_numbers.append(x)


def getOdd(x):
    if x % 2 != 0:
        return True


odd_numbers = filter(getOdd, list_numbers)

odd_list = []

for x in odd_numbers:
    odd_list.append(x)

print(odd_list)


odd_sum = reduce(lambda a, b: a + b, odd_list)

print("La suma de los números impares es", odd_sum)
