import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from fetch_helper import get_file_extension, fetch_and_save, get_count_of_images, get_start_count


def main():
    """"Получить картинки дня Nasa."""
    load_dotenv()
    nasa_api_key = os.environ["NASA_API_KEY"]
    dir_name = os.getenv('IMAGES_DIR_PATH', 'images')
    count = get_count_of_images()

    payload = {
        'api_key': nasa_api_key,
        'count': count
    }

    url_to_images = "https://api.nasa.gov/planetary/apod"
    Path(dir_name).mkdir(parents=True, exist_ok=True)

    response_images = requests.get(url_to_images, params=payload)
    response_images.raise_for_status()
    images_urls = response_images.json()
    start_count = get_start_count(dir_name, r'nasa_apod_')

    for url_number, image in enumerate(images_urls, start_count):
        if image['media_type'] == 'image':
            url_image = image['url']
            file_extension = get_file_extension(url_image)
            path_to_image = Path(dir_name, f'nasa_apod_{url_number}{file_extension}')
            fetch_and_save(url_image, path_to_image)


if __name__ == "__main__":
    main()
