import unittest
from unittest.mock import patch

import calculadora


class TestCalculadora(unittest.TestCase):
    def test_soma_sem_entrada_saida(self):
        with patch("builtins.input", side_effect=AssertionError("entrada indevida")):
            with patch("builtins.print", side_effect=AssertionError("saída indevida")):
                self.assertEqual(calculadora.calcular(2, 3, "+"), 5)
                self.assertEqual(calculadora.calcular(-2.5, 1.5, "+"), -1)

    def test_subtracao(self):
        self.assertEqual(calculadora.calcular(7, 3, "-"), 4)
        self.assertEqual(calculadora.calcular(-7, -3, "-"), -4)
        self.assertEqual(calculadora.calcular(1.5, 2, "-"), -0.5)

    def test_multiplicacao(self):
        self.assertEqual(calculadora.calcular(2, 3, "*"), 6)
        self.assertEqual(calculadora.calcular(-2, 3, "*"), -6)
        self.assertEqual(calculadora.calcular(-2, -3, "*"), 6)
        self.assertEqual(calculadora.calcular(0, 3, "*"), 0)
        self.assertEqual(calculadora.calcular(1.5, 2, "*"), 3)

    def test_divisao(self):
        self.assertEqual(calculadora.calcular(6, 3, "/"), 2)
        self.assertEqual(calculadora.calcular(-6, 3, "/"), -2)
        self.assertEqual(calculadora.calcular(-6, -3, "/"), 2)
        self.assertEqual(calculadora.calcular(7, 2, "/"), 3.5)
        self.assertEqual(calculadora.calcular(0, 2, "/"), 0)

    def test_divisao_por_zero_sem_entrada_saida(self):
        with patch("builtins.input", side_effect=AssertionError("entrada indevida")):
            with patch("builtins.print", side_effect=AssertionError("saída indevida")):
                self.assertIsNone(calculadora.calcular(7, 0, "/"))
                self.assertIsNone(calculadora.calcular(0, 0, "/"))

    def test_potencia_sem_entrada_saida_nem_mutacao_global(self):
        estado = vars(calculadora).copy()
        casos = ((2, 3, 8), (5, 0, 1), (2, -3, 0.125), (-2, 3, -8), (9, 0.5, 3))
        with patch("builtins.input", side_effect=AssertionError("entrada indevida")):
            with patch("builtins.print", side_effect=AssertionError("saída indevida")):
                for base, expoente, esperado in casos:
                    with self.subTest(base=base, expoente=expoente):
                        self.assertEqual(calculadora.calcular(base, expoente, "**"), esperado)
        self.assertEqual(vars(calculadora), estado)

    def test_simbolo_invalido(self):
        for simbolo in ("", "%", "potencia"):
            with self.subTest(simbolo=simbolo):
                with self.assertRaisesRegex(ValueError, "Operação inválida"):
                    calculadora.calcular(2, 3, simbolo)

    def test_operacoes_sem_entrada_saida_nem_mutacao_global(self):
        estado = vars(calculadora).copy()
        with patch("builtins.input", side_effect=AssertionError("entrada indevida")):
            with patch("builtins.print", side_effect=AssertionError("saída indevida")):
                for simbolo, esperado in (("+", 9), ("-", 3), ("*", 18), ("/", 2)):
                    with self.subTest(simbolo=simbolo):
                        self.assertEqual(calculadora.calcular(6, 3, simbolo), esperado)
                        self.assertEqual(calculadora.calcular(6, 3, simbolo), esperado)
                self.assertIsNone(calculadora.calcular(6, 0, "/"))
                with self.assertRaises(ValueError):
                    calculadora.calcular(6, 3, "%")
        self.assertEqual(vars(calculadora), estado)


if __name__ == "__main__":
    unittest.main()
