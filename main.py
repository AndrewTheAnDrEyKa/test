import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Устанавливаем уровень логирования (не обязательно, но полезно)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Этот обработчик будет вызываться при команде /start
def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Привет! Я бот. Чтобы узнать больше обо мне, используй команду /info')
    return ConversationHandler.END

# Этот обработчик будет вызываться при команде /info
def info(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Привет! Я - программист, обожающий пёсиков и пирожные с корицей. Я создал этого бота, чтобы помогать вам с разными задачами и отвечать на вопросы. Если у вас есть какие-либо вопросы или запросы, не стесняйтесь писать мне!')
    return ConversationHandler.END

# Главная функция
def main() -> None:
    # Замените '6576505998:AAF16kkS5WILGDNRhk9HaMMdz8AbZf9tgjU' на ваш токен бота
    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

    dispatcher = updater.dispatcher

    # Добавляем обработчики команд
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('info', info))

    # Запускаем бота
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
