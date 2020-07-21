import random
from conta import Conta

class Loja:
    def __init__(self, i):
        self.i = i
        self.conta = Conta(0)
        self.custo = round(random.random() * 10, 2)
        self.satisfacao = random.randint(0, 10)
        self.capacidade = random.randint(5, 100)

    def visita_clientes(self):
        if self.capacidade >= 0:
            self.capacidade -= 1
            return True
        else:
            return False

    def oferece_satisfacao(self):
        if self.capacidade <= 5:
            self.satisfacao -= 10
            return self.satisfacao
        elif self.capacidade < 50:
            return self.satisfacao
        else:
            self.satisfacao += 10
            return self.satisfacao

    def __repr__(self):
        return self.i

if __name__ == '__main__':
    fast_shop = Loja('shopping_conjunto')
    big_box = Loja('big_box')
    pizza_do_tom_ze = Loja('pizza1')
    carrefour = Loja('boulevard_shopping')
    pizza_do_tom_ze.conta.deposito(20000)