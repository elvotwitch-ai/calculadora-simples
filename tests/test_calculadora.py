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

    def test_raiz_positiva_ignora_segundo_operando(self):
        for radicando, esperado in ((9, 3), (2, 2 ** 0.5), (0.25, 0.5)):
            with self.subTest(radicando=radicando):
                resultado = calculadora.calcular(radicando, object(), "raiz")
                assert isinstance(resultado, float)
                self.assertAlmostEqual(resultado, float(esperado))

    def test_raiz_negativa_gera_value_error(self):
        for radicando in (-1, -0.25):
            with self.subTest(radicando=radicando):
                with self.assertRaisesRegex(ValueError, "radicando negativo"):
                    calculadora.calcular(radicando, None, "raiz")

    def test_raiz_zero(self):
        self.assertEqual(calculadora.calcular(0, None, "raiz"), 0)

    def test_raiz_sem_entrada_saida_nem_mutacao_global(self):
        estado = vars(calculadora).copy()
        with patch("builtins.input", side_effect=AssertionError("entrada indevida")):
            with patch("builtins.print", side_effect=AssertionError("saída indevida")):
                for radicando, esperado in ((9, 3), (0, 0)):
                    with self.subTest(radicando=radicando):
                        self.assertEqual(calculadora.calcular(radicando, None, "raiz"), esperado)
                        self.assertEqual(calculadora.calcular(radicando, None, "raiz"), esperado)
                with self.assertRaises(ValueError):
                    calculadora.calcular(-1, None, "raiz")
        self.assertEqual(vars(calculadora), estado)

    def test_porcentagem_positiva(self):
        self.assertEqual(calculadora.calcular(20, 15, "%"), 3)

    def test_porcentagem_fracionaria(self):
        resultado = calculadora.calcular(12.5, 2.5, "%")
        assert isinstance(resultado, float)
        self.assertAlmostEqual(resultado, 0.3125)

    def test_porcentagem_zero(self):
        for fator_1, fator_2 in ((20, 0), (0, 15), (0, 0)):
            with self.subTest(fator_1=fator_1, fator_2=fator_2):
                self.assertEqual(calculadora.calcular(fator_1, fator_2, "%"), 0)

    def test_porcentagem_negativa(self):
        for fator_1, fator_2, esperado in ((20, -15, -3), (-20, 15, -3), (-20, -15, 3)):
            with self.subTest(fator_1=fator_1, fator_2=fator_2):
                self.assertEqual(calculadora.calcular(fator_1, fator_2, "%"), esperado)

    def test_porcentagem_sem_entrada_saida_nem_mutacao_global(self):
        estado = vars(calculadora).copy()
        with patch("builtins.input", side_effect=AssertionError("entrada indevida")):
            with patch("builtins.print", side_effect=AssertionError("saída indevida")):
                for fator_1, fator_2, esperado in ((20, 15, 3), (20, 0, 0), (20, -15, -3)):
                    with self.subTest(fator_1=fator_1, fator_2=fator_2):
                        self.assertEqual(calculadora.calcular(fator_1, fator_2, "%"), esperado)
                        self.assertEqual(calculadora.calcular(fator_1, fator_2, "%"), esperado)
        self.assertEqual(vars(calculadora), estado)

    def test_simbolo_invalido(self):
        for simbolo in ("", "modulo", "potencia"):
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
                    calculadora.calcular(6, 3, "modulo")
        self.assertEqual(vars(calculadora), estado)


if __name__ == "__main__":
    unittest.main()
