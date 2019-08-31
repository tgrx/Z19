import telebot
from telebot import types

token = "550640345:AAGJ4ahUBiono_q7pZ_rzZyhNSZZBgu2NPs"

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == "__main__":
    bot.polling(none_stop=True)

markup = types.ReplyKeyboardMarkup()
markup.row("a", "v")
markup.row("c", "d", "e")
bot.send_message(repeat_all_messages.chat.id, "choose one letter:", reply_markup=markup)
