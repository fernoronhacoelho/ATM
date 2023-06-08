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
    
    def atualizarUsuarioTelefone(self,telefone, novoTelefone):
        for cliente in self.clientesList:
            if cliente['telefone'] == telefone:
                if len(telefone) == 13 or len(telefone) ==14:
                    cliente['telefone'] = novoTelefone
        else:
            print('Digite um telefone válido, lembre-se do formato solicitado!\n')
            return False
                
    def cadastrarUsuarioCPF_CNPJ():  
        cpf_cnpj = input('Insira o CPF ou CNPJ (Sem caracteres especiais): \n')
        if len(cpf_cnpj) == 11 or len(cpf_cnpj) == 14:
            return cpf_cnpj
        else:
            print('Digite um CPF/CNPJ válido, lembre-se do formato solicitado!\n')
            return False
    
    def atualizarUsuarioCPF_CNPJ(self,cpf_cnpj, novoCPF_CNPJ):
        for cliente in self.clientesList:
            if cliente['cpf_cnpj'] == cpf_cnpj:
                if len(cpf_cnpj) == 11 or len(cpf_cnpj) == 14:
                    cliente['cpf_cnpj'] = novoCPF_CNPJ
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
        if len(senha) == 6:
            return senha
        else:
            print('A senha está incorreta. Ela deve conter 6 dígitos.\n')
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
                data = str(input('Qual é a data do pagamento programado? [AAAA-MM-DD]\n'))
                hoje =str(date.today())
                if data==hoje and cliente['saldo']>=valor:
                    cliente['saldo'] -= valor
                    print('Pagamento foi realizado')
                elif data!=hoje:
                    cliente['saldo'] = cliente['saldo']
                    print(f'Pagamento de R${valor} é para a data {data}. O pagamento ainda não foi efetuado.')
                    
                elif data==hoje and cliente['saldo']<valor:
                    print("Operação não realiza! Saldo insuficiente.")  
                else:
                    print("O pagamento já foi efetuado")
    
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
                print(hoje)
                print(data)
                if data==hoje and clienteLogado['saldo']>=valorParcela:
                    clienteLogado['saldo'] -= valorParcela
                elif data==hoje and clienteLogado['saldo']<valorParcela:
                    print("Operação não realiza! Saldo insuficiente.")
                else:
                    pass
