
def menu():
    menu = """\n

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [nu] Novo usuário
    [lc] Informações da conta
    [q] Sair

    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += (f"Depósito: R$ {valor:.2f}\n")
        print('Depósito realizado com sucesso!')
    else: 
        print("Falha na operação. Informe um valor válido")
    return saldo, extrato

def sacar (*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    excedeu_limite = valor > limite
    if valor > saldo:
        print ('Operação Falhou. Saldo insuficiente')
    elif excedeu_limite:
        print ('Operação falhou. Valor do saque superior ao limite')
    elif numero_saques >= limite_saques:
        print ('Falhou. Número limite de saques diários excedido')
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Falha na operação. Valor informado é inválido")
    return saldo, extrato

def exibir_extrato (saldo, /, *, extrato):
    print("\n********** EXTRATO **********")
    print("Sem movimentações no extrato" if not extrato else extrato)
    print(f"\nSaldo Final: {saldo:.2f}")
    print("*******************************")

def criar_usuario (usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario: 
        print("\nJá existe usuário cadastrado com o CPF informado")
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd/mm/aaaa):')
    endereco = input('Informe seu endereço completo (formato: logradouro, número - bairro - cidado/sigla estado)')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf cadastrado do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado, verifique o cadastro")

def lista_contas(contas):
    for conta in contas:
        resultado = f'''\
        Agência: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        '''
        print('*'* 20)
        print(resultado)

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    numero_conta = 1
    agencia = '0001'

    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Digite o valor do depósito"))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            saque = float(input("Digite o valor desejado para o saque"))
            saldo, extrato = sacar(saldo=saldo, 
            valor=valor,
            extrato=extrato, 
            limite=limite, 
            numero_saques=numero_saques, 
            limite_saques=limite_saques)
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "nc":
            conta = criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1
        elif opcao == "lc":
            lista_contas(contas)
        elif opcao == "q":
            break
        else:
            print('Operação inválida, por favor selecione novamente')
main()