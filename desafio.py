from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

#INICIO CLASSES

class Conta:
    def __init__(self, cliente: Cliente, numero: int):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
        
    @property
    def agencia(self):
        return self._agencia
        
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
         
    def sacar(self, valor: float):
    
        if self.saldo < valor:
            print("Operação inválida! Saldo insuficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso.")
            return True
        
        else:
            print("Operação inválida! O valor informado precisa ser maior que R$ 0,00.")
        
        return False
   
    def depositar(self, valor: float):
    
        if valor > 0:
            self._saldo += valor
            print("\nDepósito realizado com sucesso.")
        else:
            print("Operação inválida! O valor informado precisa ser maior que R$ 0,00.")
            return False
        return True

class ContaCorrente(Conta):
    def __init__(self, cliente: Cliente, numero: int, limite = 500, limite_saques = 3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        
    def sacar(self, valor):
        numero_saques = 0
        for transacao in self.historico.transacoes:
            numero_saques += (transacao["tipo"] == Saque.__name__)
    
        if self.saldo < valor:
            print("Operação inválida! Saldo insuficiente.")
        elif valor > limite:
            print(f"Operação inválida! Valor máximo para saque é de R$ {limite:.2f}.")
        elif numero_saques >= limite_saques:
            print("Operação inválida! Limite de saques diários atingido.")
            
        elif valor > 0:
            self._saldo -= valor
            print("\nSaque realizado com sucesso.")
            return True    
        else:
            print("Operação inválida! O valor informado precisa ser maior que R$ 0,00.")
        
        return False
        
class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractclassmethod
    def registrar(self, conta: Conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)
        
class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta: Conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
        
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
        
    def adicionar_transacao(self, transacao: Transacao):
        registro = {
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
        }
        self.transacoes.append(registro)
        

class Cliente:
    def __init__(self, endereco: str):
        self._endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)
        
class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

#FIM CLASSES

#TODO: Reimplementar funções abaixo.

def menu():
    return "\n[d] Depositar\n[s] Sacar\n[e] Extrato\n[nc] Nova conta\n[nu] Novo usuário\n[lc] Listar contas\n[q] Sair\n\n=>\t"
    
def depositar(clientes):
    pass

def sacar(clientes):
    pass

def emitir_extrato(clientes):
    pass

def criar_cliente(clientes):
    pass

def criar_conta(numero_conta, clientes, contas):
    pass

def listar_contas(contas):
    pass

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            criar_conta(len(contas) + 1, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()

def main():
    clientes = []
    contas = []

    while True:
        opcao = input(menu())

        if opcao == "q":
            break
        
        elif opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)
            
        else:
            print("Operação inválida! Por favor certifique-se de que esteja selecionando a operação desejada e tente de novo.")

main()
