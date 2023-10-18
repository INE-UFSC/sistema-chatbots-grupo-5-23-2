from .Bot import Bot
from .Comando import Comando


class BotZangado(Bot):
    def __init__(self,  nome):
        self.__nome = nome
        self.__comandos = [Comando(1, 'Bom dia', ['Bom dia é o ...']), 
                           Comando(2, 'Conte uma piada', ['O que é, o que é que tem quatro bocas mas não fala? Com certeza não é sua mãe!']), 
                           Comando(3, 'Quero um conselho', ['KKKKK. Não sou psicólogo.'])]
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
        return(f'Olá, sou o {self.__nome}! Desprazer em conhecê-lo!')
 
    def mostra_comandos(self):
        for comando in self.__comandos:
            print(f'{comando.id} - {comando.mensagem}')
            #Substituido para lógica com atributos da classe Comando

    def executa_comando(self, id):
        for comando in (self.__comandos):
            if comando.id == id or comando.mensagem == id:
                return str(comando.getRandomResposta())
        return "Comando inexistente bobão!!"

    

    def boas_vindas(self):
        return f'Grande porcaria, podia ter escolhido outro.'

    def despedida(self):
        return 'Espero nunca mais te ver.'