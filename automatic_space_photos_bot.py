import os
import random
import telegram
import time
from dotenv import load_dotenv
from pathlib import Path


def main():
    load_dotenv()
    TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
    TG_CHAT_ID = os.environ["TG_CHAT_ID"]
    post_frequency = os.getenv('POST_FREQUENСY', 14400)
    dir_name = os.getenv('IMAGES_DIR_PATH', 'images')

    bot = telegram.Bot(token=TELEGRAM_TOKEN)

    if os.path.isdir(dir_name):
        _, _, image_names = list(os.walk(dir_name))[0]

        while True:
            random.shuffle(image_names)
            for name in image_names:
                with open(Path(dir_name, name), 'rb') as image:
                    try:
                       bot.send_document(chat_id=TG_CHAT_ID, document=image)
                    except telegram.error.NetworkError('No internet connection'):
                        try:
                            bot.send_document(chat_id=TG_CHAT_ID, document=image)
                        except telegram.error.NetworkError('No internet connection'):
                            time.sleep(20)
                time.sleep(int(post_frequency))

    else:
        print('There is no catalog with photos. Upload photos.')


if __name__ == "__main__":
    main()
