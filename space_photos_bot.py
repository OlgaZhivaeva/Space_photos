import os
from dotenv import load_dotenv
import telegram


load_dotenv()
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

bot = telegram.Bot(token=TELEGRAM_TOKEN)
print(bot.get_me())

bot.send_message(chat_id="@dvmn_flood", text="Hi! I'm a bot. I can download photos of space from the Internet.")
