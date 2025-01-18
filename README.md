# Heads Up

- This process can take hours depending on the number of videos you have.

- Keep an eye on your device storage, downloading large amounts of videos will use a lot of storage quickly.

# How To Use

## Prerequisites

- Make sure Python is installed

- Make sure `yt-dlp` is installed, you can install it with `pip install yt-dlp`

## Usage

- Download your Tiktok data as a json file (in your settings, go to your account and you should find the option to download it there)

- Put the json file you recived in the same filder as the python file

- Open said folder in your terminal and run the python file

## Output

- Your favorited videos, as well as metadata such as title, like count, favorite count, etc. will be saved into a `downloads` folder in the same directory.

- Each video will have its own folder that pairs it with its metadata file.

# Tweaking The Script

At the top of the file, there are variables you can use to tweak the script abit without digging through code.

- `thread_count`: This changes the number of downloads that can happening at once. The default is 20, as setting it too high may result in a large consumption of computer resources.

- `tiktok_data_file_name`: The name of the file containing your tiktok data. The default is "user_data_tiktok.json", as I believe this is the default name when you download your data.

- `save_metadaa`: Whether to save the metadata of the video or not. The default is `True`. Set it to `False` if you dont want the metadata. (Metadata contains info like the video title, hashtags, video publisher, and some more technical stuff)
