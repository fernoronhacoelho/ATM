import json
from Models.models import Cliente
import datetime

class ClienteController():
    def __init__(self, clienteList, clientesDir):
        self.clientesList = clienteList
        self.clientesDir = clientesDir
    def updateJson(self):
        with open(self.clientesDir, 'w') as updateFile:
            json.dump(self.clientesList, updateFile, indent=4)
    def registrarCliente (self, nome, cpf_cnpj, endereco, telefone, numeroConta, senha, saldo):
        #date = datetime.now()
        novoCliente = Cliente(nome, cpf_cnpj, endereco, telefone, numeroConta, senha, saldo)
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
                hoje =datetime.now().strftime("%d-%m-%Y")
                if data==hoje and cliente['saldo']>=valor:
                    cliente['saldo'] -= valor
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
                saldo+=credito
                hoje =datetime.now().strftime("%d")
                if data==hoje and cliente['saldo']>=valorParcela:
                    cliente['saldo'] -= valorParcela
            
                elif data==hoje and saldo<valorParcela:
                    print("Operação não realiza! Saldo insuficiente.")
                else:
                    pass