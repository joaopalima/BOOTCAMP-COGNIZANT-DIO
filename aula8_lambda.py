## labda é uma função anônima

# def contador_letras(lista_palavras):
#     contador = []
#     for x in lista_palavras:
#         quantidade = len(x)
#         contador.append(quantidade)
#     return contador

##codigo abaixo equivale ao codigo a cima, de forma mais simples
contador_letras = lambda lista: [len(x) for x in lista] ##lambda é eficiente para funções em uma única linha /// "len" = quantidade de letras em "x"

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5, 10))
print(subtracao(10,5))

calculadora = { ## dicionário
    'soma': lambda a,b: a+b,
    'subtracao': lambda a,b: a-b,
    'multiplicacao': lambda a,b: a*b,
    'divisao': lambda  a,b: a/b,
}

print(type(calculadora))
soma = calculadora['soma'] # soma = lambda a,b: a+b
multiplcacao = calculadora['multiplicacao']
print('A soma é: {}'.format(soma(10,5)))
print('A multiplicação é: {}'.format(multiplcacao(10,2)))
