import argparse
import requests
from pathlib import Path
from fetch_helper import get_file_extension, fetch_and_save


def get_launch_id():
    """Функция для получения ID запуска из командной строки"""
    parser = argparse.ArgumentParser(description='Фотографии запусков SpaceX')
    parser.add_argument('-l', '--launch_id', default='latest', help='ID запуска')
    args = parser.parse_args()
    return args.launch_id


def spacex():
    """" Функция для получения картинок spacex """
    launch_id = get_launch_id()
    url_to_images = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    dir_name = 'images'
    Path(dir_name).mkdir(parents=True, exist_ok=True)

    response = requests.get(url_to_images)
    response.raise_for_status()
    url_image_list = response.json()['links']['flickr']['original']

    for url_number, url_image in enumerate(url_image_list, 1):
        file_extension = get_file_extension(url_image)
        path_image = f'{dir_name}/spacex_{url_number}{file_extension}'
        print(url_image)
        fetch_and_save(url_image, path_image)


if __name__ == "__main__":
    spacex()
