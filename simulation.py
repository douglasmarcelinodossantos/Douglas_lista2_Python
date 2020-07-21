import random
from loja import Loja
from agente import Agent

class Simulacao:
    def __init__(self):
        self.lojas = list()
        self.clientes = list()
        self.criar_lojas()
        self.criar_clientes()
        self.deposito_inicial()

    def criar_lojas(self):
        for i in range(10):
            self.lojas.append(Loja(i))

    def criar_clientes(self):
        for i in range(10):
            self.clientes.append(Agent(i))

    def media_satisfacao(self):
        satisfacao_somada = 0
        for clientes in self.clientes:
            satisfacao_somada += clientes.satisfacao
        return satisfacao_somada / len(self.clientes)

    def media_custo(self):
        custo_somado = 0
        for loja in self.lojas:
            custo_somado += loja.custo
        return custo_somado / len(self.lojas)

    def media_contas(self):
        saldo_contas_clientes_somada = 0
        for clientes in self.clientes:
            saldo_contas_clientes_somada += clientes.conta.saldo
        saldo_contas_lojas_somada = 0
        for lojas in self.lojas:
           saldo_contas_lojas_somada += lojas.conta.saldo
        return ((saldo_contas_clientes_somada + saldo_contas_lojas_somada) / len(self.clientes + self.lojas))

    def deposito_inicial(self):
        for clientes in self.clientes:
            clientes.conta.deposito(random.randint(10, 20))

    def run_model(self):
        for clientes in self.clientes:
            loja_escolhida = random.choice(self.lojas)
            if clientes.conta.saldo >= 0:
                posso_ir = loja_escolhida.visita_clientes()
                if posso_ir == True:
                    loja_escolhida.conta.deposito(clientes.conta.retirada(loja_escolhida.custo))
                    clientes.satisfacao += loja_escolhida.satisfacao
                    return clientes.satisfacao
                else:
                    return False
            else:
                return False
        return self.media_satisfacao(), self.media_custo(), self.media_contas()

def salvar_information(self):
    with open('information.txt', 'w') as handler:
        handler.write(f'{self}')
        return salvar_information

if __name__ == '__main__':
    minha_sim = Simulacao()
    media = minha_sim.run_model()
    media_satisfacao = minha_sim.media_satisfacao()
    media_custo = minha_sim.media_custo()
    media_contas = minha_sim.media_contas()
    # salvar_information(f'O valor da média
    salvar_information(f'O valor da média da simulação é {media}\n'
                   f'A média de satisfação é {media_satisfacao}\n'
                   f'A média do custo é {media_custo}\n'
                   f'A média de contas é {media_contas}')