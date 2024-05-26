import datetime
import os
import requests
from dotenv import load_dotenv
from os.path import splitext
from os.path import split
from pathlib import Path
from urllib.parse import urlparse
from urllib.parse import unquote


load_dotenv()
API_KEY = os.environ["API_KEY"]


def get_file_extension(url_image):
    """ Функция получает расширение файла из адреса """
    parse_url = urlparse(url_image)
    (_, parse_file) = split(unquote(parse_url.path, encoding='utf-8', errors='replace'))
    (_, file_extension) = splitext(parse_file)
    return file_extension


def fetch_and_save(url_image, path_image, params=None):
    """ Функция скачивает картинку по указанному адресу и записывает по указанному пути"""
    response = requests.get(url_image, params=params)
    response.raise_for_status()
    # with open(path_image, 'wb') as file:
    #     file.write(response.content)
    print(url_image, path_image)


def spacex():
    """" Функция для получения картинок spacex """
    url_to_images = f'https://api.spacexdata.com/v5/launches/latest'
    dir_name = 'images'
    Path(dir_name).mkdir(parents=True, exist_ok=True)

    response = requests.get(url_to_images)
    response.raise_for_status()
    url_image_list = response.json()['links']['flickr']['original']

    for url_number, url_image in enumerate(url_image_list, 1):
        file_extension = get_file_extension(url_image)
        path_image = f'{dir_name}/spacex_{url_number}{file_extension}'
        fetch_and_save(url_image, path_image)


def nasa_apod():
    """" Функция для получения картинок дня Nasa """
    payload = {
        'api_key': API_KEY,
        'count': 25
    }
    url_to_images = "https://api.nasa.gov/planetary/apod"
    dir_name = 'images_apod'
    Path(dir_name).mkdir(parents=True, exist_ok=True)

    response = requests.get(url_to_images, params=payload)
    response.raise_for_status()
    url_image_list = response.json()

    for url_number, image in enumerate(url_image_list, 1):
        url_image = image['url']
        file_extension = get_file_extension(url_image)
        path_image = f'{dir_name}/nasa_apod_{url_number}{file_extension}'
        fetch_and_save(url_image, path_image)


def nasa_epic():
    """" Функция для получения эпичных картинок Nasa """
    payload = {
        'api_key': API_KEY
    }

    url_to_photo_info = "https://api.nasa.gov/EPIC/api/natural"
    dir_name = 'images_epic'
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    photos_info = requests.get(url_to_photo_info, params=payload)

    for photo_number, photo in enumerate(photos_info.json(), 1):
        creation_date = datetime.datetime.fromisoformat(photo['date']).strftime("%Y/%m/%d")
        image_name = photo['image']
        url_image = f'https://api.nasa.gov/EPIC/archive/natural/{creation_date}/png/{image_name}.png'
        path_image = f'{dir_name}/nasa_epic_{photo_number}.png'
        fetch_and_save(url_image, path_image, payload)


if __name__ == "__main__":
    spacex()
    nasa_apod()
    nasa_epic()
