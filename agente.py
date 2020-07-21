from conta import Conta
from loja import Loja

class Agent:
    def __init__(self, i):
        self.i = i
        self.conta = Conta(0)
        self.satisfacao = 0

if __name__ == '__main__':
    carrefour = Loja('carrefour')
    carlito = Agent(0)
    juliana = Agent(1)
    juliana.conta.deposito(1000)
    carlito.conta.deposito(2500)
    carrefour.conta.deposito(juliana.conta.retirada(carrefour.custo))
    carrefour.conta.deposito(carlito.conta.retirada(carrefour.custo))

