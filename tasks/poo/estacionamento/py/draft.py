from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, hora_entrada: int, tipo: str):
        self.id = id
        self.hora_entrada: int = hora_entrada
        self.tipo = tipo

    def setEntrada(self, hora_entrada: int):
        self.hora_entrada = hora_entrada

    def getEntrada(self):
        return self.hora_entrada
    
    def getTipo(self):
        return self.tipo
    
    def getId(self):
        return self.id
    
    @abstractmethod
    def calcularValor(self, hora_saida: int):
        pass

    def __str__(self):
        tipo_ajust = self.tipo.rjust(10, "_")
        id_ajust = self.id.rjust(10, "_")
        return f"{tipo_ajust} : {id_ajust} : {int(self.hora_entrada)}"


class Bike(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, 0, "Bike")

    def calcularValor(self, hora_saida: int):
        return 3

class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, 0, "Moto")

    def calcularValor(self, hora_saida):
        tempoHoras = hora_saida - self.hora_entrada
        return tempoHoras/20
    
class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, 0, "Carro")

    def calcularValor(self, hora_saida):
        tempoHoras = hora_saida - self.hora_entrada
        valor = tempoHoras / 10
        if valor < 5:
            valor = 5
        return valor
    
class Estacionamento:
    def __init__(self):
        self.veiculos: list[Veiculo] = []
        self.hora_atual = 0

    def procurarVeiculo(self, id: str) -> int:
        for i, veiculo in enumerate(self.veiculos):
            if veiculo.getId() == id:
                return i
        return -1
        
    def estacionar(self, veiculo: Veiculo):
        if self.procurarVeiculo(veiculo.getId()) != -1:
            return f"fail: veiculo ja esta no estacionamento"
        self.veiculos.append(veiculo)
        veiculo.setEntrada(self.hora_atual)

    def pagar(self, id: str):
        index = self.procurarVeiculo(id)
        if index == -1:
            return f"fail: veiculo nao esta no estacionamento"
        v = self.veiculos[index]
        valor = v.calcularValor(self.hora_atual)
        return f"{v.getTipo()} chegou {int(v.getEntrada())} saiu {int(self.hora_atual)}. Pagar R$ {valor:.2f}"
    
    def sair(self, id: str):
        index = self.procurarVeiculo(id)
        if index == -1:
            return f"fail: veiculo nao esta no estacionamneto"
        v = self.veiculos[index]
        valor = v.calcularValor(self.hora_atual)
        self.veiculos.pop(index)
        return f"Veiculo {v.getTipo()} saiu do estacionamento e pagou R${valor}"

    def passarTempo(self, tempo: float):
        self.hora_atual += tempo

    def __str__(self):
        if len(self.veiculos) == 0:
            return f"Hora atual: {int(self.hora_atual)}"
        lista = "\n".join(str(v) for v in self.veiculos)
        return f"{lista}\nHora atual: {int(self.hora_atual)}"
    
def main():
    estacionamento = Estacionamento()
    while True:
        line = input()
        print(f"${line}")
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "estacionar":
            tipo = args[1].lower()
            id = args[2]

            if tipo == "bike":
                res = estacionamento.estacionar(Bike(id))
                if res is not None:
                    print(res)
            
            elif tipo == "moto":
                res = estacionamento.estacionar(Moto(id))
                if res is not None:
                    print(res)

            elif tipo == "carro":
                res = estacionamento.estacionar(Carro(id))
                if res is not None:
                    print(res)

        elif args[0] == "pagar":
            id = args[1]
            print(estacionamento.pagar(id))

        elif args[0] == "sair":
            id = args[1]
            print(estacionamento.sair(id))

        elif args[0] == "tempo":
            tempo = float(args[1])
            estacionamento.passarTempo(tempo)
        elif args[0] == "show":
            print(estacionamento)

main()