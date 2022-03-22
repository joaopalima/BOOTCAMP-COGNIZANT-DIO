import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#criado objeto de conexão

print("Cliente Socket criado com sucesso!!")

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor, tranquilo?'

try:
    print("Cliente: " + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096) ##recebe do servidor uma resposta de 4096bytes
    dados = dados.decode() ##recebe e vai desempacotar os dados
    print(" Cliente: " + dados)
finally:
    print("Cliente: Fechando a conexão")
    s.close()
