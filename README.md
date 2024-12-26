# Bot de Previsões para Blaze via Telegram

Este projeto é um bot totalmente desenvolvido em **Python** que utiliza uma **API aberta da Blaze**, uma plataforma de apostas online, para auxiliar usuários com previsões baseadas em seus próprios palpites.

---

## Funcionalidades

- 🔮 **Previsões Baseadas em Palpites**: O bot utiliza os palpites fornecidos pelos usuários para calcular e exibir as próximas entradas na Blaze.
- 📲 **Notificações via Telegram**: Envia mensagens diretamente no Telegram indicando:
  - A próxima entrada.
  - A cor prevista para a aposta.
- 🎯 **Suporte ao Gale 1**: Implementa a estratégia de **Gale 1**, caso a primeira previsão não seja assertiva.

---

## Tecnologias Utilizadas

O bot foi desenvolvido em **Python** e faz uso das seguintes ferramentas e bibliotecas:

- **Telegram Bot API**: Para comunicação e notificações no Telegram.
- **API aberta da Blaze**: Para obter os dados necessários da plataforma de apostas.
- **Requests**: Para realizar requisições à API.
- **Datetime**: Para gerenciar horários das entradas.

---

## Como Funciona

1. **Conexão com a API da Blaze**: O bot se conecta à API aberta da Blaze para obter dados em tempo real.
2. **Processamento dos Palpites**: Os usuários fornecem seus palpites, e o bot calcula a próxima entrada com base nas tendências detectadas.
3. **Notificação no Telegram**: O bot envia uma mensagem no Telegram indicando a próxima aposta, a cor prevista e, caso necessário, sugere a estratégia Gale 1.
4. **Automatização e Precisão**: O sistema é otimizado para minimizar erros e oferecer um suporte confiável aos usuários.

---

## Requisitos

Para executar o bot, você precisará de:

- Python 3.8 ou superior.
- Bibliotecas necessárias: `python-telegram-bot`, `requests`, `datetime`.
- Token do Telegram Bot API (obtido ao criar um bot via [BotFather](https://core.telegram.org/bots#botfather)).
- Acesso à API aberta da Blaze.

---

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Anthony17DEV/BotBlaze.git
   cd seuprojeto
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure seu arquivo de ambiente:
   - Adicione o token do Telegram e as credenciais da API da Blaze no arquivo `.env` (se aplicável).
4. Inicie o bot:
   ```bash
   python bot.py
   ```
5. Interaja com o bot no Telegram e envie seus palpites para começar a receber notificações.

---

## Status do Projeto

O projeto está funcional e em uso, mas melhorias contínuas podem ser feitas para aumentar a precisão das previsões e implementar estratégias adicionais.

---

# Blaze Prediction Bot via Telegram

This project is a bot entirely developed in **Python** that leverages an **open Blaze API**, an online betting platform, to assist users with predictions based on their own guesses.

---

## Features

- 🔮 **Prediction Based on Guesses**: The bot uses user-provided guesses to calculate and display the next entries on Blaze.
- 📲 **Telegram Notifications**: Sends messages directly on Telegram, indicating:
  - The next entry.
  - The predicted color.
- 🎯 **Gale 1 Strategy Support**: Implements the **Gale 1 strategy** in case the first prediction is not successful.

---

## Technologies Used

The bot is built with **Python** and utilizes the following tools and libraries:

- **Telegram Bot API**: For communication and notifications on Telegram.
- **Open Blaze API**: To fetch necessary data from the betting platform.
- **Requests**: For API requests.
- **Datetime**: To manage entry times.

---

## How It Works

1. **Connection to Blaze API**: The bot connects to Blaze's open API to fetch real-time data.
2. **Processing User Guesses**: Users provide their guesses, and the bot calculates the next entry based on detected trends.
3. **Telegram Notification**: The bot sends a message on Telegram indicating the next bet, the predicted color, and, if needed, the Gale 1 strategy.
4. **Automation and Precision**: The system is optimized to minimize errors and provide reliable support to users.

---

## Requirements

To run the bot, you will need:

- Python 3.8 or higher.
- Required libraries: `python-telegram-bot`, `requests`, `datetime`.
- Telegram Bot API token (obtained by creating a bot via [BotFather](https://core.telegram.org/bots#botfather)).
- Access to Blaze's open API.

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/Anthony17DEV/BotBlaze.git
   cd yourproject
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your environment file:
   - Add your Telegram token and Blaze API credentials in the `.env` file (if applicable).
4. Run the bot:
   ```bash
   python bot.py
   ```
5. Interact with the bot on Telegram and send your guesses to start receiving notifications.

---

## Project Status

The project is fully functional and in use, but continuous improvements can be made to enhance prediction accuracy and implement additional strategies.
