import argparse
import os
import requests
import telegram
from dotenv import load_dotenv
from os.path import splitext
from os.path import split
from urllib.parse import urlparse
from urllib.parse import unquote


def get_file_extension(image_url):
    """Получить расширение файла из адреса."""
    parsed_url = urlparse(image_url)
    decoded_url = unquote(parsed_url.path, encoding='utf-8', errors='replace')
    (_, parsed_file) = split(decoded_url)
    (_, file_extension) = splitext(parsed_file)
    return file_extension


def fetch_and_save(url_image, path_image, params=None):
    """Скачать картинку по указанному адресу и записать по указанному пути."""
    response = requests.get(url_image, params=params)
    response.raise_for_status()
    with open(path_image, 'wb') as file:
        file.write(response.content)


def get_count_of_images():
    """Получить количество изображений из командной строки."""
    parser = argparse.ArgumentParser(description='Скачивание фотографий Nasa')
    parser.add_argument('-c', '--count', type=int, default=10, help='Количество фотографий для скачивания')
    args = parser.parse_args()
    return args.count


def send_document(path_to_image):
    """Опубликовать картинку."""
    load_dotenv()
    telegram_token = os.environ["TELEGRAM_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]
    bot = telegram.Bot(token=telegram_token)

    with open(path_to_image, 'rb') as image:
        bot.send_document(chat_id=tg_chat_id, document=image)

def get_all_images(path_to_dir):
    """Получить все картинки из папки"""
    _, _, images = list(os.walk(path_to_dir))[0]
    return images
