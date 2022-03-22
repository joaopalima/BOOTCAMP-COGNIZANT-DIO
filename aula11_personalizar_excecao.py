class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True: ## executa sempre, pois é verdade sempre
    try:
        x = int(input('entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10') ##força uma exceção
        elif x<0:
            raise InputError('Nota não pode ser menor que 0')
        break ## se passar passos anterios com sucesso, vai parar/ tiver erro vai executar exceção
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números: ')
    except InputError as ex:
        print(ex)