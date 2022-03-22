## "w' = criar arquivo / sobrepor o arquivo
## 'a' = atualizar arquivo se o arquivo já existe // tb gera um arquivo
## 'r' = read == ler arquivo
## def = método

import shutil


def escrever_arquivo(texto): ## método escrever arquivo
    diretorio = 'C:/Users/joaop/Documents/Dev/Git/DIO/Bootcamp_Cognizant/Python/app_python/teste.txt' ##escolhe diretório para criação do arquivo
    arquivo = open(diretorio, 'a')
    arquivo.write(texto) ##reescreve uma nova linha
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):  ## Método atualizar
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquvo): ## método ler arquivo
    arquivo = open(nome_arquvo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print((aluno_nota))
    aluno_nota = aluno_nota.split('\n') ## split transforma em lista // toda vez que encontrar "\n" vai virar intem da lista
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        #print(x)
        lista_notas = x.split(',') ## pega o nome dos alunos na lista na posição 0
        aluno = lista_notas[0]
        lista_notas.pop(0) ##retira primeiro dado da lista
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) /4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/joaop/Documents/Dev/Git/DIO/Bootcamp_Cognizant/')
#copia e move para o caminho abaixo
def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/joaop/Documents/Dev/Git/DIO/Bootcamp_Cognizant/Python')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    #copia_arquivo(('notas.txt'))
    #lista_media = media_notas('notas.txt')
    #print(lista_media)
    #media_notas('notas.txt')
    #escrever_arquivo(('Primeira linha.\n')) ##chamada do método escrever_arquivo
    #aluno = 'Pichu, 7,9,3,8\n'
    #atualizar_arquivo('notas.txt', aluno) ##chamada do método atualiza_arquivo
    #ler_arquivo('teste.txt') ##chamada do método ler_arquivo
