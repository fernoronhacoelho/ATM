from datetime import *
import json

class Cliente():

    def __init__(self, nome, cpf_cnpj, endereco, telefone, numeroConta, senha,saldo):
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.endereco = endereco
        self.telefone = telefone
        self.numeroConta = numeroConta
        self.senha = senha
        self.saldo = saldo

    
    
class Gerente():
    def __init__(self):
        self.numeroConta = '0000'
        self.senha = 'gerente'

class Conta():
    
    def __init__(self, noConta):
        self.numeroConta = noConta


class Transacao(Conta):
    
    def __init__(self, tipo, valor, noConta, data='0'):
        super().__init__(noConta)
        
        self.tipo = tipo
        self.valor = valor
        self.data = data

class Pagamento(Conta):
    def __init__(self, noConta, valor, data):
        super().__init__(noConta)
        
        self.valor = valor
        self.data = data
class Credito(Conta):
    def __init__(self, noConta, numeroDaParcela, valorParcela, dataPagamento):
        super().__init__(noConta)
        
       
        self.valor = valorParcela
        self.numeroParcela = numeroDaParcela
        self.data = dataPagamento
