def area(a, b):
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a * b

def perimeter(a, b):
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return (a + b) * 2