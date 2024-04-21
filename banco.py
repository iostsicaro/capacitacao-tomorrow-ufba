class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    #o carctere f é usado para interpolação, funcionando da mesma 
    #forma que o template string do JS
    def __str__(self):
        return f"Cliente: {self.nome}, CPF: {self.cpf}"
    
class Conta:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if(valor <= self.saldo):
            self.saldo -= valor
            print("SALDO REALIZADO COM SUCESSO!")
            print(f"SALDO: {self.saldo}")
        else:
            print("SALDO INSUFICIENTE!")
    
    def consulta(self):
        print(f"SALDO: {self.saldo}")

    def __str__(self):
        return f"Conta do cliente: {self.cliente.nome}, SALDO: {self.saldo}"

class ContaCorrente(Conta):
    def __init__(self, cliente, saldo=0, limite=1000):
        super().__init__(cliente, saldo)
        self.limite = limite
    
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
        else:
            print("Limite de saque excedido.")

class ContaPoupanca(Conta):
    def __init__(self, cliente, saldo=0, juros=0.01):
        super().__init__(cliente, saldo)
        self.juros = juros
    
    def aplicar_juros(self):
        self.saldo += self.saldo * self.juros

cliente1 = Cliente("Icaro", "123.456.789-05")
cliente2 = Cliente("Matheus", "678.908.456-32")

conta_corrente = ContaCorrente(cliente1, saldo=20000, limite=500)
conta_poupanca = ContaPoupanca(cliente2, saldo=50000, juros=70)

conta_corrente.deposito(500)
conta_poupanca.deposito(100)
conta_poupanca.aplicar_juros()

conta_corrente.consulta()
conta_poupanca.consulta()