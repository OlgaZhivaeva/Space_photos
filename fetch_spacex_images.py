import argparse
import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from fetch_helper import get_file_extension, fetch_and_save


def get_launch_id():
    """Получить ID запуска из командной строки."""
    parser = argparse.ArgumentParser(description='Фотографии запусков SpaceX')
    parser.add_argument('-l', '--launch_id', default='latest', help='ID запуска')
    args = parser.parse_args()
    return args.launch_id


def get_spacex_images():
    """"Получить картинки SpaceX."""
    load_dotenv()
    dir_name = os.getenv('IMAGES_DIR_PATH', 'images')

    launch_id = get_launch_id()
    url_to_images = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    Path(dir_name).mkdir(parents=True, exist_ok=True)

    response_images = requests.get(url_to_images)
    response_images.raise_for_status()
    url_image_list = response_images.json()['links']['flickr']['original']

    for url_number, url_image in enumerate(url_image_list, 1):
        file_extension = get_file_extension(url_image)
        path_image = Path(dir_name, f'spacex_{url_number}{file_extension}')
        fetch_and_save(url_image, path_image)


if __name__ == "__main__":
    get_spacex_images()
