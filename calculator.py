class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if b >= 0:
            for _ in range(b):
                result = self.add(result, a)
        else:
            for _ in range(-b):
                result = self.add(result, -a)
        return result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("division by zero")

        is_negative = (a < 0 and b > 0) or (a > 0 and b < 0)

        dividend = self.subtract(0, a) if a < 0 else a
        divisor = self.subtract(0, b) if b < 0 else b

        result = 0
        while dividend >= divisor:
            dividend = self.subtract(dividend, divisor)
            result = self.add(result, 1)
        return self.subtract(0, result) if is_negative else result
    
    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("modulo by zero")
        if b > 0:
            while a >= b:
                a = self.subtract(a, b)
            while a < 0:
                a = self.add(a, b)
        else:
            while a <= b:
                a = self.subtract(a, b)
            while a > 0:
                a = self.add(a, b)
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(-2, -3))
    print("Example: division: ", calc.divide(-10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
