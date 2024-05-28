import requests
from os.path import splitext
from os.path import split
from urllib.parse import urlparse
from urllib.parse import unquote


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
    with open(path_image, 'wb') as file:
        file.write(response.content)
