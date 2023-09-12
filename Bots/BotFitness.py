from Bots.Bot import Bot

class BotFitness(Bot):
    def __init__(self,nome):
        self.__nome = nome
        self.comandos = {
            1: {
                'comando': 'Quero uma opinião sobre o meu treino', 
                'resposta': 'Após uma avaliação minuciosa, percebi que você é um FRANGO !'
                },
            2: {
                'comando': 'Treino para braço', 
                'resposta': 'Comece alongando os braços\n- 3 séries de 2 minutos tentando cortar o bife do RU\n- 2 séries de 2 minutos tentando cortar a bisteca do RU'
                },
            3: {
                'comando': 'Quero uma opinião sobre o meu shape', 
                'resposta': 'Look at him. Nem parece que treina... Braços finos, corpo compacto e pouco aesthetic'
                },
        }

    @property
    def nome(self):
        return self.__nome

    def apresentacao(self):
        return "Eu sou o Rodrigo Goes, natural é a fonte da juventude!"
    
    def executa_comando(self, cmd):
        try:  
            comando = self.__comandos[cmd]['resposta']
        except KeyError:
            comando = 'Comando inexistente, frango!!'
        return comando

    def boas_vindas(self):
        return ("Obrigado por me escolher!")

    def despedida(self):
        return ("Volte sempre meu querido Fake Natty !")