## tratamento de erro com try: except:

lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1 ## dando erro aqui não excuta nada pra baixo
    numero = lista[1]
#    x = a
#    print('fechando arquivo')
#    arquivo.close()

except ZeroDivisionError:
    print('Não é possível fazer divisão por zero')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritimética')
except IndexError:
    print('Erro ao acessar um índice inválido da lista')
except BaseException as ex:
    print('Erro desconhecido. Erro: {}' .format(ex))
else: ## só excuta se não tiver nenhum erro no bloco anterior
    print('Executa quando não ocorre exceção')
finally: ## executa dando ou erro ou não
    print('Sempre executa')
    print('fechando arquivo')
    arquivo.close()

