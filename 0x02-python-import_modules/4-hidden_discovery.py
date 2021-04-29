#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
        lista = dir(hidden_4)
        for i in range(len(lista)):
                if lista[i][0:2] != '__':
                        print("{}".format(lista[i]))
