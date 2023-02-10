import os
from time import sleep
from random import randint

def menu():
    os.system("cls")
    print("=-"*15)
    print('JOGO DA ADIVINHAÇÃO')
    print("=-"*15)
    print("Selecione a opção desejada:")
    print("=-"*15)
    print("1 * JOGAR")
    print("2 * SAIR")
    print("=-"*15)
    while True:
        op = input("O que deseja fazer? ").strip()[0].upper()
        if op == "2" or op == "S":
            os.system("cls")
            print("ENCERRANDO...")
            sleep(1)
            os.system("cls")
            exit()
        elif op == "1" or op == "J":
            os.system("cls")
            sleep(1)
            break
        else:
            print("OPÇÃO INVALIDA. DIGITE 1 OU 2.")


def jogar():
    cont = 0
    com = randint(0, 10)
    print("Óla, eu sou seu Computador e pensei em um número entre 0 e 10.\nSerá que você consegue acertar?\n")
    while True:
        try:
            cont +=1
            num = int(input("Qual seu palpite? "))
            if num == com:
                if cont == 1:
                    print(f"UAU. Você é INCRíVEL!!! Acertou em {cont} tentativa. O número pensado foi {com}.")
                else:
                    print(f"\nPARABENS!!! Você acertou em {cont} tentativas o número pensado foi {com}.")
                cont = 0
                com = randint(0, 10)
                while True:
                    con = input("\nDeseja jogar novamente? S/N: ").strip()[0].upper()
                    if con == "S":
                        sleep(0.5)
                        os.system("cls")
                        sleep(0.5)
                        return jogar()    
                    elif con == "N":
                        os.system("cls")
                        print("ENCERRANDO...")
                        sleep(1)
                        os.system("cls")
                        exit()
                    else:
                        print("OPÇÃO INVALIDA")
            elif num > com:
                print("Você errou. Tente um numero menor!")
            elif num < com:
                print("Você errou. Tente um numero maior!")
        except ValueError:
            cont -= 1
            print("OPÇÃO INVALIDA!")


while True:
    menu()
    jogar()
