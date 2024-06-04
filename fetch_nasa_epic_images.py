import datetime
import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from fetch_helper import fetch_and_save, get_count_of_images


def main():
    """Получить эпичные картинки Nasa."""
    load_dotenv()
    nasa_api_key = os.environ["NASA_API_KEY"]
    dir_name = os.getenv('IMAGES_DIR_PATH', 'images')
    try:
        count = get_count_of_images()
    except TypeError():
        count = 10

    payload = {
        'api_key': nasa_api_key
    }

    url_to_photos_info = "https://api.nasa.gov/EPIC/api/natural"
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    photos_info = requests.get(url_to_photos_info, params=payload)
    photos_info.raise_for_status()

    for photo_number, photo in enumerate(photos_info.json()[:count], 1):
        creation_date = datetime.datetime.fromisoformat(photo['date']).strftime("%Y/%m/%d")
        image_name = photo['image']
        url_image = f'https://api.nasa.gov/EPIC/archive/natural/{creation_date}/png/{image_name}.png'
        path_image = Path(dir_name, f'nasa_epic_{photo_number}.png')
        fetch_and_save(url_image, path_image, payload)


if __name__ == "__main__":
    main()
