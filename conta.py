

class Conta:
    def __init__(self, i):
        self.i = i
        self.saldo = 0

    def deposito(self, quantia):
        self.saldo += quantia
        return quantia

    def retirada(self, quantia):
        self.saldo -= quantia
        return quantia

if __name__ == '__main__':
    santander = Conta(2550399)
    santander.deposito(500)
    santander.deposito(650)
    santander.deposito(200)