# gerar senha aleatóra

import random, string

#tamanho = 16  #tamanho da senha - 16 caracteres
tamanho = int(input('digite o tamanho de senha que você deseja: '))

chars = string.ascii_letters + string.digits + '!@#$%¨&*()-=+,.;:/?'

rnd = random.SystemRandom() #os.urandom --> gera número aleatórios a parir de fonte do sistema operacional

print('' .join(rnd.choice(chars) for i in  range(tamanho)))