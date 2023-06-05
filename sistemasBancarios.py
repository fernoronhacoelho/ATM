# Código feito por: Fernanda Noronha
# Versão 2.2  05/06/2023
# Funcao do gerente atualizar o cadastro e apagar cliente
# Organizar os métodos da gerente.
# Realizar as transações
#Criar a automação do json para o extrato considerando a conta
#Fazer o extrato
#Fazer o UML

from datetime import *
import json

class Cliente():
    def __init__(self, nome, endereco, noConta, cpf_cnpj, telefone, senha):
        self.nome = nome
        self.endereco = endereco
        self.NoConta = noConta
        self.cpf_cnpj = cpf_cnpj
        self.telefone = telefone
        self.senha  = senha

class Gerente():
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

class Conta():
    def __init__(self, noConta):
        self.saldo = 0
        self.NoConta = noConta
        self.extrato = []


class Transacoes(Conta):
    
    def __init__(self, noConta):
        super().__init__(noConta)
        self.limite = self.saldo
    
    def registrarTransacao(self, transacao,valor):
        self.extrato.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": valor,
                "data":datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

    def sacar(self, valor):
        if valor <= self.limite:
            self.saldo-=valor
            Transacoes.registrarTransacao("saque",valor)
        else:
            print("Operação não realiza! Saldo insuficiente.")
    
    def depositar(self, valor):
        self.saldo+=valor
        Transacoes.registrarTransacao("depósito",valor)
    
    def pagamentoProgramado(self,valor):
        data = input('Qual é a data do pagamento programado? [DD-MM-AAAA]\n')
        hoje =datetime.now().strftime("%d-%m-%Y")
        if data==hoje and self.saldo>=valor:
            self._saldo -= valor
            Transacoes.registrarTransacao("pagamentoProgramado",valor)
        elif data==hoje and self.saldo<valor:
            print("Operação não realiza! Saldo insuficiente.")
        else:
            pass
    
    def solicitarCredito(self,credito, parcela,data):
        tipoCredito=input("Responda o número correspondente a sua opção:\n 1-Pessoa Física\n 2-Pessoa Jurídica\n")
        if tipoCredito ==1:
            taxa = 1+0.5^parcela
            valorParcela = (taxa*credito)/parcela
        elif tipoCredito == 2:
            taxa = 1+0.15^parcela
            valorParcela = (taxa*credito)/parcela
        self.saldo+=credito
        hoje =datetime.now().strftime("%d")
        if data==hoje and self.saldo>=valorParcela:
            self.saldo -= valorParcela
            Transacoes.registrarTransacao("pagamentoProgramado",valorParcela)
        elif data==hoje and self.saldo<valorParcela:
            print("Operação não realiza! Saldo insuficiente.")
        else:
            pass

class Extrato(Transacoes):
    def __init__(self):
        
        pass
Cliente1=Cliente("Fernanda", "Lago Norte", "1234", "1234456789","61999888999","111111")
print(Cliente1.endereco)

transicao = Transacoes("1234", "Fernanda")
transicao.solicitarCredito(1000,3,31)
print(transicao.transacoes)
transicao.depositar(1000)
print(transicao.transacoes)

class manipulardb():
    jsonDirCliente = "Controllers\clientes.json"
    jsonDirExtrato = "Controllers\extratos.json"

    with open(jsonDirCliente) as fp:
        userList = json.load(fp)
    novoCliente = Gerente.clientes
    convertCliente = vars(novoCliente)
    userList.append(convertCliente)

    novoCliente = Cliente("Gabriel", "Asa Sul", "00002")
    convertCliente = vars(novoCliente)
    userList.append(convertCliente)

    with open(jsonDirCliente, "w") as updateFile:
        json.dump(userList, updateFile, indent=4)


