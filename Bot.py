import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.remote.webdriver import By
from time import sleep
import requests

driver = uc.Chrome()
driver.get('https://blaze.com/pt/games/double')
sleep(5)

# Mensagens Padrao
analise = 'Analisando possivel entrada...'
win = 'Winzada 🟩'
win_branco = '⬜ Winzada no branco ⬜'
loss = 'Infelizmanete não foi dessa vez ❌\nPare por um momento e volte mais tarde'
nao_confirmacao = 'Não confirmou Entrada \nAguarde o próximo sinal'


##############################

def esperar():
    while True:
        try:
            driver.find_element(By.CLASS_NAME, 'time-left').find_element(By.TAG_NAME, 'span').text
            break
        except:
            pass

    while True:
        try:
            driver.find_element(By.CLASS_NAME, 'time-left').find_element(By.TAG_NAME, 'span').text
        except:
            break


def retornar_historico():
    return [i['color'] for i in requests.get('https://blaze.com/api/roulette_games/recent').json()][::-1]


def retornar_ultimo():
    return requests.get('https://blaze.com/api/roulette_games/current').json()['color']


def martin_gale(gale, ultimo):
    enviar_mensagem(gale)
    esperar()
    sleep(1.5)
    ultimo_ = retornar_ultimo()
    if ultimo_ != ultimo and ultimo_ != 0:
        enviar_mensagem(win)
        return True
    elif ultimo_ == 0:
        enviar_mensagem(win_branco)
        return True


def enviar_mensagem(mensagem):
    bot_token = '6154063307:AAHp_1V0rr6VMuR_lErciT462lXGCJGYNGo'
    chat_id = '-1001954814927'
    url_blaze = '🎰 [Blaze](https://blaze.com/pt/games/double)'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={mensagem}\n{url_blaze}&parse_mode=Markdown'
    requests.get(url)


cor = ['Branco', 'Preto', 'Vermelho']
simbolo = ['⬜', '⬛', '🟥']

print('Bot do negão inicado ...')
enviar_mensagem('Bot do negão iniciado ...')
while True:
    try:
        print('OK')
        esperar()
        sleep(1.5)
        historico = retornar_historico()
        ultimo = retornar_ultimo()
        historico.append(ultimo)
        padrao = historico[-4:]
        print(padrao)
        confirmacao = f'{simbolo[padrao[0]]} Entrada confirmada no {cor[padrao[0]]}\n{simbolo[0]} Proteção no branco' #Depois testar trocar os 0 por 1
        gale1 = f'Vamos para o gale 1 \n{simbolo[padrao[0]]} {cor[padrao[0]]}\n{simbolo[0]} Proteção no Branco'
        gale2 = f'Cuidado! Vamos para o gale 2 \n{simbolo[padrao[0]]} {cor[padrao[0]]}\n{simbolo[0]} Proteção no Branco'

        # Como as estratégias sempre jogam na cor contraria, resolvi colocar as cores
        # Vermelha e Preta em indices diferentes para aproveirar a logica
        if padrao == [1, 1, 1, 1] or padrao == [2, 2, 2, 2] or padrao == [1, 2, 1, 2] or padrao == [2, 1, 2, 1] or padrao == [2, 2, 1, 1] or padrao == [1, 1, 2, 2] or padrao == [1, 1, 1, 2] or padrao == [2, 2, 2, 1] or padrao == [2, 2, 1, 2] or padrao == [1, 1, 2, 1]:
            enviar_mensagem(analise)
            esperar()
            sleep(1.5)
            ultimo = retornar_ultimo()
            while True:
                if ultimo == padrao[0]:
                    enviar_mensagem(confirmacao)
                    esperar()
                    sleep(1.5)
                    ultimo_ = retornar_ultimo()
                    if ultimo_ != ultimo and ultimo_ != 0:
                        enviar_mensagem(win)
                        break
                    elif ultimo_ == 0:
                        enviar_mensagem(win_branco)
                        break
                    else:
                        if martin_gale(gale1, ultimo):
                            break
                        else:
                            if martin_gale(gale2, ultimo):
                                break
                            else:
                                enviar_mensagem(loss)
                                break

                else:
                    enviar_mensagem(nao_confirmacao)
                    break
    except Exception as e:
        print(e)
        driver.get('https://blaze.com/pt/games/double')
        sleep(10)
        pass
