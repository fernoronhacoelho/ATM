import json
from datetime import date
from Models.models import Transacao, Conta

class TransacaoController():
    def __init__(self, extratosList, extratosDir):
        self.extratosList = extratosList
        self.extratosDir = extratosDir
    def updateJson(self, conta, transacoes):
        with open(f"database\\Transacoes\\extratos_{conta}.json", 'w') as updateFile:
            json.dump(transacoes, updateFile, indent=4)
        updateFile.close()
    def registrarTransacao(self, tipo, valor, conta, data):
        data = str(date.today())
        novaTransacao = Transacao(tipo, valor, conta, data)
        converteTransacao = vars(novaTransacao)

        with open(f"database\\Transacoes\\extratos_{conta}.json") as transactionsFile:
            transacoes = json.load(transactionsFile)
            transacoes.append(converteTransacao)

        self.updateJson(conta,transacoes)

        transactionsFile.close()

    def mostrarExtrato(self,noConta):
        with open(f"database\\Transacoes\\extratos_{noConta}.json") as transactionsFile:
            transacoes = json.load(transactionsFile)
            if transacoes == []:
                print("Você não possui nenhum registro de transação")
            else:
                print(f"Você está acessando o extrato da conta {noConta}\n")
                print(" Tipo de transação              Valor                 Data")
                for transacao in transacoes:
                    if transacao['numeroConta'] == noConta:
                        print(f"{transacao['tipo']}   {transacao['valor']}    {transacao['data']}\n")
                        
