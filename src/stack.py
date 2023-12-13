from copy import deepcopy


class Stack:

    def __init__(self):
        self.__stack = []

    def insert(self, *args):
        for x in args:
            self.__stack.insert(0, x)

        return self

    def remove(self):
        return self.__stack.pop(0)

    def size(self):
        return len(self.__stack)

    def items(self):
        return self.__stack

    def clear(self):
        self.__stack = []

    def copy(self):
        return deepcopy(self)

    def __repr__(self):
        return f'Stack({self.__stack})'

    def __eq__(self, other):
        return self.__stack == other.__stack