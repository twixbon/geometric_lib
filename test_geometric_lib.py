import unittest
import math
from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class TestGeometricLib(unittest.TestCase):
    # ТЕСТЫ ДЛЯ КРУГА
    def test_circle_basic(self):
        self.assertAlmostEqual(circle_area(5), math.pi * 25)
        self.assertAlmostEqual(circle_perimeter(3), 2 * math.pi * 3)
    
    def test_circle_edge_cases(self):
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_perimeter(0), 0)
        with self.assertRaises(ValueError):
            circle_area(-2)

    # ТЕСТЫ ДЛЯ КВАДРАТА
    def test_square_basic(self):
        self.assertEqual(square_area(5), 25)
        self.assertEqual(square_perimeter(4), 16)
    
    def test_square_edge_cases(self):
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_perimeter(0), 0)
        with self.assertRaises(ValueError):
            square_area(-3)

    # ТЕСТЫ ДЛЯ ПРЯМОУГОЛЬНИКА
    def test_rectangle_basic(self):
        self.assertEqual(rectangle_area(5, 4), 20)
        self.assertEqual(rectangle_perimeter(3, 7), 20)
        self.assertEqual(rectangle_area(10, 10), 100) 
    
    def test_rectangle_edge_cases(self):
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(5, 0), 0)
        with self.assertRaises(ValueError):
            rectangle_area(-1, 5)

    # ТЕСТЫ ДЛЯ ТРЕУГОЛЬНИКА
    def test_triangle_basic(self):
        self.assertEqual(triangle_area(6, 4), 12)
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
    
    def test_triangle_edge_cases(self):
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)
        with self.assertRaises(ValueError):
            triangle_area(-2, 3)

    # ТЕСТЫ ДЕСЯТИЧНЫХ ЧИСЕЛ
    def test_decimal_numbers(self):
        self.assertEqual(rectangle_area(2.5, 4), 10.0)
        self.assertAlmostEqual(circle_area(2.5), math.pi * 6.25)
        self.assertEqual(square_area(2.5), 6.25)

    # ТЕСТЫ БОЛЬШИХ ЧИСЕЛ
    def test_large_numbers(self):
        self.assertEqual(rectangle_area(1000, 500), 500000)
        self.assertEqual(square_area(100), 10000)

    # КОМПЛЕКСНЫЕ ТЕСТЫ
    def test_multiple_shapes(self):
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertEqual(square_area(2), 4)
        self.assertEqual(rectangle_area(3, 4), 12)
        self.assertEqual(triangle_area(4, 3), 6)

