class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1


    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

print(__name__)
if __name__ == '__main__': ## usado para fazer teste dentro do console // executa essa parte do codigo
    televisao = Televisao()
    televisao.power()
    print('televisão está ligada: {}' .format(televisao.ligada)) ## apertou "botão" ligar -- Televisão ligada
    televisao.power()
    print('televisão está ligada: {}' .format(televisao.ligada)) ## apertou "botão" de novo -- Televisão desligada
    print('Canal: {}'.format(televisao.canal)) ## imprime canal instanciado -- canal 5
    televisao.power() ## apertou "botão" ligar -- Televisão ligada
    print('televisão está ligada: {}' .format(televisao.ligada))
    print('televisão está ligada: {}' .format(televisao.ligada)) ## instanciou classe televisão -- Televisão desligada
    televisao.aumenta_canal() ## aumenta para canal 6
    televisao.aumenta_canal() ## aumenta para canal 7
    print('Canal: {}'.format(televisao.canal)) ##imprime canal 7
    televisao.diminui_canal() ## aumenta para canal 6
    print('Canal: {}'.format(televisao.canal)) ##imprime canal 6
