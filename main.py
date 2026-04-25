def coletar_dados(ultimo_resultado):
    while True:
        usando_memoria = False

        if ultimo_resultado is not None:
            print(f"ultimo resultado: {ultimo_resultado}")
            resposta = input("usar ultimo resultado como primeiro fator? (s/n): ").strip().lower()

            if resposta == "s":
                fator_1 = ultimo_resultado
                fator_1_texto = None
                usando_memoria = True
            else:
                fator_1_texto = input("insira um numero: ").strip()
        else:
            fator_1_texto = input("insira um numero: ").strip()

        fator_2_texto = input("insira outro numero: ").strip()
        simbolo = input("insira uma operação: ").strip()

        if not usando_memoria and fator_1_texto == "":
            print("insira um numero inteiro válido ou simbolo operacional válido")
            continue
        if fator_2_texto == "" or simbolo == "":
            print("insira um numero inteiro válido ou simbolo operacional válido")
            continue

        try:
            if not usando_memoria and fator_1_texto:
                fator_1 = int(fator_1_texto)

            fator_2 = int(fator_2_texto)
        except ValueError:
            print("insira numeros inteiros")
            continue

        if simbolo not in ["+", "-", "*", "/"]:
            print("Insira um dos 4 simbolos matemáticos: +, -, *, /")
            continue

        return fator_1, fator_2, simbolo

def calcular(fator_1, fator_2, simbolo):
    
    if simbolo == "+":
        resultado = fator_1 + fator_2

    elif simbolo == "-":
        resultado = fator_1 - fator_2

    elif simbolo == "*":
        resultado = fator_1 * fator_2
    
    elif simbolo == "/":
        if fator_2 == 0:
            print("nao é possivel dividir por 0")
            return None
    
        resultado = fator_1 / fator_2

    return resultado

ultimo_resultado = None

while True:
    fator_1, fator_2, simbolo = coletar_dados(ultimo_resultado)
    resultado = calcular(fator_1, fator_2, simbolo)

    if resultado is None:
        continue
    print(f"resultado: {resultado}")
    ultimo_resultado = resultado

    continuar = input("continuar calculando? (s/n) ou reset(r): ").strip().lower()
    if continuar == "r":
        ultimo_resultado = None
        print("memoria resetada")
        continue
    if continuar != "s":
        break