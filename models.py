import datetime
import json

class Cliente():

    def __init__(self, nome, cpf_cnpj, endereco, telefone, numeroConta, senha):
        self.nome = nome
        self.cpf_cnpj = cpf_cnpj
        self.endereco = endereco
        self.telefone = telefone
        self.numeroConta = numeroConta
        self.senha = senha

    def sacarDinheiro(self):
        valor = input("Qual valor você quer sacar em R$?\n")
        noConta = input("Número da sua conta?\n")
        Transacao.sacar(noConta, valor)
        pass

    def depositarDinheiro(self):
        valor = input("Qual valor você quer depositar em R$?\n")
        noConta = input("Número da sua conta?\n")
        Transacao.depositar(noConta, valor)
        pass
    
    def programarPagamento(self):
        valor = input("Qual valor do pagamento que você quer programar o pagamento em R$?\n")
        noConta = input("Número da sua conta?\n")
        Transacao.pagamentoProgramado(noConta, valor)
        pass
    
    def solicitarCredito(self):
        valor = input("Qual valor você quer de crédito concedido em R$?\n")
        noConta = input("Número da sua conta?\n")
        parcelas = input("Qual é o número de parcelas desejado?")
        data = input("Qual dia do mês você vai realizar o pagamento dessas parcelas? No formato dd \n")
        Transacao.solicitarCredito(noConta, valor, parcelas, data)
        pass
    
class Gerente():
    def __init__(self):
        self.numeroConta = '00000'
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
        self.saldo = 0
        self.numeroConta = noConta
        self.extrato = []


class Transacao(Conta):
    
    def __init__(self, noConta):
        super().__init__(noConta)
        self.limite = self.saldo
    
    def depositar(self, noConta, valor):
        self.saldo+=valor
        return self.saldo
    def sacar(self, noConta, valor):
        if valor <= self.limite:
            self.saldo-=valor
        #   self.extrato.append(
        #        {
        #            "Número da Conta": noConta,   
        #            "Tipo": "Saque",
        #            "Valor": valor,
        #           "Data":datetime.now().strftime("%d-%m-%Y %H:%M:%s")
        #       }
        #    )
        else:
            print("Operação não realiza! Saldo insuficiente.")
    def pagamentoProgramado(self,noConta,valor):
        data = input('Qual é a data do pagamento programado? [DD-MM-AAAA]\n')
        hoje =datetime.now().strftime("%d-%m-%Y")
        
        if data==hoje and self.saldo>=valor:
            self._saldo -= valor
            self.extrato.append(
            
        )
        
        elif data==hoje and self.saldo<valor:
            print("Operação não realiza! Saldo insuficiente.")
        
        else:
            pass
    
    def solicitarCredito(self, noConta, credito, parcela,data):
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
            
        elif data==hoje and self.saldo<valorParcela:
            print("Operação não realiza! Saldo insuficiente.")
        else:
            pass

class manipulardb():
    jsonDirCliente = "database\clientes.json"
    jsonDirExtrato = "database\extratos.json"

    with open(jsonDirCliente) as fp:
        userList = json.load(fp)
   # novoCliente = Gerente.passCliente
    #convertCliente = vars(novoCliente)
    #userList.append(convertCliente)

    with open(jsonDirCliente, "w") as updateFile:
        json.dump(userList, updateFile, indent=4)