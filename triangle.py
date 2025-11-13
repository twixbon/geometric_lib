def area(a, h):
    if a < 0 or h < 0:
        raise ValueError("Основание и высота не могут быть отрицательными")
    return a * h / 2

def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a + b + c