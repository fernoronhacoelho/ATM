import json
from Models.models import Cliente
from datetime import date, timedelta

class ClienteController():
    def __init__(self, clienteList, clientesDir):
        self.clientesList = clienteList
        self.clientesDir = clientesDir
        self.pagamentos=[]
        self.creditosParcelas=[]
    
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
                if cliente['saldo']>= valor:
                    cliente['saldo'] -=valor
                    self.updateJson()
                    
    def verificarPagamento(self, clienteLogado):
        for pagamento in self.pagamentos:
            if clienteLogado['numeroConta'] == pagamento[0]:
                hoje = str(date.today())
                if pagamento[1] == hoje:
                    if clienteLogado['saldo']>=pagamento[2]:
                        clienteLogado['saldo'] -= pagamento[2]
                        self.updateJson()
                        print('Pagamento foi realizado')
                        self.pagamentos.remove({clienteLogado['numeroConta'],pagamento[1],pagamento[2]})
                        return {True,pagamento[2]}
                    elif pagamento[1]!=hoje:
                        clienteLogado['saldo'] = clienteLogado['saldo']
                        print(f'Pagamento de R${pagamento[2]} é para a data {pagamento[1]}. O pagamento ainda não foi efetuado.')
                        return False

    def pagamentoProgramado(self,valor, clienteLogado):
        for cliente in self.clientesList:
            if cliente['numeroConta'] == clienteLogado['numeroConta']:
                data = str(input('Qual é a data do pagamento programado? [AAAA-MM-DD]\n'))
                hoje =str(date.today())
                self.pagamentos.append({clienteLogado['numeroConta'],data,valor})
                if data==hoje and cliente['saldo']>=valor:
                    cliente['saldo'] -= valor
                    self.updateJson()
                    print('Pagamento foi realizado')
                    self.pagamentos.remove({clienteLogado['numeroConta'],data,valor})
                    return {True, valor}
                    break
                elif data!=hoje:
                    cliente['saldo'] = cliente['saldo']
                    print(f'Pagamento de R${valor} é para a data {data}. O pagamento ainda não foi efetuado.')
                    self.pagamentos.append({clienteLogado['numeroConta'],data,valor})
                    return False
                    break
                elif data==hoje and cliente['saldo']<valor:
                    print("Operação não realiza! Saldo insuficiente.")
                    return False
                    break  
                else:
                    print("O pagamento já foi efetuado")
                    return False
    
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
                ano = date.today().strftime("%a")
                for i in range(parcela):
                    mes=+1
                    if mes<10:
                        dataPagamento = f"{ano}-0{mes}-{data}"
                    else:
                        dataPagamento = f"{ano}-{mes}-{data}"
                    if mes>12:
                        ano=+1
                        mes=1
                        if mes<10:
                            dataPagamento =f"{ano}-0{mes}-{data}"
                        else:
                            dataPagamento = f"{ano}-{mes}-{data}"
                    numeroDaParcela = i+1
                    self.creditosParcelas.append({clienteLogado["numeroConta"], numeroDaParcela, valorParcela, dataPagamento })
                if data==hoje and clienteLogado['saldo']>=valorParcela:
                    clienteLogado['saldo'] -= valorParcela
                    self.updateJson()
                    return {True, valorParcela}
                elif data==hoje and clienteLogado['saldo']<valorParcela:
                    print("Operação não realiza! Saldo insuficiente.")
                    return False
                else:
                    return False

    def verificarPagamentoCredito(self, clienteLogado):
        for credito in self.creditosParcelas:
            if clienteLogado['numeroConta'] == credito[0]:
                hoje = str(date.today())
                if credito[3] == hoje:
                    if clienteLogado['saldo']>=credito[2]:
                        clienteLogado['saldo'] -= credito[2]
                        print('Pagamento foi realizado')
                        self.updateJson()
                        self.creditosParcelas.remove({clienteLogado['numeroConta'],credito[1],credito[2],credito[3]})
                        return {True, credito[2]}
                    elif credito[1]!=hoje:
                        clienteLogado['saldo'] = clienteLogado['saldo']
                        print(f'Pagamento da parcela {credito[1]} de R${credito[2]} é para a data {credito[3]}. O pagamento ainda não foi efetuado.')
                        return False