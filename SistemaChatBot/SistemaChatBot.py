from Bots.Bot import Bot
from abc import ABC
import textwrap as tw





class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa=nomeEmpresa
        for bot in lista_bots:
            if not isinstance(bot, Bot):
                return 'Lista invalida'
        self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        return('Seja bem-vindo ao FiveBots!')

    def mostra_menu(self):
        return("Os bots disponíveis no momento são: ")
    
    def favor_escolher(self):
        return("Favor escolher um digitando o número!")
    
    def mostra_bots(self):
        bots = ""
        for pos, val in enumerate(self.__lista_bots):
            bots = bots + (f'\n{pos+1} - {val.nome }')
        return bots


    def mostra_comandos_bot(self):
        for comando in self.__bot.comandos:
            print(f'{comando.id} - {comando.mensagem}')
        #for i in self.__bot.comandos:
         #   comando = self.__bot.comandos[i]['comando']
          #  print(f'{i} - {comando}')

    def le_envia_comando(self):
        pass

    @property
    def bot(self):
        return self.__bot

    def responder(self, num_msg, mensagem_user):
        if num_msg == 1:
            return (self.boas_vindas() + ' ' + self.mostra_menu() + self.mostra_bots() + "\n" + self.favor_escolher())
        
        try:
            return self.__bot.executa_comando(mensagem_user)
        
        except AttributeError:
            try:
                self.__bot = self.__lista_bots[int(mensagem_user)-1]
                return (self.__bot.apresentacao() + ' ' + self.__bot.boas_vindas())

            except ValueError:
                return "Caractere inválido - favor digitar 1, 2 ou 3."

    def formatado(self, num_msg, mensagem_user):
        return tw.fill(self.responder(num_msg, mensagem_user), 77, replace_whitespace=False)
    
    def botRemove(self):
        self.__bot = None
    


