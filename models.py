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

    def sacarDinheiro():
        valor = input("Qual valor você quer sacar em R$?\n")
        noConta = input("Número da sua conta?\n")
        Transacao.sacar(noConta, valor)
        pass

    def depositarDinheiro():
        valor = input("Qual valor você quer depositar em R$?\n")
        noConta = input("Número da sua conta?\n")
        Transacao.depositar(noConta, valor)
        pass
    
    def programarPagamento():
        valor = input("Qual valor do pagamento que você quer programar o pagamento em R$?\n")
        noConta = input("Número da sua conta?\n")
        Transacao.pagamentoProgramado(noConta, valor)
        pass
    
    def solicitarCredito():
        valor = input("Qual valor você quer de crédito concedido em R$?\n")
        noConta = input("Número da sua conta?\n")
        parcelas = input("Qual é o número de parcelas desejado?")
        data = input("Qual dia do mês você vai realizar o pagamento dessas parcelas? No formato dd \n")
        Transacao.solicitarCredito(noConta, valor, parcelas, data)
        pass
    
class Gerente():
    def __init__(self):
        self.numeroConta = '0000'
        self.senha = 'gerente'


'''
class Gerente():
    
    def __init__(self, senha):
        self.senha = senha
        self.clientes=[]
        
    #criar um dicionario com esses dados
    
    def cadastrarUsuario(self):
        
        nome = input('Insira o nome do cliente:\n')
        telefone= input('Insira o telefone do cliente com o ddd no formato (xx) xxxxx-xxxx:\n')
        cpf_cnpj = input('Insira o CPF ou CNPJ (Sem caracteres especiais):\n')
        endereco = input('Insira o endereço do cliente')
        senha = input('Insira sua senha de 6 dígitos')
        
        
        self.clientes.append(
                {
                    'Nome': nome,
                    'CPF_CNPJ': cpf_cnpj,
                    'Endereço': endereco,
                    'Telefone': telefone,
                    'Número da conta': "000"
                    
                    #verificar como gerar números de conta automático
                    #verificar como acessar o número da conta para exportar
                }
        )

    def passCliente(self):
        return self.clientes
'''

class Conta():
    
    def __init__(self, noConta):
        self.numeroConta = noConta


class Transacao(Conta):
    
    def __init__(self, noConta, tipo, valor, data='0'):
        super().__init__(noConta)
        self.conta = noConta
        self.tipo = tipo
        self.valor = valor
        self.data = data

