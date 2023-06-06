# Código feito por: Fernanda Noronha
# Versão 3.0  05/06/2023
# Funcao do gerente atualizar o cadastro e apagar cliente
# Organizar os métodos da gerente.
#Verificar erro json, cliente logado e data
#Fazer o extrato
#Fazer o UML

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

        clientesController.registrarCliente(nome, cpf_cnpj,endereco,telefone,noConta, senha,0)
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
            valor = float(input('Qual valor você quer sacar? \n'))
            clientesController.saque(valor,clienteLogado)
            extratosController.registrarTransacao('Saque',valor,clienteLogado['numeroConta'],0)

        elif operacao == '2':
            print('Você escolheu depositar dinheiro.')
            valor = float(input('Qual valor você quer depositar? \n'))
            clientesController.deposito(valor,clienteLogado)
            extratosController.registrarTransacao('Deposito',valor,clienteLogado['numeroConta'],0)
            
        elif operacao == '3':
            print('Você escolheu a operação solicitar crédito')
            valor = float(input('Qual valor você quer solicitar? \n'))
            parcelas=int(input('Quantas parcelas você vai querer?'))
            data=input('Qual dia do mes você vai querer realizar o pagamento das parcelas?')
            clientesController.solicitarCredito(clienteLogado['numeroConta'],valor,parcelas,data)
            extratosController.registrarTransacao('Deposito',valor,clienteLogado['numeroConta'],0)
        elif operacao == '4':
            print('Você eescolheu a operação de pagamento programado')
            valor = float(input('Qual valor você quer depositar? \n'))
            clientesController.pagamentoProgramado(valor,clienteLogado)
            extratosController.registrarTransacao('Deposito',valor,clienteLogado['numeroConta'],0)
        elif operacao == '5':
            print('Você vai emitir extrato')

        elif operacao == '6':
            break
        else:
            print('Escolha uma opção válida')
    
        operacao = input('Escolha uma operacao: ')

print('Sessão encerrada!')


#Arrumar todos os clientes
#instanciar os dois módulos e torcer pra dar certo agora XD