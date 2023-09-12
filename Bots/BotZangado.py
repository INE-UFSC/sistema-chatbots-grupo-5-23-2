from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,  nome):
        self.__nome = nome
        self.__comandos = {
            1: {
                'comando': 'Bom dia',
                'resposta': 'Bom dia é o ...'
            },
            2: {
                'comando': 'Conte uma piada',
                'resposta': 'O que é, o que é que tem quatro bocas mas não fala? \nCom certeza não é sua mãe!'
            },
            3: {
                'comando': 'Quero um conselho',
                'resposta': 'KKKKK. Não sou psicólogo.'
            }
        }

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        print(f'-> Olá, sou o {self.__nome}! Desprazer em conhecê-lo!')
 
    def mostra_comandos(self):
        for i in self.__comandos:
            comando = self.__comandos[i]['comando']
            print(f'{i} - {comando}')
    
    def executa_comando(self, cmd):
        print(self.__comandos[cmd]['resposta'])

    def boas_vindas(self):
        print(f'-> {self.__nome} diz: Grande porcaria. Podia ter escolhido outro.')

    def despedida(self):
        print('Espero nunca mais te ver.')