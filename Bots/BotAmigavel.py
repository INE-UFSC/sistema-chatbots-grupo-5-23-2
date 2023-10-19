from .Bot import Bot
from .Comando import Comando


#Florzinha
class BotAmigavel(Bot):
    def __init__(self,  nome):
        self.__nome = nome
        self.__comandos = [Comando('Bom dia', ['Bom dia! Como você está?']), 
                           Comando('Conte uma piada', ['Por que o esqueleto não briga com ninguém?\nPorque ele não tem saco!']), 
                           Comando('Quero um conselho', ['Pegue e se cuide! Ande pela sombra sempre.'])]
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
            
    def executa_comando(self, id_comando: str):
        flag = False
        for comando in (self.__comandos):
            if comando.id.upper() == id_comando.upper():
                flag = True
                return str(comando.getRandomResposta())
        if flag == False:
            return "Comando inexistente! Tente novamente por favor :) Se precisar de ajuda clique em 'ajuda'"
            #Tava com um return de comando inexistente aqui que rodaria anyways, coloquei uma flag para verificar se ele encontrou resposta

    def boas_vindas(self):
        return 'Obrigado por ter me escolhido. Espero que sejamos bons amigos.'

    def despedida(self):
        return 'Pena que já acabou...'
