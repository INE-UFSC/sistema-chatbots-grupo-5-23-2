from .Bot import Bot
from .Comando import Comando

class BotFitness(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.__comandos = [Comando(1, 'Quero uma opinião sobre o meu treino', ['Após uma avaliação minuciosa, percebi que você é um FRANGO !']), 
                           Comando(2, 'Treino para braço', ['Comece alongando os braços\n- 3 séries de 2 minutos tentando cortar o bife do RU\n- 2 séries de 2 minutos tentando cortar a bisteca do RU']), 
                           Comando(3, 'Quero uma opinião sobre o meu shape', ['Look at him. Nem parece que treina... Braços finos, corpo compacto e pouco aesthetic'])]
                        #Dicionário substituido por lista de objetos

    @property
    def nome(self):
        return self.__nome

    @property
    def comandos(self):
        return self.__comandos

    def apresentacao(self):
        return 'Eu sou o Rodrigo Goes, natural é a fonte da juventude!'
    
    def mostra_comandos(self):
        for comando in self.__comandos:
            print(f'{comando.id} - {comando.mensagem}')
            #Substituido para lógica com atributos da classe Comando
            
    def executa_comando(self, id):
        try:  
            for comando in self.__comandos:
                if comando.id == id:
                    return comando.getRandomResposta()
        except KeyError:
            return 'Comando inexistente, frango!!'

    def boas_vindas(self):
        return ('Obrigado por me escolher!')

    def despedida(self):
        return ('Volte sempre meu querido Fake Natty !')