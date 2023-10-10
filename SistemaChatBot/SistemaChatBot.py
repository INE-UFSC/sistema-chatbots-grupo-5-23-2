from Bots.Bot import Bot
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
        print('Seja bem-vindo ao FiveBots!')

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
            except IndexError:
                print('Bot inválido! Escolha novamente')

    def mostra_comandos_bot(self):
        for comando in self.__bot.comandos:
            print(f'{comando.id} - {comando.mensagem}')
        #for i in self.__bot.comandos:
         #   comando = self.__bot.comandos[i]['comando']
          #  print(f'{i} - {comando}')

    def le_envia_comando(self):
        pass

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        print(self.__bot.boas_vindas())
        while True:
            self.mostra_comandos_bot()
            cmd = int(input())
            if cmd == -1:
                print(self.__bot.despedida())
                break
            comando = self.__bot.executa_comando(cmd)
            print(comando)
