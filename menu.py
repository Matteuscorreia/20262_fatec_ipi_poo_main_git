import calculadora 

def menu():
    while True:
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            a = float(input("Digite o primeiro numero: "))
            b = float(input("Digite o segundo numero: "))
            print(f"Resultado: {calculadora.somar(a, b)}")

        elif opcao == "2":
            a = float(input("Digite o primeiro numero: "))
            b = float(input("Digite o segundo numero: "))
            print(f"Resultado: {calculadora.subtrair(a, b)}")

        elif opcao == "3":
            a = float(input("Digite o primeiro numero: "))
            b = float(input("Digite o segundo numero: "))
            print(f"Resultado: {calculadora.multiplicar(a, b)}")

        elif opcao == "4":
            a = float(input("Digite o primeiro numero: "))
            b = float(input("Digite o segundo numero: "))
            print(f"Resultado: {calculadora.dividir(a, b)}")