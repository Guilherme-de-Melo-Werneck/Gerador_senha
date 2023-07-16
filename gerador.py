import random #fornece funções relacionadas à geração de números aleatórios
import string #fornece várias constantes úteis com caracteres

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation # Define os caracteres que serão usados na senha
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))# Gera a senha utilizando compreensão de lista e a função random.choice()
    return senha # Retorna a senha gerada

def senha1():
    tamanho = int(input("Digite o tamanho da senha desejada: ")) # Solicita ao usuário o tamanho da senha desejada
    senha = gerar_senha(tamanho) # Chama a função gerar_senha para obter a senha gerada
    print("Senha gerada:", senha) # Exibe a senha gerada na tela

if __name__ == '__main__':
    senha1() # Chama a função senha1 para executar o programa