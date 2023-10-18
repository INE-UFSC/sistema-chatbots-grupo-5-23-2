from .Bot import Bot
from .Comando import Comando


class BotAmigavel(Bot):
    def __init__(self,  nome):
        self.__nome = nome
        self.__comandos = [Comando(1, 'Bom dia', ['Bom dia! Como você está?']), 
                           Comando(2, 'Conte uma piada', ['Por que o esqueleto não briga com ninguém?\nPorque ele não tem saco!']), 
                           Comando(3, 'Quero um conselho', ['Pegue e se cuide! Ande pela sombra sempre.'])]
                        #Dicionário substituido por lista de objetos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def comandos(self):
        return self.__comandos


    def apresentacao(self):
        return(f'Olá, sou o {self.__nome}! Fico feliz em conhecê-lo!')
 
    def mostra_comandos(self):
        for comando in self.__comandos:
            print(f'{comando.id} - {comando.mensagem}')
            #Substituido para lógica com atributos da classe Comando
            
    def executa_comando(self, id):
        for comando in (self.__comandos):
            if comando.id == id or comando.mensagem == id:
                return str(comando.getRandomResposta())
        return "Comando inexistente! Tente novamente por favor :)"

    def boas_vindas(self):
        return f'Obrigado por ter me escolhido. Espero que sejamos bons amigos.'

    def despedida(self):
        return 'Pena que já acabou...'
