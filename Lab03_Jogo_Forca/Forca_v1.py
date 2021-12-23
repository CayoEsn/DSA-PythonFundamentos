# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# Classe


class Hangman:

    # # Método Construtor
    def __init__(self, word):
        self.word = word
        self.letters = []
        self.countlettersRight = 0
        self.countlettersWrong = 0

    # # Método para adivinhar a letra
    def guess(self, letter):
        if (letter in self.word):
            self.letters.append(letter)
            self.countlettersRight += 1
        else:
            self.countlettersWrong += 1

    # # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.countlettersWrong >= 6

    # # Método para verificar se o jogador venceu
    def hangman_won(self):
        return self.hide_word() == self.word

    # # Método para não mostrar a letra no board
    def hide_word(self):
        return ''.join([(letter if letter in self.letters else "_") for letter in self.word])

    # # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        return board[self.countlettersWrong]


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("./Lab03_Jogo_Forca/palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank) - 1)].strip()

# Função Main - Execução do Programa


def main():

    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while (not(game.hangman_over()) and not(game.hangman_won())):
        print(game.print_game_status())
        print("\n")
        print("Palavra: " + game.hide_word())
        print("\n")
        print("Letras erradas: " + str(game.countlettersWrong))
        print("\n")
        print("Letras corretas: " + str(game.countlettersRight))
        print("\n")
        letter = input("Digite uma letra: ")

        game.guess(letter)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')


# Executa o programa
if __name__ == "__main__":
    main()
