class Calculator:

    def div(self, x: int | float, y: int | float) -> int | float:
        for e in x, y:
            if not isinstance(e, int | float):
                raise TypeError

        if y == 0:
            raise ZeroDivisionError

        return x / y

    def add(self, x: int | float, y: int | float) -> int | float:
        for e in x, y:
            if not isinstance(e, int | float):
                raise TypeError

        return x + y
