import argparse
import os
import random
import telegram
from dotenv import load_dotenv
from pathlib import Path
from fetch_helper import send_document, get_all_images


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
        if os.path.isdir(dir_name):
            images = get_all_images(dir_name)
            path_to_photo = Path(dir_name, random.choice(images))
            send_document(path_to_photo)
        else:
            print('There is no catalog with photos. Upload photos.')
    else:
        if os.path.isfile(path_to_photo):
            send_document(path_to_photo)
        else:
            print('The file does not exist. Specify the correct file path.')


if __name__ == "__main__":
    main()
