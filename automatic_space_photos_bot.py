import os
import random
import telegram
import time
from dotenv import load_dotenv
from pathlib import Path
from fetch_helper import send_document, get_all_images


def main():
    load_dotenv()
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]
    post_frequency = os.getenv('POST_FREQUENСY', 14400)
    dir_name = os.getenv('IMAGES_DIR_PATH', 'images')

    bot = telegram.Bot(token=telegram_token)

    if not os.path.isdir(dir_name):
        print('There is no catalog with photos. Upload photos.')
        return
    image_names = get_all_images(dir_name)

    while True:
        random.shuffle(image_names)
        for name in image_names:
            send_document(bot, tg_chat_id, Path(dir_name, name))
            time.sleep(int(post_frequency))


if __name__ == "__main__":
    main()
