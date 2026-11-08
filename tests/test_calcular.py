import contextlib
import importlib
import io
import unittest
from unittest.mock import patch

import main


class TestCalcular(unittest.TestCase):
    def test_soma_positivos(self):
        self.assertEqual(main.calcular(2, 3, "+"), 5)

    def test_soma_negativos(self):
        self.assertEqual(main.calcular(-2, -3, "+"), -5)

    def test_subtracao_positivos(self):
        self.assertEqual(main.calcular(7, 3, "-"), 4)

    def test_subtracao_negativos(self):
        self.assertEqual(main.calcular(-7, -3, "-"), -4)

    def test_multiplicacao_positivos(self):
        self.assertEqual(main.calcular(2, 3, "*"), 6)

    def test_multiplicacao_negativos(self):
        self.assertEqual(main.calcular(-2, -3, "*"), 6)
        self.assertEqual(main.calcular(-2, 3, "*"), -6)

    def test_divisao_positivos(self):
        self.assertEqual(main.calcular(6, 3, "/"), 2)

    def test_divisao_negativos(self):
        self.assertEqual(main.calcular(-6, -3, "/"), 2)
        self.assertEqual(main.calcular(-6, 3, "/"), -2)

    def test_divisao_fracionaria(self):
        self.assertEqual(main.calcular(7, 2, "/"), 3.5)

    def test_divisao_por_zero(self):
        with contextlib.redirect_stdout(io.StringIO()) as saida:
            self.assertIsNone(main.calcular(7, 0, "/"))
        self.assertEqual(saida.getvalue(), "nao é possivel dividir por 0\n")


class TestColetarDados(unittest.TestCase):
    def test_entrada_valida(self):
        with patch("builtins.input", side_effect=["2", "3", "+"]):
            self.assertEqual(main.coletar_dados(None), (2, 3, "+"))

    def test_entrada_invalida_seguida_de_valida(self):
        with patch("builtins.input", side_effect=["a", "3", "+", "2", "3", "+"]):
            with contextlib.redirect_stdout(io.StringIO()) as saida:
                self.assertEqual(main.coletar_dados(None), (2, 3, "+"))
        self.assertEqual(saida.getvalue(), "insira numeros inteiros\n")

    def test_uso_do_ultimo_resultado(self):
        with patch("builtins.input", side_effect=["s", "3", "+"]):
            with contextlib.redirect_stdout(io.StringIO()) as saida:
                self.assertEqual(main.coletar_dados(3.5), (3.5, 3, "+"))
        self.assertEqual(saida.getvalue(), "ultimo resultado: 3.5\n")


class TestImportacao(unittest.TestCase):
    def test_importacao_nao_abre_laco_interativo(self):
        with patch("builtins.input", side_effect=AssertionError("input na importação")):
            with contextlib.redirect_stdout(io.StringIO()) as saida:
                importlib.reload(main)
        self.assertEqual(saida.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
