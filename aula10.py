## trabalhando com data, hora

from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %C')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))
    #print(data_atual.strftime('%A - %d/%m/%y'))

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S') ##converte hora para string
    print(horario_str)
    print(type(horario_str))

def trabalhando_com_datetime():
    data_atual = datetime.now() ##data e hora atual
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    ##print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday()) ##trás o dia da semana
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo') ##Criado uma tupla para imprimir dia da semana em português
    print(tupla[data_atual.weekday()])
    data_criada = datetime(1991, 10, 5, 19,00,00)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2022'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    print(data_convertida.weekday())
    print(type(data_convertida))

    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15) ## conta com data
    print(nova_data)

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()