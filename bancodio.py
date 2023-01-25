menu = """
 ____                        ____  _       
| __ )  __ _ _ __   ___ ___ |  _ \(_) ___  
|  _ \ / _` | '_ \ / __/ _ \| | | | |/ _ \ 
| |_) | (_| | | | | (_| (_) | |_| | | (_) |
|____/ \__,_|_| |_|\___\___/|____/|_|\___/ 

[1] Depositar [2] Sacar [3] Extrato [0] sair
"""

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITES_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor para o deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Falha! O valor informado não é valido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque :"))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numeros_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Falha! Você está sem saldo.")

        elif excedeu_limite:
            print("Falha! O valor do saque excedeu o limite")

        elif excedeu_saques:
            print("Falha! Número maximo de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numeros_saques += 1
        else:
            print("Falha! O valor informado é invalido.")


    elif opcao == "3":
        print("\n======== EXTRATO ========")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("==========================")
        break

    elif opcao == "0":
        break

    else:
        print("Falha. Por favor selecione novamente a operação desejada.")

