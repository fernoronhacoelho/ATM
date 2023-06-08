# Código feito por: Fernanda Noronha
# Versão 4.1   08/06/2023
#Verificar funções de pagamento programado e crédito - verificação das datas
#Fazer as verificações dos inputs de acordo com o padrão desejado! aaaaaaaaa
#Fazer o extrato - exportar um documento json para cada número da conta cadastrado
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

        
        with open(extratosDir) as extratosFile:
            extratosList = json.load(extratosFile)

        extratosController = TransacaoController(extratosList, extratosDir)


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
    print('Olá, gerente')
    MenuGerente()

    operacao = input('Escolha uma operacao: ')

    while operacao != '8':

        if operacao == '1':
            print('Você escolheu cadastrar novo cliente.')
            print('................................................................................')
            nome = ClienteController.cadastrarUsuarioNome()
            while nome == False:
                nome = ClienteController.cadastrarUsuarioNome()
            telefone= ClienteController.cadastrarUsuarioTelefone()
            while telefone == False:
                telefone= ClienteController.cadastrarUsuarioTelefone()
            cpf_cnpj = ClienteController.cadastrarUsuarioCPF_CNPJ()
            while cpf_cnpj == False:
                cpf_cnpj = ClienteController.cadastrarUsuarioCPF_CNPJ()
            endereco = ClienteController.cadastrarUsuarioEndereco()
            noConta = clientesController.cadastrarUsuarioNoConta()
            while noConta == False:
               noConta = clientesController.cadastrarUsuarioNoConta() 
            senha = ClienteController.cadastrarUsuarioSenha()
            while senha ==False:
                senha = ClienteController.cadastrarUsuarioSenha()
            print('................................................................................')
            clientesController.registrarCliente(nome, cpf_cnpj,endereco,telefone,noConta, senha,0)

        elif operacao == '2':
            print('Você escolheu atualizar nome do cliente.')
            noConta=input('Qual é o número da conta do cliente que você gostaria de atualizar o nome?')
            novoNome = input('Qual será o novo nome?')
            clientesController.atualizarUsuarioNome(noConta, novoNome)
            clientesController.updateJson()           
        elif operacao == '3':
            print('Você escolheu atualizar CPF/CNPJ do cliente.')
            noConta=input('Qual o número da conta do cliente que você gostaria de atualizar CPF/CNPJ?')
            novoCPF_CNPJ = input('Qual será o novo CPF/CNPJ?')
            clientesController.atualizarUsuarioCPF_CNPJ(noConta, novoCPF_CNPJ)
            clientesController.updateJson()  
        elif operacao == '4':
            print('Você escolheu atualizar endereço do cliente.')
            noConta=input('Qual o número da conta do cliente que você gostaria de atualizar o endereço?')
            novoEndereco = input('Qual será o novo endereço?')
            clientesController.atualizarUsuarioEndereco(noConta, novoEndereco)
            clientesController.updateJson()  
        elif operacao == '5':
            print('Você escolheu atualizar telefone do cliente.')
            noConta=input('Qual o número da conta do cliente que você gostaria de atualizar o telefone?')
            novoTelefone = input('Qual será o novo telefone?')
            clientesController.atualizarUsuarioTelefone(noConta, novoTelefone)
            clientesController.updateJson()
        elif operacao =='6':
            print('Você escolheu visualizar cliente')
            noConta = input('Qual é o número da conta do usuário que deseja ser visualizado? ')
            clientesController.visualizarUsuario(noConta)
        elif operacao =='7':
            print('Você escolheu excluir cliente')
            noConta = input('Qual é o número da conta que você deseja excluir?')
            clientesController.excluirUsuario(noConta)
            clientesController.updateJson()

        elif operacao == '8':
            break
        else:
            print('Escolha uma opção válida')
        MenuGerente()
        operacao = input('Escolha uma operacao: ')

    print('Sessão encerrada!')    
    clienteLogado = {}
else:
   
    for cliente in clientesList:
        if cliente['senha'] == senha:
            print("Senha correta!")
        elif cliente['senha']!=senha:
            clienteLogado={}
    clienteLogado = clientesController.login(noConta, senha)
   
   
if clienteLogado != {}:
    clientesController.verificarPagamento(clienteLogado)
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
            clientesController.solicitarCredito(clienteLogado,valor,parcelas,data)
            extratosController.registrarTransacao('Credito adquirido',valor,clienteLogado['numeroConta'],0)
            
        elif operacao == '4':
            print('Você escolheu a operação de pagamento programado')
            valor = float(input('Qual valor do seu pagamento programado? \n'))
            pagamento = clientesController.pagamentoProgramado(valor,clienteLogado)
            if pagamento == True:
                extratosController.registrarTransacao('Pagamento Programado',valor,clienteLogado['numeroConta'],0)
            elif pagamento == False:
                pass
        elif operacao == '5':
            print('Você vai emitir extrato')
            extratosController.mostrarExtrato(clienteLogado['numeroConta'])
        elif operacao == '6':
            break
        else:
            print('Escolha uma opção válida')
        Menu()
        operacao = input('Escolha uma operacao: ')

    print('Sessão encerrada!')


# Precisa excluir o extrato do cliente que foi excluido também?