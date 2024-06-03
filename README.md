# Space Telegram

The project is designed to automatically publish photos of space in the telegram channel

### How to install

Clone the repository

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```commandline
pip install -r requirements.txt
```

### Create a telegram bot

Save the token received when creating the bot. Add your bot to your telegram channel.
Give him administrator rights.

### Get a Nasa API Token
 
Go to the Nasa website at the [link](https://api.nasa.gov/)
and get an API token

### Create a file `.env`:

```commandline
NASA_API_KEY=your_Nasa_API_token
TELEGRAM_TOKEN=your_telegram_token
POST_FREQUENSY=frequency_of_publications_in_seconds
TG_CHAT_ID='your_channel_ID'
IMAGES_DIR_PATH=path_to_the_image_directory
```
By default, the publication frequency is four hours. 
If you do not specify the path to the image directory, the Images will be uploaded
to the project directory `images`

### Download photos of space

To download launch photos from the site, you can specify the launch id.
By default, the last launch.
```commandline
python fetch_spacex_images.py -l launch_id
```

To download astronomical images of the day from the Nasa website, enter the command
specifying the number. By default, 10 photos will be downloaded.
```commandline
python fetch_nasa_apod_images.py -c count
```

To download epic photos from the Nasa website, enter
```commandline
python fetch_nasa_epic_images.py
```

### Start posting photos

To publish one photo, run the script specifying the path to the file.
By default, a randomly selected photo will be published.
```commandline
python space_photos_bot.py -p path_to_file
```

For automated publishing, run the script
```commandline
python automatic_space_photos_bot.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).