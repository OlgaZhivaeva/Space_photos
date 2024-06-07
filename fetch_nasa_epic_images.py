import datetime
import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from fetch_helper import fetch_and_save, get_count_of_images, get_start_count


def main():
    """Получить эпичные картинки Nasa."""
    load_dotenv()
    nasa_api_key = os.environ["NASA_API_KEY"]
    dir_name = os.getenv('IMAGES_DIR_PATH', 'images')
    count = get_count_of_images()

    payload = {
        'api_key': nasa_api_key
    }

    url_to_photos_info = "https://api.nasa.gov/EPIC/api/natural"
    Path(dir_name).mkdir(parents=True, exist_ok=True)
    photos_info = requests.get(url_to_photos_info, params=payload)
    photos_info.raise_for_status()
    start_count = get_start_count(dir_name, r'nasa_epic_')

    for photo_number, photo in enumerate(photos_info.json()[:count], start_count):
        creation_date = datetime.datetime.fromisoformat(photo['date']).strftime("%Y/%m/%d")
        image_name = photo['image']
        url_image = f'https://api.nasa.gov/EPIC/archive/natural/{creation_date}/png/{image_name}.png'
        path_to_image = Path(dir_name, f'nasa_epic_{photo_number}.png')
        fetch_and_save(url_image, path_to_image, payload)


if __name__ == "__main__":
    main()
