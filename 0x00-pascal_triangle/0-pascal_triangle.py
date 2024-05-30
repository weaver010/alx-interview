#!/usr/bin/python3


def pascal_triangle(n):
    result = []
    for i in range(n):
        num = 11 ** i
        list_d = list(str(num))
        result.append(list_d)
    return result
