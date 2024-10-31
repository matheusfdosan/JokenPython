# By Matheus Faustino
import random

def vitoria_maquina_ilustracao():
    print("   _____")
    print("  | ___ |")
    print("  ||   ||  Fácil D+")
    print("  ||___||")
    print("  |   _ |")
    print("  |_____|")
    print(" /_/_|_\\_\\----.")
    print("/_/__|__\\_\\   )")
    print("             (")
    print("             []")

def vitoria_usuario_ilustracao():
    print("        .-\"-.")
    print("       /  - -\\")
    print("       \\  @ @/   Você ganhou!")
    print("        (_ <_) /")
    print("        _)(`")
    print("    ,_(`_))\\")
    print("     \"-\\)__/")
    print("      __|||__")
    print("     ((__|__))")

def empate_ilustracao():
    print("          .  .")
    print("          |\\_|\\")
    print("          | a_a\\   Deu Empate!")
    print("          | | \"]  /")
    print("      ____| '-\\___")
    print("    /.----.___.-'\\")
    print("  //        _    \\")
    print("  //   .-. (~v~) /|")
    print("  |'|  /\\:  .--  / \\")
    print("/ |-/  \\_/____/\\/~|")
    print("/  \\ |  []_|_|_] \\ |")
    print(" \\  | \\ |___   _\\ ]_}")
    print(" |  '-' /   '.'  |")
    print(" |     /    /|:  |")
    print(" |     |   / |:  /\\")
    print(" |     /  /  |  /  \\")
    print(" |    |  /  /  |    \\")
    print(" |    |/\\/  |/|/\\    \\")
    print(" \\|\\ |\\| |  | / /\\/\\__\\")
    print(" \\ \\| | /   | |__")
    print("      / |   |____)")
    print("      |_/")

print("===== Bem-vindo ao Jokenpô! =====")

pontuacao = 0

def escolher_jogada():
    jogada_usuario = int(input("\nFaça a sua jogada:\n1. Pedra 🌑\n2. Papel 📄\n3. Tesoura ✂️\nDigite o número de sua escolha: "))

    return jogada_usuario

def escolher_jogada_maquina(dificuldade, jogada_usuario):
    jogada_maquina = 0
    match dificuldade:
        case 1:
            # Usuario sempre vence
            if jogada_usuario == 1:
                jogada_maquina = 3
            elif jogada_usuario == 2:
                jogada_maquina = 1
            else:
                jogada_maquina = 2
        case 2:
            # Aleatório
            jogada_maquina = random.choice([1,2,3])
        case 3:
            # Máquina sempre vence
            if jogada_usuario == 1:
                jogada_maquina = 2
            elif jogada_usuario == 2:
                jogada_maquina = 3
            else:
                jogada_maquina = 1

    return jogada_maquina

def determinar_vencedor(jogada_usuario, jogada_maquina):
    resultado = ""
    global pontuacao
    match jogada_usuario:
        case 1:
            if jogada_maquina == 1:
                resultado = "\n 🤝 Empate! Jogue denovo para desempatar."
            elif jogada_maquina == 2:
                resultado = "\n😢 Você perdeu! Tente novamente."
                pontuacao -= 1
            else:
                resultado = "\n✨ Você ganhou! 🎉"
                pontuacao += 1
        case 2:
            if jogada_maquina == 1:
                resultado = "\n✨ Você ganhou! 🎉"
                pontuacao += 1
            elif jogada_maquina == 2:
                resultado = "\n 🤝 Empate! Jogue denovo para desempatar."
            else:
                resultado = "\n😢 Você perdeu! Tente novamente."
                pontuacao -= 1
        case 3:
            if jogada_maquina == 1:
                resultado = "\n😢 Você perdeu! Tente novamente."
                pontuacao -= 1
            elif jogada_maquina == 2:
                resultado = "\n✨ Você ganhou! 🎉"
                pontuacao += 1
            else:
                resultado = "\n 🤝 Empate! Jogue denovo para desempatar."
    return resultado

def exibir_resultado(jogada_usuario, jogada_maquina, vencedor):
    print("\nCalculando o resultado...\n")
    print("==============================")
    def nomear_escolha(jogada):
        resposta = ""
        if jogada == 1:
            resposta = "Pedra 🌑"
        elif jogada == 2:
            resposta = "Papel 📄 ️"
        else:
            resposta = "Tesoura ✂️"
        return resposta
    print(f"🧑 Sua escolha: {nomear_escolha(jogada_usuario)}\n🤖 Escolha do computador: {nomear_escolha(jogada_maquina)}")
    print("==============================")
    if vencedor == "\n✨ Você ganhou! 🎉":
        vitoria_usuario_ilustracao()
    elif vencedor == "\n😢 Você perdeu! Tente novamente.":
        vitoria_maquina_ilustracao()
    else:
        empate_ilustracao()
    print(vencedor)

def jogar_jokenpo():
    while True:
        dificuldade = int(input("Escolha a dificuldade:\n[1] Noob🤓\n[2] Justo⚖️\n[3] Roubado😡\nOpção: "))

        if dificuldade < 1 or dificuldade > 3:
            print("Escolha uma das dificuldades acima ⬆")
            continue
        else:
            jogada_usuario = escolher_jogada()

            if jogada_usuario < 1 or jogada_usuario > 3:
                print("Escolha uma das jogadas acima ⬆")
                continue
            else:
                jogada_maquina = escolher_jogada_maquina(dificuldade, jogada_usuario)
                vencedor = determinar_vencedor(jogada_usuario, jogada_maquina)

                exibir_resultado(jogada_usuario, jogada_maquina, vencedor)

                tentar_novamente = int(input("\nDeseja jogar novamente?\n1. Sim\n2. Não\n\nEscolha: "))

                if tentar_novamente == 1:
                    continue
                else:
                    print(f"Sua pontuação foi: {pontuacao} pontos\n")
                    print("\nObrigado por jogar!\nTchau Tchau 👋")
                    break

jogar_jokenpo()

