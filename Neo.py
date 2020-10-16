import telebot

TOKEN = "1348439222:AAHp9D8pIAUC4_7nqnOYQfhjhsWEmnBikIQ"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])
def start(message):
    print(message)
    print(message.chat.id)
    chat_id = message.chat.id
    bot.send_message(chat_id, "HELLO")


bot.polling(none_stop=True)  # Запускает бота

print("dsf")

