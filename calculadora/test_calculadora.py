import unittest
from calculadora import adicionar, dividir

class TestCalculadora(unittest.TestCase):
    def test_adicionar(self):
        self.assertEqual(adicionar(2, 3), 5)
        self.assertEqual(adicionar(-1, 1), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            dividir(5, 0)



if __name__ == "__main__":
    unittest.main()