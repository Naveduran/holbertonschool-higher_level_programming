#!/usr/bin/python3
def uppercase(str): #objetivo: imprimir una string en minuscula
    for i in range(len(str)):
        num = ord(str[i])
        if num >= 97 and num <= 122:
            num = num - 32
        print("{:c}".format(num), end='')
    print()
