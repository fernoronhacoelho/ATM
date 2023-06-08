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
        for transacao in self.extratosList:
            if transacao['numeroConta'] == noConta:
                print(f'{transacao}\n')
