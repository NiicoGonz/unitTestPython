from math_v01 import *
import unittest

class TestMath(unittest.TestCase):
    #los metodos de testeo simpre deben empezar por test
    def test_division(self):
        #caso 1
        result = division(5, 2)
        self.assertEqual(2.5, result)
        #caso 2
        result = division(2, 5)
        self.assertEqual(0.4, result)
        #caso 3
        result = division(0, 10)
        self.assertEqual(0, result)
        #caso 4
        result = division(10, 0)
        self.assertEqual("No se puede dividir entre cero", result)
        #caso 5
        result = division(-10, 5)
        self.assertEqual(-2, result)
        #caso 6
        result = division(10, -5)
        self.assertEqual(-2, result)
    

    def test_area_rec(self):
        #caso1
        result = area_rec(10, 2)
        self.assertEqual(20, result)
        #caso2
        result = area_rec(5, 20)
        self.assertEqual(100, result)
        #caso3
        result = area_rec(0, 10)
        self.assertEqual(0, result)
        #caso4
        result = area_rec(20, 0)
        self.assertEqual(0, result)
        #caso5
        result = area_rec(-10, 2)
        self.assertEqual("areas negativas no existen", result)
        #caso6
        result = area_rec(5, -2)
        self.assertEqual("areas negativas no existen", result)
        #caso7
        result = area_rec(-5, -2)
        self.assertEqual("areas negativas no existen", result)

    def test_area_circ(self):
        #caso1
        result= area_circ(2)
        self.assertEqual(12.56, result)
        #caso2
        result = area_circ(-2)
        self.assertEqual("areas negativas no existen", result)

        #caso3
        result = area_circ(4)
        self.assertEqual(50.24, result)
        #caso4
        result = area_circ(-4)
        self.assertEqual("areas negativas no existen", result)
        #caso5
        result = area_circ(12)
        self.assertEqual(452.16, result)
        #caso6
        result = area_circ(-12)
        self.assertEqual("areas negativas no existen", result)
        #caso7
        result = area_circ(23)
        self.assertEqual(1661.0600000000002, result)

    def test_perime_circu(self):
        #caso1
        result=perime_circu(12)
        self.assertEqual(75.36,result)
        #caso2
        result = perime_circu(-12)
        self.assertEqual("el perimetro de un circulo no puede ser negativo", result)
        #caso3
        result = perime_circu(23)
        self.assertEqual(144.44, result)
        #caso4
        result = perime_circu(-23)
        self.assertEqual(
            "el perimetro de un circulo no puede ser negativo", result)
        #caso5
        result=perime_circu(2)
        self.assertEqual(12.56,result)
        #caso6 
        result = perime_circu(-7)
        self.assertEqual("el perimetro de un circulo no puede ser negativo", result)
        #caso7
        result = perime_circu(4)
        self.assertEqual(25.12, result)

    def test_area_tri(self):
        #caso1
        result=area_tria(2,12)
        self.assertEqual(12,result)
        #caso2
        result = area_tria(2, -12)
        self.assertEqual("base o altura no puede ser negativa", result)
        #caso3
        result = area_tria(3, 3)
        self.assertEqual(4.5, result)
        #caso4
        result = area_tria(-3,-3)
        self.assertEqual("base o altura no puede ser negativa", result)
        #caso5
        result = area_tria(3, 13)
        self.assertEqual(19.5, result)
        #caso6
        result = area_tria(-3, -13)
        self.assertEqual("base o altura no puede ser negativa", result)
        #caso7
        result = area_tria(102, 22)
        self.assertEqual(1122, result)


    def test_perime_tria(self):
        #caso1
        result=perime_tria(2,4,7)
        self.assertEqual(13,result)
        #caso2
        result = perime_tria(-2, 4, 7)
        self.assertEqual(
            "La longitud del lado del triángulo debe ser un número positivo", result)
        #caso3
        result = perime_tria(2, -4, 7)
        self.assertEqual(
            "La longitud del lado del triángulo debe ser un número positivo", result)
        #caso4
        result = perime_tria(2, 4,-7)
        self.assertEqual(
            "La longitud del lado del triángulo debe ser un número positivo", result)
        #caso5
        result = perime_tria(-2, -4, -7)
        self.assertEqual(
            "La longitud del lado del triángulo debe ser un número positivo", result)
        #caso6
        result = perime_tria(12, 10, 7)
        self.assertEqual(
            29, result)
        #caso7
        result = perime_tria(12,22, 14)
        self.assertEqual(48,result)
    
    def test_vol_esfe(self):
        #caso1
        result=vol_esfe(12)
        self.assertEqual(
            7234.56, result)
        #caso2
        result = vol_esfe(-12)
        self.assertEqual(
            'El radio de la esfera no puede ser negativo', result)
        #caso3
        result = vol_esfe(2)
        self.assertEqual(
            33.49333333333333, result)
        #caso4
        result = vol_esfe(-2)
        self.assertEqual(
            'El radio de la esfera no puede ser negativo', result)
        #caso5
        result = vol_esfe(122)
        self.assertEqual(
            7602350.293333334, result)
        #caso6
        result=vol_esfe(-122)
        self.assertEqual(
            'El radio de la esfera no puede ser negativo', result)
        #caso7
        result = vol_esfe(7)
        self.assertEqual(
            1436.0266666666666, result)

if __name__ == '__main__':
    unittest.main()
        
