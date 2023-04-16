import sys
import random
import sort

# Constantes

cartoes = [333315, 330000]
NOME_ARQ = 'randomnumbers'
NOME_SAIDA = f'R-{cartoes[0]:08d}-{cartoes[1]:08d}'
MAX_ARQ = 10000000
BYTES_NUM = 4

# Funções

def lerNumero(arq, bytes, pos):
    arq.seek(pos * bytes)
    return int.from_bytes(arq.read(bytes), byteorder='little')

obterAleatorios = False # Obter os números de forma aleatória (True) ou sequencial (False) do arquivo
def obterNumeros(arq, tam):
    ret = []
    for i in range(tam):
        r = random.randint(0, MAX_ARQ) if obterAleatorios else i
        #print(f'r={r}')
        num = lerNumero(arq, BYTES_NUM, r)
        ret.append(num)
    return ret

def escreverLinha(arq, texto):
    arq.write(texto + '\n')

# Mensagens iniciais

print('\n\nComparação de Algoritmos de Classificação\n')
print('Aluno: João Raphael Fontoura Dorneles (333315)')
print('Aluno: Luiz Henrik Oliveira (33xxxx)') # completar
print('Disciplina: INF01124 - Classificação e Pesquisa de Dados\n')

# Abertura do arquivo de dados

try:
    arq = open(f'{NOME_ARQ}.bin', 'rb')
    print(f'O arquivo {NOME_ARQ}.bin foi aberto com sucesso.')
except:
    print(f'Não foi possível abrir o arquivo {NOME_ARQ}.bin, verifique o diretório e tente novamente.')
    sys.exit(0)

# Verificação da integridade do arquivo de dados

ref = [253161, 293217, 84591, 57084, 992328, 1438214, 910653, 106848, 600246, 844451]
correto = True
for i in range(10):
    n = lerNumero(arq, BYTES_NUM, i)
    if n != ref[i]:
        correto = False
        break
    #print(f'{n:07d}')

if correto:
    print('O arquivo foi lido corretamente.')
else:
    print('Não foi possivel ler o arquivo corretamente, verifique o arquivo no diretório e a lista de referência.')
    if (input('Você deseja continuar mesmo assim? (S/N) ').lower() == 'n'):
        print('Interrompendo execução.')
        sys.exit(0)

a0 = obterNumeros(arq, 15) # Array obtido sem ordem específica
a1 = list(a0)
a1.sort() # Array ordenado de forma crescente
a2 = list(a1)
a2.reverse() # Array ordenado de forma decrescente

funcoes = [sort.ISBL, sort.ISBB, sort.SheS, sort.BubS, sort.QukS, sort.SelS, sort.HepS,sort.TimS, sort.MerS]

#print(a0)
#print(a1)
#print(a2)

arq.close()