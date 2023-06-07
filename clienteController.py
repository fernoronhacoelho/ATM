import json
from Models.models import Cliente
from datetime import date

class ClienteController():
    def __init__(self, clienteList, clientesDir):
        self.clientesList = clienteList
        self.clientesDir = clientesDir
    def updateJson(self):
        with open(self.clientesDir, 'w') as updateFile:
            json.dump(self.clientesList, updateFile, indent=4)
    def registrarCliente (self, nome, cpf_cnpj, endereco, telefone, numeroConta, senha, saldo):
        novoCliente = Cliente(nome, cpf_cnpj, endereco, telefone, numeroConta, senha, saldo)
        converteCliente = vars(novoCliente)
        self.clientesList.append(converteCliente)
        self.updateJson()

    def cadastrarUsuarioNome():  
        nome= input('Insira o nome do cliente: \n')
        return nome
    def atualizarUsuarioNome(self,noConta, novoNome):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == noConta:
                cliente['nome'] = novoNome

    def cadastrarUsuarioTelefone():  
        telefone= input('Insira o telefone do cliente com o ddd no formato (xx) xxxxx-xxxx: \n')
        return telefone
    def atualizarUsuarioTelefone(self,telefone, novoTelefone):
        for cliente in self.clientesList:
            if cliente['telefone'] == telefone:
                cliente['telefone'] = novoTelefone
    def cadastrarUsuarioCPF_CNPJ():  
        cpf_cnpj = input('Insira o CPF ou CNPJ (Sem caracteres especiais): \n')
        return cpf_cnpj
    def atualizarUsuarioCPF_CNPJ(self,cpf_cnpj, novoCPF_CNPJ):
        for cliente in self.clientesList:
            if cliente['cpf_cnpj'] == cpf_cnpj:
                cliente['cpf_cnpj'] = novoCPF_CNPJ
    def cadastrarUsuarioEndereco():  
        endereco = input('Insira o endereço do cliente: \n')
        return endereco
    def atualizarUsuarioEndereco(self,noConta, novoEndereco):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == noConta:
                cliente['endereco'] = novoEndereco
    def cadastrarUsuarioNoConta():  
        noConta = input('Insira o número da conta: \n')
        return noConta
    def cadastrarUsuarioSenha():  
        senha = input('Insira sua senha de 6 dígitos: \n')
        return senha

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
        for cliente in self.clientesList:
            if cliente['numeroConta'] == clienteLogado['numeroConta']:
                cliente['saldo'] +=valor
                self.updateJson()
    def saque(self, valor, clienteLogado):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == clienteLogado['numeroConta']:
                if cliente['saldo']<= valor:
                    cliente['saldo'] -=valor
                    self.updateJson()
                    

    def pagamentoProgramado(self,valor, clienteLogado):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == clienteLogado['numeroConta']:
                data = input('Qual é a data do pagamento programado? [DD-MM-AAAA]\n')
                hoje =date.today().strftime("%d-%m-%Y")
                if data==hoje and cliente['saldo']>=valor:
                    cliente['saldo'] -= valor
                elif data!=hoje:
                    cliente['saldo'] = cliente['saldo']
                elif data==hoje and cliente['saldo']<valor:
                    print("Operação não realiza! Saldo insuficiente.")  
                else:
                    pass
    
    def solicitarCredito(self, clienteLogado,credito, parcela,data):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == clienteLogado['numeroConta']:
                tipoCredito=input("Responda o número correspondente a sua opção:\n 1-Pessoa Física\n 2-Pessoa Jurídica\n")
                if tipoCredito ==1:
                    taxa = 1+0.5^parcela
                    valorParcela = (taxa*credito)/parcela    
                elif tipoCredito == 2:
                    taxa = 1+0.15^parcela
                    valorParcela = (taxa*credito)/parcela
                clienteLogado['saldo']+=credito
                hoje =date.today().strftime("%d")
                if data==hoje and clienteLogado['saldo']>=valorParcela:
                    clienteLogado['saldo'] -= valorParcela
            
                elif data==hoje and clienteLogado['saldo']<valorParcela:
                    print("Operação não realiza! Saldo insuficiente.")
                else:
                    pass