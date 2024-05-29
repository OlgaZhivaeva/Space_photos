import os
from dotenv import load_dotenv
import telegram


load_dotenv()
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]

bot = telegram.Bot(token=TELEGRAM_TOKEN)
print(bot.get_me())


bot.send_message(chat_id="@space_and_space", text="Hi! I'm a bot. I can download photos of space from the Internet.")
bot.send_document(chat_id="@space_and_space", document=open('images/spacex_1.jpg', 'rb'))
bot.send_document(chat_id="@space_and_space", document='https://apod.nasa.gov/apod/image/2107/LRVBPIX3M82Crop1024.jpg')
