import json
from datetime import date
from Models.models import Pagamento, Credito, Conta
class VerificaoController():
    def __init__(self, pagamentosList, pagamentosDir, creditosList, creditosDir):
        self.pagamentosList = pagamentosList
        self.pagamentosDir = pagamentosDir
        self.creditosList = creditosList
        self.creditosDir = creditosDir
    
    def updateJsonPagamento(self):
        with open(self.pagamentosDir, 'w') as updateFile:
            json.dump(self.pagamentosList, updateFile, indent=4)
    
    def registrarPagamento(self, conta, valor, data):
        novoPagamento = Pagamento(conta, valor, data)
        convertePagamento = vars(novoPagamento)
        self.pagamentosList.append(convertePagamento)
        self.updateJsonPagamento()
    
    def updateJsonCreditos(self):
        with open(self.creditosDir, 'w') as updateFile:
            json.dump(self.creditosList, updateFile, indent=4)
    
    def registrarCredito(self, conta, numeroDaParcela, valorParcela, dataPagamento):
        novoCredito = Credito(conta, numeroDaParcela, valorParcela, dataPagamento)
        converteCredito = vars(novoCredito)
        self.creditosList.append(converteCredito)
        self.updateJsonCreditos()
    
    def excluirPagamento(self, noConta):
        hoje = str(date.today())
        for pagamento in self.pagamentosList:
            if pagamento['data'] == hoje:
                self.pagamentosList.remove(pagamento)                

    def mostrarPagamento(self,noConta):
        for pagamento in self.pagamentosList: 
            if pagamento['numeroConta'] == noConta:
                print(f'{pagamento} \n')

    def excluirCredito(self, noConta):
        hoje = str(date.today())
        for credito in self.creditosList:
            if credito['data'] == hoje:
                self.creditosList.remove(credito)

    def mostrarCredito(self,noConta):
        for credito in self.creditosList: 
            if credito['numeroConta'] == noConta:
                print(f'{credito} \n')

    def verificarPagamentoCredito(self, clienteLogado):
        for credito in self.creditosList:
            if clienteLogado['numeroConta'] == credito['numeroConta']:
                hoje = str(date.today())
                verificar=False
                if credito['data'] == hoje:
                    if clienteLogado['saldo']>=credito['valor']:
                        clienteLogado['saldo'] -= credito['valor']
                        print('Pagamento foi realizado')
                        self.excluirCredito(clienteLogado['numeroConta'])
                        verificar = credito['valor']
                        break
                elif credito['data']!=hoje:
                    clienteLogado['saldo'] = clienteLogado['saldo']
                    print(f"Pagamento da parcela {credito['numeroParcela']} de R${credito['valor']} é para a data {credito['data']}. O pagamento ainda não foi efetuado.")
                    verificar = False
        print("A lista de pagamento dos créditos está verificada\n")
        return verificar
    def verificarPagamento(self, clienteLogado):
        for pagamento in self.pagamentosList:
            if clienteLogado['numeroConta'] == pagamento['numeroConta']:
                hoje = str(date.today())
                verificar =False
                if pagamento['data'] == hoje:
                    if clienteLogado['saldo']>=pagamento['valor']:
                        clienteLogado['saldo'] -= pagamento['valor']
                        print('Pagamento foi realizado')
                        self.excluirPagamento(clienteLogado['numeroConta'])
                        verificar = pagamento['valor']
                        break
                elif pagamento['data']!=hoje:
                    clienteLogado['saldo'] = clienteLogado['saldo']
                    print(f"Pagamento de R${pagamento['valor']} é para a data {pagamento['data']}. O pagamento ainda não foi efetuado.\n")
                    verificar = False
        print("A lista de pagamento programado está verificada")
        return verificar
        