import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from fetch_helper import get_file_extension, fetch_and_save


load_dotenv()
API_KEY = os.environ["API_KEY"]


def nasa_apod():
    """" Функция для получения картинок дня Nasa """
    payload = {
        'api_key': API_KEY,
        'count': 3
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


if __name__ == "__main__":
    nasa_apod()
