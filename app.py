#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotAmigavel import BotAmigavel
from Bots.BotFitness import BotFitness

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Docinho"), BotAmigavel("Florzinha"), BotFitness("Lindinha")]

sys = scb.SistemaChatBot("Fivebots", lista_bots)
sys.inicio()