# Código feito por: Fernanda Noronha
# Versão 6.0   15/06/2023

from Views.menu import *
from Controllers.transacaoController import TransacaoController
from Controllers.clienteController import ClienteController
from Controllers.verificacaoController import *
import json

if __name__ == "__main__":
        
        clientesDir = 'database\\clientes.json'
        extratosDir = 'database\\extratos.json'
        creditosDir = 'database\\creditos.json'
        pagamentosDir = 'database\\pagamentos.json'        

        with open(creditosDir) as creditosFile:
            creditosList = json.load(creditosFile)
        
        with open(pagamentosDir) as pagamentosFile:
            pagamentosList = json.load(pagamentosFile)        

        with open(clientesDir) as clientesFile:
            clientesList = json.load(clientesFile)

        with open(extratosDir) as extratosFile:
            extratosList = json.load(extratosFile)
        clientesController = ClienteController(clientesList, clientesDir)
        verificacaoController = VerificaoController(pagamentosList, pagamentosDir, creditosList, creditosDir)
        extratosController = TransacaoController(extratosList, extratosDir)


Login()
noConta = input('Digite o número da sua conta: \n')
if noConta == '0000': 
    print('Você está entrando na seção de gerência\n')
else:
    for cliente in clientesList:
        if cliente['numeroConta'] == noConta:
            print('Cliente cadastrado\n')
        else:
            clienteLogado={}
LoginSenha()
senha = input('Digite a sua senha: \n')
if noConta == '0000' and senha == 'gerente':
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
    exit()

elif noConta=='0000' and senha !='gerente':
    print('Senha da gerência incorreta. Acesso negado!') 
    clienteLogado = {}
else:
    for cliente in clientesList:
        if cliente['numeroConta'] ==noConta and cliente['senha'] == senha:
            print("Senha correta!")
            clienteLogado = clientesController.login(noConta, senha)
            break
        elif cliente['numeroConta'] == noConta and cliente['senha']!=senha:
            clienteLogado={}
    
   
if clienteLogado =={}:
    print("Usuário/senha incorretos. Por favor, rode o programa novamente para acessar sua conta.")
elif clienteLogado != {}:
    PagamentoRealizado = verificacaoController.verificarPagamento(clienteLogado)
    ParcelaCreditoPaga = verificacaoController.verificarPagamentoCredito(clienteLogado)
    
    print('Olá,')
    print(clienteLogado['nome'])
    if PagamentoRealizado != False:
        extratosController.registrarTransacao('Pagamento Programado',str(PagamentoRealizado),clienteLogado['numeroConta'],0)
        clientesController.updateJson()
        verificacaoController.excluirPagamento(clienteLogado['numeroConta'])
        verificacaoController.updateJsonPagamento()
    if ParcelaCreditoPaga != False:
        extratosController.registrarTransacao('Parcela do Credito',str(ParcelaCreditoPaga),clienteLogado['numeroConta'],0)
        clientesController.updateJson()
        verificacaoController.excluirCredito(clienteLogado['numeroConta'])
        verificacaoController.updateJsonCreditos()

        
    Menu()

    operacao = input('Escolha uma operacao: ')

    while operacao != '6':

        if operacao == '1':
            print('Você escolheu sacar dinheiro.')
            valor = input('Qual valor você quer sacar? \n')
            verificacao = str.isnumeric(valor)
            if verificacao==True:
                clientesController.saque(float(valor),clienteLogado)
                extratosController.registrarTransacao('Saque',valor,clienteLogado['numeroConta'],0)
            elif verificacao == False: 
                print('Escolha um valor numérico e tente realizar a operação novamente.')
                    

        elif operacao == '2':
            print('Você escolheu depositar dinheiro.')
            valor = input('Qual valor você quer depositar? \n')
            verificacao = str.isnumeric(valor)
            if verificacao==True:
                clientesController.deposito(float(valor),clienteLogado)
                extratosController.registrarTransacao('Deposito',valor,clienteLogado['numeroConta'],0)
            elif verificacao == False: 
                print('Escolha um valor numérico e tente realizar a operação novamente.')
            
        elif operacao == '3':
            print('Você escolheu a operação solicitar crédito')
            valor = input('Qual valor você quer solicitar? \n')
            parcelas=input('Quantas parcelas você vai querer?')
            data=str(input('Qual dia do mês você vai querer realizar o pagamento das parcelas? [dd]'))
            verificacao = str.isnumeric(valor)
            verificacaoParcela = str.isnumeric(parcelas)
            verificacaoDia = str.isnumeric(data)
            if verificacao == True and verificacaoParcela == True and verificacaoDia ==True:
                while len(data) !=2 or int(data)>31:
                    print('Digite a data com dois algorismos significativos, caso tenha só uma unidade, coloque o zero na frente.\n')
                    data=str(input('Qual dia do mês você vai querer realizar o pagamento das parcelas? [dd]'))
               
                clientesController.solicitarCredito(clienteLogado,float(valor),int(parcelas),data)
                extratosController.registrarTransacao('Credito adquirido',valor,clienteLogado['numeroConta'],0)
            elif verificacao == False or verificacaoParcela == False:
                print("Por favor, tente realizar a operação novamente e adicione valores válidos de quantidade de parcelas e/ou valor.\n")
                
            
        elif operacao == '4':
            print('Você escolheu a operação de pagamento programado')
            valor = input('Qual valor do seu pagamento programado? \n')
            verificacao=str.isnumeric(valor)
            if verificacao == True:
                pagamento = clientesController.pagamentoProgramado(float(valor),clienteLogado)
                if pagamento == True:
                    extratosController.registrarTransacao('Pagamento Programado',valor,clienteLogado['numeroConta'],0)
                    
            elif verificacao == False:
                print('Escolha um valor numérico e tente realizar a operação novamente.')
                
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

