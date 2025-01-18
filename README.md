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

- This process can take hours, depending on the amount of saved videos you have.


# Tweaking The Script

- At the top of the file, there is a variable called `thread_count`. This changes the number of downloads that can happening at once. The default is 20, as setting it too high may result in a large consumption of computer resources.
