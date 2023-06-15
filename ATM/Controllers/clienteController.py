import json
from Models.models import Cliente, Pagamento, Credito
from datetime import date, timedelta
from Controllers.verificacaoController import *

creditosDir = 'database\\creditos.json'
pagamentosDir = 'database\\pagamentos.json'        

with open(creditosDir) as creditosFile:
    creditosList = json.load(creditosFile)
        
with open(pagamentosDir) as pagamentosFile:
        pagamentosList = json.load(pagamentosFile)

verificacaoController = VerificaoController(pagamentosList, pagamentosDir, creditosList, creditosDir)

class ClienteController():
    def __init__(self, clienteList, clientesDir):
        self.clientesList = clienteList
        self.clientesDir = clientesDir
        self.pagamentos= []
        self.creditos= []
    
    def updateJson(self):
        with open(self.clientesDir, 'w') as updateFile:
            json.dump(self.clientesList, updateFile, indent=4)
        

    def registrarCliente (self, nome, cpf_cnpj, endereco, telefone, numeroConta, senha, saldo):
        novoCliente = Cliente(nome, cpf_cnpj, endereco, telefone, numeroConta, senha, saldo)
        converteCliente = vars(novoCliente)
        self.clientesList.append(converteCliente)
        self.updateJson()

        clienteTransacoes = open(f"database\\Transacoes\\extratos_{numeroConta}.json","x")
        clienteTransacoes.write("[]")
        clienteTransacoes.close()

    def registrarPagamento(self, novoPagamento):    
        pagamento = novoPagamento
        self.pagamentos.append(pagamento)
        with open(self.pagamentosDir, 'w') as updateFile:
            json.dump(self.pagamentos, updateFile, indent=4)
    def registrarCredito(self, novoCredito):
        credito = novoCredito
        self.creditos.append(novoCredito)
        with open(self.creditosDir, 'w') as updateFile:
            json.dump(self.creditos, updateFile, indent=4)
        

    def cadastrarUsuarioNoConta(self):
        noConta = str(input('Insira o número da conta: \n'))
        for cliente in self.clientesList:
            if cliente['numeroConta'] == noConta:
                print('Por favor escolha outro número de conta contendo 4 dígitos.\n')
                noexiste = False
                return False
                break
            else:
                noexiste = True
                
        if len(noConta) !=4 and noexiste==True:
            print('Por favor escolha uma nova conta de 4 dígitos.\n')
            return False
        elif len(noConta) ==4 and noexiste ==True: 
            return noConta
        
        
        
    def cadastrarUsuarioNome():  
        nome= input('Insira o nome do cliente: \n')
        return nome
    
    def atualizarUsuarioNome(self,noConta, novoNome):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == noConta:
                cliente['nome'] = novoNome

    def cadastrarUsuarioTelefone():  
        telefone= input('Insira o telefone do cliente com o ddd no formato (xx)xxxxx-xxxx: \n')
        if len(telefone) == 13 or len(telefone) ==14:
            return telefone
        else:
            print('Digite um telefone válido, lembre-se do formato solicitado!\n')
            return False
    
    def atualizarUsuarioTelefone(self,noConta, novoTelefone):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == noConta:
                if len(novoTelefone) == 13 or len(novoTelefone) ==14:
                    cliente['telefone'] = novoTelefone
        else:
            print('Digite um telefone válido, lembre-se do formato solicitado!\n')
            return False
                
    def cadastrarUsuarioCPF_CNPJ():  
        cpf_cnpj = input('Insira o CPF ou CNPJ (Sem caracteres especiais): \n')
        verificarcpf = str.isnumeric(cpf_cnpj)
        if verificarcpf == True:
            if len(cpf_cnpj) == 11 or len(cpf_cnpj) == 14:
                return cpf_cnpj
            else:
                print('Digite um CPF/CNPJ válido, lembre-se do formato solicitado!\n')
                return False
        else:
             while verificarcpf == False:
                print("CPF/CNPJ em formato inválido.")
                cpf_cnpj = input('Insira o CPF ou CNPJ (Sem caracteres especiais): \n')
                verificarcpf = str.isnumeric(cpf_cnpj) 
                if verificarcpf == True:
                    return cpf_cnpj
                    break
                else:
                    return False  
    def atualizarUsuarioCPF_CNPJ(self,noConta, novoCPF_CNPJ):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == noConta:
                if len(novoCPF_CNPJ) == 11 or len(novoCPF_CNPJ) == 14:
                    verificarCPF_CNPJ = str.isnumeric(novoCPF_CNPJ)
                    if verificarCPF_CNPJ == True:
                        cliente['cpf_cnpj'] = novoCPF_CNPJ
                    else:
                            print("CPF/CNPJ em formato inválido. Escolha a operação novamente e digite um valor numérico.")
                else:
                    print('Digite um CPF/CNPJ válido, lembre-se do formato solicitado!\n')
                    return False

    def cadastrarUsuarioEndereco():  
        endereco = input('Insira o endereço do cliente: \n')
        return endereco
    
    def atualizarUsuarioEndereco(self,noConta, novoEndereco):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == noConta:
                cliente['endereco'] = novoEndereco
   
    def cadastrarUsuarioSenha():  
        senha = str(input('Insira sua senha de 6 dígitos: \n'))
        verificarSenha = str.isnumeric(senha)
        if len(senha) == 6 and verificarSenha == True:
            return senha
        else:
            print('A senha está incorreta. Ela deve conter 6 dígitos e ser numérica.\n')
            return False

    def visualizarUsuario(self, noConta):
        for cliente in self.clientesList: 
            if cliente['numeroConta'] == noConta:
                print(f'{cliente} \n')
    
    def excluirUsuario(self, noConta):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == noConta:
                if cliente['saldo'] == 0:
                    self.clientesList.remove(cliente)
                else:
                    print('Para excluir o cliente o saldo da conta deverá ser igual a 0.')

    def login(self, noConta, senha):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == noConta and cliente['senha'] == senha:
                return cliente
    
    def deposito(self, valor, clienteLogado):
        if type(valor) == int or type(valor) == float:
            for cliente in self.clientesList:
                if cliente['numeroConta'] == clienteLogado['numeroConta']:
                    cliente['saldo'] +=valor
                    print(f"O depósito de R${valor} foi realizado com sucesso!")
                    self.updateJson()
        else:
            print("Escolha um valor válido.")
    
    def saque(self, valor, clienteLogado):
        if type(valor) == int or type(valor) == float:
            for cliente in self.clientesList:
                if cliente['numeroConta'] == clienteLogado['numeroConta']:
                    if cliente['saldo']>= valor:
                        cliente['saldo'] -=valor
                        print(f"O saque de R${valor} foi realizado com sucesso!")
                        self.updateJson()
                    else:
                        print(f"Você não possui saldo suficiente para sacar R${valor}.")
        elif type(valor) == str:
            print("Escolha um valor válido.")


    def pagamentoProgramado(self,valor, clienteLogado):
        if type(valor) == int or type(valor) ==float:
            for cliente in self.clientesList:
                if cliente['numeroConta'] == clienteLogado['numeroConta']:
                    
                    dia = str(input('Qual é o dia do pagamento programado? [DD]\n'))
                    mes = str(input('Qual é o mês do pagamento programado? [MM]\n'))
                    ano = str(input('Qual é o ano do pagamento programado? [AAAA]\n'))
                    diahoje =date.today().strftime("%d")
                    meshoje = int(date.today().strftime("%m"))
                    anohoje = date.today().strftime("%Y")
                    verificarAno = str.isnumeric(ano)
                    verificarMes = str.isnumeric(mes)
                    verificarDia = str.isnumeric(dia)

                    if int(dia) >31 and verificarDia == True:
                        verificarDia = False
                    
                    elif int(dia) <= 31 and int(dia) >28 and int(mes) == 2:
                        verificarDia =False
                        print(f'Fevereiro não possui o dia {dia}')
                    
                    if int(mes) >= 12 and verificarMes == True:
                        verificarMes = False
                    
                    if int(ano) < int(anohoje) and verificarAno ==True:
                        verificarAno = False
                    if int(ano) == int(anohoje) and int(mes)< int(meshoje) and verificarAno ==True:
                        verificarAno = False
                    if int(ano) == int(anohoje) and int(mes)== int(meshoje) and int(dia)< int(diahoje) and verificarAno ==True:
                        verificarAno = False

                    if verificarAno == True and verificarMes == True and verificarDia ==True:
                        if len(ano) == 4 and len(mes) ==2 and len(dia)==2:
                            data = ano+"-"+mes+"-"+dia
                            hoje =str(date.today())
                            novoPagamento = Pagamento(valor,clienteLogado['numeroConta'],data)
                            if data==hoje and cliente['saldo']>=valor:
                                cliente['saldo'] -= valor
                                self.updateJson()
                                print('Pagamento foi realizado')
                                return True
                                break
                            elif data!=hoje:
                                cliente['saldo'] = cliente['saldo']
                                print(f'Pagamento de R${valor} é para a data {data}. O pagamento ainda não foi efetuado.')
                                verificacaoController.registrarPagamento(clienteLogado['numeroConta'],valor,data)
                                return False
                                break
                            elif data==hoje and cliente['saldo']<valor:
                                print("Operação não realiza! Saldo insuficiente.")
                                return False
                                break  
                            else:
                                print("O pagamento já foi efetuado")
                                return False
                    else:
                        print('Data incorreta. Tente novamente inserindo dias válidos')
        else:
            print("Escolha um valor válido.")
    
    def solicitarCredito(self, clienteLogado,credito, parcela,data):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == clienteLogado['numeroConta']:
                tipoCredito=input("Responda o número correspondente a sua opção:\n 1-Pessoa Física\n 2-Pessoa Jurídica\n")
                valorParcela=0.0
                if tipoCredito =='1':
                    taxa = 1+(0.5**parcela)
                    valorParcela = (taxa*credito)/parcela    
                elif tipoCredito == '2':
                    taxa = 1+(0.15**parcela)
                    valorParcela = (taxa*credito)/parcela
                clienteLogado['saldo']+=credito

                print(f'Você solicitou um crédito de {credito} que será parcelado em {parcela}x e o valor de cada parcela será de {valorParcela} que será cobrado no dia {data} dos próximos {parcela} meses.')
                    
                hoje =date.today().strftime("%d")
                mes = int(date.today().strftime("%m"))
                ano = int(date.today().strftime("%Y"))
                for i in range(0,parcela):
                    mes+=1
                    print(mes)
            
                    if mes<10:
                        dataPagamento = f"{ano}-0{mes}-{data}"
                        if mes == 2 and int(data)>28:
                            dataPagamento = f"{ano}-03-01"
                    elif mes>=10 and mes <=12:
                        dataPagamento = f"{ano}-{mes}-{data}"
                    elif mes>12:
                        ano+=1
                        mes=1
                        #if mes<10:
                        dataPagamento =f"{ano}-0{mes}-{data}"
                        
                    numeroDaParcela = i+1
                    verificacaoController.registrarCredito(clienteLogado['numeroConta'], numeroDaParcela, valorParcela, dataPagamento)
                if data==hoje and clienteLogado['saldo']>=valorParcela:
                    clienteLogado['saldo'] -= valorParcela
                    self.updateJson()
                    return {True, valorParcela}
                elif data==hoje and clienteLogado['saldo']<valorParcela:
                    print("Operação não realiza! Saldo insuficiente.")
                    return False
                else:
                    return False
