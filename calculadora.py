"""Operações puras, independentes da interface de terminal."""


def calcular(fator_1, fator_2, simbolo):
    """Calcula dois operandos numéricos sem entrada/saída nem estado global.

    Aceita +, -, * e /. Divisão por zero retorna None, como na interface
    existente, mas sem imprimir mensagem. Símbolo inválido gera ValueError.
    """
    if simbolo == "+":
        return fator_1 + fator_2
    if simbolo == "-":
        return fator_1 - fator_2
    if simbolo == "*":
        return fator_1 * fator_2
    if simbolo == "/":
        if fator_2 == 0:
            return None
        return fator_1 / fator_2
    raise ValueError("Operação inválida: use +, -, * ou /.")
