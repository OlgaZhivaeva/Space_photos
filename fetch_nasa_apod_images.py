import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from fetch_helper import get_file_extension, fetch_and_save, get_count_of_images


def get_nasa_apod_images():
    """"Получить картинки дня Nasa."""
    load_dotenv()
    NASA_API_KEY = os.environ["NASA_API_KEY"]
    dir_name = os.getenv('IMAGES_DIR_PATH', 'images')
    try:
        count = int(get_count_of_images())
    except:
        count = 10

    payload = {
        'api_key': NASA_API_KEY,
        'count': count
    }

    url_to_images = "https://api.nasa.gov/planetary/apod"
    Path(dir_name).mkdir(parents=True, exist_ok=True)

    response_images = requests.get(url_to_images, params=payload)
    response_images.raise_for_status()
    url_images = response_images.json()

    for url_number, image in enumerate(url_images, 1):
        if image['media_type'] == 'image':
            url_image = image['url']
            file_extension = get_file_extension(url_image)
            path_image = Path(dir_name, f'nasa_apod_{url_number}{file_extension}')
            fetch_and_save(url_image, path_image)


if __name__ == "__main__":
    get_nasa_apod_images()
