def abrir(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo.')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>1} anos')
    finally:
        a.close()

def lerarquivop(nome):
    try:
        b = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo.')
    else:
        for linha in b:
            dado = linha.split(';')
            for c in dado:
                print(f'{c:<20}', end = '')
    finally:
        b.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq,'at')
    except:
        print('houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()

def linha():
    print(50*'-')

def cabecalho(inp):
    print(50*'-')
    print(f'{inp:^45}')
    print(50 * '-')

def cadastrarp(arq, list):
    try:
        a = open(arq, 'at')
    except:
        print('Hubo un error en la apertura del archivo')
    else:
        try:
            for c in list:
                for e in c.values():
                    a.write(f'{e};')
                a.write('\n')
        except:
            print('Hubo un error al escribir el archivo en la lista')
        else:
            print('Producto cadastrado con suceso')
