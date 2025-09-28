



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

def calculadora():
    print("Bem-vindo à Calculadora Melhorada!\n")
    print("Selecione a operação:")
    print("1. Adicionar (+)")
    print("2. Subtrair (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    print("5. Sair")

    while True:
        # Pega a escolha do usuário
        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha == '5':
            print("Calculadora encerrada. Até mais!")
            break

        if escolha in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, digite números.")
                continue

            if escolha == '1':
                print(f"{num1} + {num2} = {adicionar(num1, num2)}\n")

            elif escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}\n")

            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}\n")

            elif escolha == '4':
                resultado = dividir(num1, num2)
                print(f"{num1} / {num2} = {resultado}\n")
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal
if __name__ == "__main__":
    calculadora()