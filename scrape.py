import yt_dlp
import concurrent.futures
import json

# Script Settings
tiktok_data_file_name = "user_data_tiktok.json"
save_metadata = True
thread_count = 20


# Fetch Tiktok data file
def get_json():
  with open(tiktok_data_file_name, 'r', encoding="utf8") as f:
    data = json.load(f)
    f.close()
    return data

# Download tiktok video
def download_tiktok_video(url: str, output_name: str = "test", output_path: str = "."):
  ydl_opts = {
    'outtmpl': f'{output_path}/{output_name}.%(ext)s',  # Save file as title.ext in the specified directory
    'format': 'best',  # Download the best available format
    'quiet': True,    # Display progress
    'noplaylist': True, # Ensure only a single video is downloaded
    'writeinfojson': save_metadata,
  }

  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      ydl.download([url])
      print(f"Download of {url} completed successfully!")
  except Exception as e:
    print(f"An error occurred: {e}")

tiktok_url = "https://www.tiktokv.com/share/video/7423968892256636191/"
data = get_json()["Activity"]["Favorite Videos"]["FavoriteVideoList"]

pool = concurrent.futures.ThreadPoolExecutor(max_workers=thread_count)
for index in range(0, len(data), thread_count):
  futures = [] # List of tasks
  
  for workerNum in range(thread_count): # Get workers
    if index + workerNum < len(data):
      video = data[index + workerNum]
      date = video["Date"]
      
      futures.append(pool.submit(download_tiktok_video, video["Link"], output_name=date, output_path=f"./downloads/{date}"))
    
  concurrent.futures.wait(futures)