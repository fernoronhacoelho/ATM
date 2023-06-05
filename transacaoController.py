import json
import datetime
from models import Transacao, Conta

class TransacaoController():
    def __init__(self, extratosList, extratosDir):
        self.extratosList = extratosList
        self.extratosDir = extratosDir
    def updateJson(self):
        with open(self.extratosDir, 'w') as updateFile:
            json.dump(self.extratosList, updateFile, indent=4)
    def registrarTransacaoDeposito (self, numeroConta, valor):
        novaTransacao = Transacao.depositar(numeroConta, valor)
        converteTransacao = vars(novaTransacao)
        self.extratosList.append(
                {
                    "Número da Conta": numeroConta,   
                    "Tipo": "Depósito",
                    "Valor": valor,
                   "Data":datetime.now().strftime("%d-%m-%Y %H:%M:%s")
               }
        )
        self.updateJson()
    
    def registrarTransacaoSaque (self, numeroConta, valor):
        novaTransacao = Transacao.sacar(numeroConta, valor)
        converteTransacao = vars(novaTransacao)
        self.extratosList.append(
            {
                    "Número da Conta": numeroConta,   
                    "Tipo": "Saque",
                    "Valor": valor,
                   "Data":datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            }
         )
        self.updateJson()
    
    def registrarTransacaoDeposito (self, numeroConta, valor):
        novaTransacao = Transacao.pagamentoProgramado(numeroConta, valor)
        converteTransacao = vars(novaTransacao)
        self.extratosList.append({
                "Número da Conta": numeroConta,
                "Tipo": "Pagamento Programado",
                "Valor": valor,
                "Data":datetime.now().strftime("%d-%m-%Y %H:%M:%s")
            })
        self.updateJson()
    
    def registrarTransacaoCredito (self, numeroConta, valorParcela):
        novaTransacao = Transacao.solicitarCredito(numeroConta, valorParcela)
        converteTransacao = vars(novaTransacao)
        self.extratosList.append(
                {
                    "Número da Conta": numeroConta,
                    "Tipo": "Saque",
                    "Valor": valorParcela,
                    "Data":datetime.now().strftime("%d-%m-%Y %H:%M:%s")
                })
        self.updateJson()