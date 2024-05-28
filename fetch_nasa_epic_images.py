import datetime
import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from fetch_helper import fetch_and_save


load_dotenv()
API_KEY = os.environ["API_KEY"]


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
    nasa_epic()
