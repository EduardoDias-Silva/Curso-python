



def adicionar(x, y):
    """Soma dois números"""
    return x + y

def subtrair(x, y):
    """Subtrai dois números"""
    return x - y

def multiplicar(x, y):
    """Multiplica dois números"""
    return x * y

def dividir(x, y):
    """Divide dois números, com tratamento para divisão por zero"""
    if y == 0:
        raise ZeroDivisionError( "Erro: Divisão por zero!")
    return x / y

def potencia(x, y):
    """Calcula x elevado a y"""
    return x ** y

def raiz(x):
    """Calcula a raiz quadrada de x"""
    if x < 0:
        raise ValueError("Raiz de número negativo não permitida.")
    return x ** 0.5

OPERACOES = {
    '1': ('Adicionar (+)', adicionar, 2),
    '2': ('Subtrair (-)', subtrair, 2),
    '3': ('Multiplicar (*)', multiplicar, 2),
    '4': ('Dividir (/)', dividir, 2),
    '5': ('Potência (^)', potencia, 2),
    '6': ('Raiz quadrada (√)', raiz, 1),
    '7': ('Sair', None, 0)
}

def obter_numero(mensagem):
    """Solicita um número ao usuário, repetindo até entrada válida"""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def calculadora():
    """Interface principal da calculadora"""
    print("Bem-vindo à Calculadora Melhorada!\n")
    while True:
        print("Selecione a operação:")
        for k, (nome, _, _) in OPERACOES.items():
            print(f"{k}. {nome}")

        escolha = input("Digite sua escolha: ").strip()
        if escolha not in OPERACOES:
            print("Opção inválida. Tente novamente.\n")
            continue

        if escolha == '7':
            print("Calculadora encerrada. Até mais!")
            break

        nome, funcao, qtd_args = OPERACOES[escolha]
        try:
            if qtd_args == 2:
                num1 = obter_numero("Digite o primeiro número: ")
                num2 = obter_numero("Digite o segundo número: ")
                resultado = funcao(num1, num2)
                print(f"Resultado: {nome.split()[0]} de {num1} e {num2} = {resultado}\n")
            elif qtd_args == 1:
                num = obter_numero("Digite o número: ")
                resultado = funcao(num)
                print(f"Resultado: {nome.split()[0]} de {num} = {resultado}\n")
        except ZeroDivisionError as zde:
            print(f"Erro: {zde}\n")
        except ValueError as ve:
            print(f"Erro: {ve}\n")

# Exemplo de teste unitário
def test_adicionar():
    assert adicionar(2, 3) == 5
    assert adicionar(-1, 1) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    try:
        dividir(5, 0)
    except ZeroDivisionError:
        pass
    else:
        assert False, "Deveria lançar ZeroDivisionError"

if __name__ == "__main__":
    calculadora()