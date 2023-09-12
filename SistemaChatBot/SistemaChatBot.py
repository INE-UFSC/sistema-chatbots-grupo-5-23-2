from Bots.Bot import Bot
from Bots.BotZangado import BotZangado
from abc import ABC

class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa=nomeEmpresa
        for bot in lista_bots:
            if not isinstance(bot, Bot):
                return 'Lista invalida'
        self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        print('Seja bem-vindo ao FiveBot!')

    def mostra_menu(self):
        print('Os chat bots disponíveis no momento são: ')
        for pos, val in enumerate(self.__lista_bots):
            print(f'{pos+1} - {val.nome }')

    def escolhe_bot(self):
        while True:
            try:
                escolha = int(input('Digite o número do chat bot desejado: '))
                self.__bot = self.__lista_bots[escolha-1]
                break
            except [TypeError, IndexError]:
                print('Bot inválido! Escolha novamente')

    def mostra_comandos_bot(self):
        for i in self.__bot.comando:
            print(f'{i} - {self.__bot.comando[i]}')

    def le_envia_comando(self):
        pass

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        self.__bot.boas_vindas()
        while True:
            self.__bot.mostra_comandos()
            cmd = int(input())
            if cmd == -1:
                self.__bot.despedida()
                break
            self.__bot.executa_comando(cmd)
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot

