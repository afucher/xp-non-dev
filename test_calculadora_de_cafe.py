import unittest
import calculadora_de_cafe

class TestCalculadoraDeCafe(unittest.TestCase):

    def test_deveRetornar0_quandoForPara0Pessoas (self):
        quantidade_de_cafe_esperada = 0
        quantidade_de_pessoas = 0
        quantidade_de_cafe = calculadora_de_cafe.calcula(quantidade_de_pessoas)

        self.assertEqual(quantidade_de_cafe_esperada, quantidade_de_cafe)

    def test_deveRetornar240_quandoForPara1Pessoa (self):
        quantidade_de_cafe_esperada = 240
        quantidade_de_pessoas = 1
        quantidade_de_cafe = calculadora_de_cafe.calcula(quantidade_de_pessoas)

        self.assertEqual(quantidade_de_cafe_esperada, quantidade_de_cafe)

    def test_deveRetornar2400_quandoForPara10Pessoas (self):
        quantidade_de_cafe_esperada = 2400
        quantidade_de_pessoas = 10
        quantidade_de_cafe = calculadora_de_cafe.calcula(quantidade_de_pessoas)

        self.assertEqual(quantidade_de_cafe_esperada, quantidade_de_cafe)

if __name__ == '__main__':
    unittest.main()