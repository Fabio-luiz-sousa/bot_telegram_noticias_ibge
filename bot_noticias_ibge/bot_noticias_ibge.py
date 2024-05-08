from telegram import Update #type: ignore
from telegram.ext import Application, CommandHandler, MessageHandler,filters,ContextTypes  # type: ignore
import os
import dotenv #type: ignore
import logging
import sys
sys.path.append('./insert_info_db/')
from select_info import select_info_news


dotenv.load_dotenv()

TOKEN = os.environ['TOKEN']

BOT_USERNAME = '@noticias_ibge_2024_bot'



# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Commands
async def start_command(update: Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Olá! Quais notícias você quer ler ?\nDe hoje - digite 1\nDa semana - digite 2')

async def help_command(update: Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Qual ajuda você está precisando ?\n'
                                    'Sobre o projeto - digite sobre')


#Responses
def handle_response(text:str)->str:
    if '1' == text:
        return select_info_news(text)
    elif '2' == text:
        return select_info_news(text)
    elif 'sobre' == text:
        return f'Repositório do projeto: \nApi do IBGE: https://servicodados.ibge.gov.br/api/docs/noticias?versao=3#api-_'
    
async def handle_message(update: Update,context:ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME,'').strip()
            response = handle_response(new_text)
        else:
            return
    else:
        response = handle_response(text)
    print('Bot:',response)
    await update.message.reply_text(response)


print('Starting bot ...')
app = Application.builder().token(TOKEN).build()

# Commands
app.add_handler(CommandHandler('start',start_command))
app.add_handler(CommandHandler('help',help_command))

# Messages
app.add_handler(MessageHandler(filters.TEXT,handle_message))


# Polls the bot
print('Polling...')
app.run_polling(poll_interval=5)