import os
import random
import time
from dotenv import load_dotenv
import telegram

load_dotenv()
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
ID_CHAT = os.environ["ID_CHAT"]
post_frequency = os.getenv('POST_FREQUENSY', 14400)


def main():
    bot = telegram.Bot(token=TELEGRAM_TOKEN)

    if os.path.isdir('images'):
        _, _, image_list = list(os.walk('images'))[0]

        while True:
            random.shuffle(image_list)
            for image in image_list:
                bot.send_document(chat_id="@space_and_space", document=open(f'images/{image}', 'rb'))
                time.sleep(int(post_frequency))

    else:
        print('There is no catalog with photos. Upload photos.')


if __name__ == "__main__":
    main()
