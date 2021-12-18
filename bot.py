import telebot
import settings
from utils import Logger


class Bot:
    HANDLERS = {
        "Привет": None,
        "Изменить": None
    }

    def __init__(self):
        self.env = settings.env
        self.TOKEN = self.env.TOKEN
        self.bot = telebot.TeleBot(self.TOKEN)
        self.logger = Logger('bot_logger')

    def listen(self):
        self.bot.set_update_listener(self.receive)
        self.logger.add('Listening successfully started')
        self.bot.polling()

    def receive(self, messages: list):
        message_text, chat_id = messages[0].text, messages[0].chat.id
        if message_text.lower() in [key.lower() for key in self.HANDLERS.keys()]:
            self.bot.send_message(chat_id, message_text)

    def send(self, message: str, chat_id: int):
        self.bot.send_message(chat_id, message)
