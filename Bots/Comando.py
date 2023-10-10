import random

class Comando:
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, id: int, mensagem: str, respostas = []):
        self.__id = id
        self.__mensagem = mensagem
        self.__respostas = respostas

    @property
    def id(self):
        return self.__id
    
    @property
    def mensagem(self):
        return self.__mensagem

    def getRandomResposta(self):
        resposta_aleatoria = random.choice(self.__respostas)
        return resposta_aleatoria

    def addResposta(self, resposta):
        if isinstance(resposta, str):
            self.__respostas.append(resposta)
        else:
            return 'Parâmetro inválido. Digite em formato de texto.'

    def delResposta(self, resposta):
        if resposta in self.__respostas:
            self.__respostas.pop(resposta)
        else:
            return 'Resposta não cadastrada.'
