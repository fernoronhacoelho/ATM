import json
from models import Cliente

class ClienteController():
    def __init__(self, clienteList, clientesDir):
        self.clientesList = clienteList
        self.clientesDir = clientesDir
    def updateJson(self):
        with open(self.clientesDir, 'w') as updateFile:
            json.dump(self.clientesList, updateFile, indent=4)
    def registrarCliente (self, nome, cpf_cnpj, endereco, telefone, numeroConta, senha):
        novoCliente = Cliente(nome, cpf_cnpj, endereco, telefone, numeroConta, senha)
        converteCliente = vars(novoCliente)
        self.clientesList.append(converteCliente)
        self.updateJson()


    def login(self, noConta, senha):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == noConta and cliente['senha'] == senha:
                return cliente
    
    def deposito(self, valor, clienteLogado):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == clienteLogado['numeroConta']:
                cliente['saldo'] +=valor
                self.updateJson()

