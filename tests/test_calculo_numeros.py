import unittest
from src.exceptions import (
    ingrese_numero,
    NumeroDebeSerPositivo,
)
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='100'
    )
    # Test del ingreso valido debe retornar el numero
    def test_ingreso_valido(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='-100'
    )

    # Test para ingreso de numeros negativos debe retornar una expecion
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='AAA'
    )
    # Test para ingresos no numericos debe retornar una exepcion
    def test_ingreso_no_numerico(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main() 
