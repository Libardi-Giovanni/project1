def exibir_preco(nome_produto, preco):
    print(f'{nome_produto} está no valor de: R${preco}')

# Argumentos posicionais
exibir_preco('Iphone', 5000)

# Argumentos nomeados
exibir_preco(nome_produto='Iphone', preco=5000)


def gerar_objeto_personalizado(cor,*, altura, formato):
    print(cor, altura, formato)

gerar_objeto_personalizado('azul', altura=2.10, formato='redondo')


def somar(*valores, b):
    print(valores)
    for valor in valores:
        b += valor
    print(b)

somar(10, 20, 5, b=5)
# *args

# **kwargs (Keyword arguments)
def concatenar(**palavras):
    frase = ' '
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)

concatenar(a='Nós', b='Somos', c='Pythonistas', d='profissionais')

def fazer_calculo(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)

fazer_calculo('Jeff',4,6,3,7,a=1,b=2,c=5)
