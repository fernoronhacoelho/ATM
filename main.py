from Views.menu import *
from Controllers.transacaoController import TransacaoController
from Controllers.clienteController import ClienteController
import json

if __name__ == "__main__":
        
        clientesDir = 'database\\clientes.json'
        extratosDir = 'database\extratos.json'

        with open(clientesDir) as clientesFile:
            clientesList = json.load(clientesFile)

        clientesController = ClienteController(clientesList, clientesDir)

        for cliente in clientesList:
            print(f'{cliente} \n')
        
        with open(extratosDir) as extratosFile:
            extratosList = json.load(extratosFile)

        extratosController = TransacaoController(extratosList, extratosDir)

        for transacao in extratosList:
            print(f'{cliente} \n')

Login()
noConta = input('Digite o número da sua conta: \n')
if noConta == '0000': 
    print('Você está entrando na seção de gerência\n')
else:
    for cliente in clientesList:
        if cliente['numeroConta'] == noConta:
            print('Cliente cadastrado\n')
LoginSenha()
senha = input('Digite a sua senha: \n')
if senha == 'gerente':
        
        print('................................................................................')
        nome = input('Insira o nome do cliente: \n')
        telefone= input('Insira o telefone do cliente com o ddd no formato (xx) xxxxx-xxxx: \n')
        cpf_cnpj = input('Insira o CPF ou CNPJ (Sem caracteres especiais): \n')
        endereco = input('Insira o endereço do cliente: \n')
        noConta = input('Insira o número da conta: \n')
        senha = input('Insira sua senha de 6 dígitos: \n')
        print('................................................................................')

        clientesController.registrarCliente(nome, cpf_cnpj,endereco,telefone,noConta, senha)
        clienteLogado = {}
else:
   
    for cliente in clientesList:
        if cliente['senha'] == senha:
            print("Senha correta!")
        elif cliente['senha']!=senha:
             clienteLogado={}
    clienteLogado = clientesController.login(noConta, senha)
   
   
if clienteLogado != {}:
    print('Olá,')
    print(clienteLogado['nome'])
    Menu()

    operacao = input('Escolha uma operacao: ')

    while operacao != '6':

        if operacao == '1':
            print('Você escolheu sacar dinheiro.')
            valor = input('Qual valor você quer depositar? \n')
            TransacaoController.registrarTransacaoDeposito(clienteLogado['numeroConta'], valor)

        elif operacao == '2':
            print('Você escolheu depositar dinheiro.')

        elif operacao == '3':
            print('Você está solicitando crédito')

        elif operacao == '4':
            print('Você está realizando um pagamento programado')

        elif operacao == '5':
            print('Você vai emitir extrato')

        elif operacao == '6':
            break
        else:
            print('Escolha uma opção válida')
    
        operacao = input('Escolha uma operacao: ')

print('Sessão encerrada!')