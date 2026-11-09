"""Operações puras, independentes da interface de terminal."""


def calcular(fator_1, fator_2, simbolo):
    """Calcula dois operandos numéricos sem entrada/saída nem estado global.

    Aceita +, -, *, /, ** e raiz. Divisão por zero retorna None, como na
    interface existente, mas sem imprimir mensagem. Símbolo inválido gera
    ValueError. Para raiz quadrada, usa fator_1 e ignora fator_2; radicando
    negativo gera ValueError, sem produzir resultado complexo.
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
    if simbolo == "**":
        return fator_1 ** fator_2
    if simbolo == "raiz":
        if fator_1 < 0:
            raise ValueError("Raiz quadrada não aceita radicando negativo.")
        return fator_1 ** 0.5
    raise ValueError("Operação inválida: use +, -, *, /, ** ou raiz.")
