from .Bot import Bot
from .Comando import Comando


#Docinho
class BotZangado(Bot):
    def __init__(self,  nome):
        self.__nome = nome
        self.__comandos = [Comando('Bom dia', ['Bom dia é o ...']), 
                           Comando('Conte uma piada', ['O que é, o que é que tem quatro bocas mas não fala? \nCom certeza não é sua mãe!']), 
                           Comando('Quero um conselho', ['KKKKK. Não sou psicólogo.'])]
                        #Dicionário substituido por lista de objetos

    @property
    def nome(self):
        return self.__nome

    @property
    def comandos(self):
        return self.__comandos
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return(f'Olá, sou o {self.__nome}! Desprazer em conhecê-lo!\n')
 
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
            return 'Comando inexistente bobão!!'
            #Tava com um return de comando inexistente aqui que rodaria anyways, coloquei uma flag para verificar se ele encontrou resposta

    def boas_vindas(self):
        return 'Grande porcaria, podia ter escolhido outro.'

    def despedida(self):
        return 'Espero nunca mais te ver.'