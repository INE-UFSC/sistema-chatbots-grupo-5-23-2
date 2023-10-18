
import PySimpleGUI as psg
import textwrap as tw
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado
from Bots.BotAmigavel import BotAmigavel
from Bots.BotFitness import BotFitness



lista_bots = [BotZangado("Docinho"), BotAmigavel("Florzinha"), BotFitness("Lindinha")]

sys = scb.SistemaChatBot("Fivebots", lista_bots)






#predefinicoes
number_msg = 0
cor_selecionada = "#083C6B"
mensagem_automatica_pre = "está funcionando perfeitamente agora (aparentemente)! Seria bom dar uma testada extra mas acho que assim dá para o gasto, portanto estarei encerrando o meu trabalho aqui por hoje. Por hoje é só pessoal! e, lembrem-se sempre, evangellion é PEAK"
nome_bot = "Bot:   "
psg.theme('DarkBlue14')
restart = True
active = False
ja_somou = False
deleted = []
conversation_column =[[]]
mensagem_automatica = tw.fill(mensagem_automatica_pre, 75)




#layout
layout = [[psg.Text("\nConverse com seu chatbot favorito! (comece falando qualquer coisa)\n", background_color="#083C6B")],
          [psg.Column(conversation_column, key="coluna", scrollable=True, vertical_scroll_only = True,
                       size=(430, 432))],
          [psg.Input(default_text="", key='-enviado-', do_not_clear=False), psg.Button("Enviar", key='-mensagem_enviar-', bind_return_key=True),
            psg.Button("Reset", key = '-reset-')],
          [psg.Button("Fechar", key ='-fechar_app-'), psg.Button("Ajuda", key = '-help-')]]

#window
window = psg.Window("Fivebots", layout, size=(470,550), background_color=cor_selecionada)

#event loop
while restart:
    restart = False

    while True:
        event, values = window.read()

        if event == psg.WIN_CLOSED or event=='-fechar_app-':
            break
        elif event == '-mensagem_enviar-':

            if active:
                number_msg += 1
                ja_somou = True
            if number_msg in deleted:
                if not active:
                    number_msg = 1
                    active = True

                window[f'user{number_msg}'].update("Você:")
                window[f"message_user_number{number_msg}"].update(values['-enviado-'])
                window[f'bot{number_msg}'].update("Bot:  ")
                window[f'message_bot_number{number_msg}'].update(sys.formatado(number_msg, values['-enviado-']))

            else:
                active = False

                if not ja_somou:
                    number_msg += 1
                ja_somou = False


                window.extend_layout(
                    window['coluna'],[[psg.Text("Você:", key=f'user{number_msg}'), psg.Text(values['-enviado-'], 
                                                key=f"message_user_number{number_msg}")]]
                )
                window.extend_layout(
                        window['coluna'], [[psg.Text(nome_bot, text_color="#167DE5", key=f'bot{number_msg}'),
                        psg.Text(sys.formatado(number_msg, values['-enviado-']), key=f'message_bot_number{number_msg}')]]
                    )

            window.refresh()
            window.visibility_changed()
            window['coluna'].contents_changed()

        elif event == '-reset-':
            for i in range(number_msg):
                if (i+1) not in deleted:
                    deleted.append(i+1)
                window[f'message_user_number{i+1}'].update("")
                window[f'user{i+1}'].update("")
                window[f'message_bot_number{i+1}'].update("")
                window[f'bot{i+1}'].update("")
            active = False
            sys.botRemove()

        
        elif event == '-help-':
            window['oi'].update(visible=False)
    window.close()

















#README - features
#auto-apaga input depois de enviar; botão enter envia mensagens automaticamente; input já vem selecionado
#automaticamente; botão de ajuda (ajuda não feita ainda); mecanismo de quebra de linhas; reset assíncrono.


