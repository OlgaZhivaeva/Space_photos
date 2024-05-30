import argparse
import os
import random
import telegram
from dotenv import load_dotenv


load_dotenv()
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
ID_CHAT = os.environ["ID_CHAT"]
POST_FREQUENSY = os.getenv('POST_FREQUENSY', 14400)


def get_path_to_photo():
    """Функция для получения пути до фотографии из командной строки"""
    parser = argparse.ArgumentParser(description='Публикация фотографий космоса')
    parser.add_argument('-p', '--path_to_photo', help='Путь до фотографии')
    args = parser.parse_args()
    return args.path_to_photo


def main():
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    path_to_photo = get_path_to_photo()

    if path_to_photo is None:
        if os.path.isdir('images'):
            _, _, image_list = list(os.walk('images'))[0]
            path_to_photo = f'images/{random.choice(image_list)}'
            bot.send_document(chat_id=ID_CHAT, document=open(path_to_photo, 'rb'))
        else:
            print('There is no catalog with photos. Upload photos.')
    else:
        if os.path.isfile(path_to_photo):
            bot.send_document(chat_id=ID_CHAT, document=open(path_to_photo, 'rb'))
        else:
            print('The file does not exist. Specify the correct file path.')


if __name__ == "__main__":
    main()
