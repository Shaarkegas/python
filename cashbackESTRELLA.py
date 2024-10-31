empresas = ["ALB","MM","CZB"]
cashback = [0.1, 0.08, 0.05]
users = []
saldousers = []
opcoes = [0,1,2,3,4,5,6]

print('SEJA BEM VINDO, O QUE DESEJAS FAZER?')
print('')
print('1 - Cadastrar Empresa')
print('2 - Cadastrar Usuário')
print('3 - Registrar Compra de um Usuário')
print('4 - Mostrar Saldo de um Usuário')
print('5 - Resgatar Saldo de um Usuário')
print('6 - Excluir Empresa')
print('0 - Sair')
print('')

decisao = int(input())

while decisao in opcoes:

    if decisao == 1: #Cadastrar Empresa
        idempresa = input('ID DA EMPRESA: ')
        empresas.append(idempresa)
        valorcash = float(input('VALOR DO CASHBACK DE SUA EMPRESA: '))
        valorcash = valorcash/100
        cashback.append(valorcash)
        print('EMPRESA CADASTRADA COM SUCESSO')

    elif decisao == 2: #Cadastrar Usuário
        print('USUARIOS JA EXISTENTES ',users)
        newuser = input('NOME DO NOVO USUARIO: ')
        users.append(newuser)
        saldousers.append(0)
        print('USUARIO CADASTRADO COM SUCESSO')

    elif decisao == 3: #Registrar Compra de um Usuário
        iuser = 0
        iempresa = 0
        print('USUARIOS CADASTRADOS ',users)
        acessouser = input('NOME DO USUARIO: ')
        if acessouser in users:
            while acessouser != (users[iuser]):
                iuser += 1
            valorcompra = float(input('VALOR DA COMPRA: '))
            print('')
            print('EMPRESAS CADASTRADAS: ',empresas)
            empresacompra = input('EMPRESA ONDE COMPRA FOI EFETUADA: ')

            if empresacompra in empresas:
                while empresacompra != (empresas[iempresa]):
                    iempresa += 1
                cashbackaplicado = (valorcompra) * (cashback[iempresa])
                saldousers[iuser] += cashbackaplicado
                print('SALDO ADICIONADO')
            else:
                print('EMPRESA NAO CADASTRADA, TENTE NOVAMENTE')
        else:
            print('USUARIO INVALIDO, TENTE NOVAMENTE')

    elif decisao == 4: #Mostrar Saldo de um Usuário
        iuser = 0
        print('USUARIOS CADASTRADOS ',users)
        acessouser = input('NOME DO USUARIO: ')
        if acessouser in users:
            while acessouser != (users[iuser]):
                iuser += 1
            print(f'{acessouser}, ATUALMENTE TENS R$ {saldousers[iuser]:.2f}')
        else:
            print('USUARIO INVALIDO, TENTE NOVAMENTE')

    elif decisao == 5: #Resgatar Saldo de um Usuário
        iuser = 0
        print('USUARIOS CADASTRADOS ',users)
        acessouser = input('NOME DO USUARIO: ')
        if acessouser in users:
            while acessouser != (users[iuser]):
                iuser += 1
            print(f'{acessouser}, ATUALMENTE TENS R$ {saldousers[iuser]:.2f}')
            resgate = float(input('QUANTOS REAIS QUER REGATAR? '))
            if resgate <= (saldousers[iuser]):

                yorn = input('DESEJA MESMO RESGATAR SEU SALDO? (S/N)')
                if yorn.lower() == 's':
                    saldousers[iuser] = saldousers[iuser] - resgate
                    print('SALDO TRANSFERIDO COM SUCESSO')
                else:
                    if yorn.lower() == 'n':
                        print('TRANSFERENCIA CANCELADA')
                    else:
                        print('OPÇAO INVALIDA')    
            else:
                print('SALDO INSUFICIENTE')
        else:
            print('USUARIO INVALIDO, TENTE NOVAMENTE')

    elif decisao == 6: #Resgatar Saldo de um Usuário
        iempresa = 0
        print('EMPRESAS CADASTRADAS: ',empresas)
        remover = input('QUE EMPRESA DESEJAS REMOVER DO SISTEMA? ')
        if remover in empresas:
            while remover != empresas[iempresa]:
                iempresa += 1
            SouN = input('DESEJA MESMO EXCLUIR A EMPRESA? (S/N)')
            if SouN.lower() == 's':
                empresas.remove(remover)
                cashback.remove(cashback[iempresa])
                print('EMPRESA EXCLUIDA COM SUCESSO.')

            else:    
                if SouN.lower() == 'n':
                    print('EXCLUSAO CANCELADA.')
        else:
            print('EMPRESA INVALIDA, TENTE NOVAMENTE')    

    if decisao == 0: #SAIR
        print('TENHA UM BOM DIA')
        exit()

    print('')
    print('1 - Cadastrar Empresa')
    print('2 - Cadastrar Usuário')
    print('3 - Registrar Compra de um Usuário')
    print('4 - Mostrar Saldo de um Usuário')
    print('5 - Resgatar Saldo de um Usuário')
    print('6 - Excluir Empresa')
    print('0 - Sair')
    print('')
    decisao = int(input())


print('OPÇAO INVALIDA')