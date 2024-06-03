import argparse
import os
import random
import telegram
from dotenv import load_dotenv
from pathlib import Path


def get_path_to_photo():
    """Получить путь до фотографии из командной строки"""
    parser = argparse.ArgumentParser(description='Публикация фотографий космоса')
    parser.add_argument('-p', '--path_to_photo', help='Путь до фотографии')
    args = parser.parse_args()
    return args.path_to_photo


def main():
    load_dotenv()
    TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
    TG_CHAT_ID = os.environ["TG_CHAT_ID"]
    dir_name = os.getenv('IMAGES_DIR_PATH', 'images')

    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    path_to_photo = get_path_to_photo()

    if path_to_photo is None:
        if os.path.isdir('images'):
            _, _, image_list = list(os.walk('images'))[0]
            path_to_photo = Path(dir_name, random.choice(image_list))
            bot.send_document(chat_id=TG_CHAT_ID, document=open(path_to_photo, 'rb'))
        else:
            print('There is no catalog with photos. Upload photos.')
    else:
        if os.path.isfile(path_to_photo):
            with open(path_to_photo, 'rb') as path:
                bot.send_document(chat_id=TG_CHAT_ID, document=path)
        else:
            print('The file does not exist. Specify the correct file path.')


if __name__ == "__main__":
    main()
