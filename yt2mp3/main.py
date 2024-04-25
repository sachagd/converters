import os
import subprocess
import sys
from multiprocessing import Pool, cpu_count
from pytube import Playlist, YouTube
from bs4 import BeautifulSoup
import requests

def get_complete_video_title(video_url):
    response = requests.get(video_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title_tag = soup.find("title")
    complete_title = title_tag.text.strip()
    if complete_title.endswith(" - YouTube"):
        complete_title = complete_title[:-10]
    return complete_title

def download_and_convert(video_url, output_path):
    try:
        # Download video
        complete_title = get_complete_video_title(video_url).replace('"',"'").replace("|"," ").replace("/"," ").replace(":", " ").replace("\\", " ")
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        video_filename = f"{complete_title}.mp4"
        audio_stream.download(output_path=output_path, filename=video_filename)
        
        # Convert to MP3
        input_path = os.path.join(output_path, video_filename)
        subprocess.run(f'ffmpeg -i "{input_path}" -map 0:a:0 -acodec libmp3lame "{os.path.join(output_path, f"{complete_title}.mp3")}"', shell=True, stderr=subprocess.DEVNULL)
        os.remove(input_path)
        print(f"Audio of '{complete_title}' downloaded successfully.")
        
    except Exception:
        failed_videos.append(complete_title)

if __name__ == "__main__":
    input_file = open("input.txt", 'r')
    urls = input_file.read().splitlines()
    failed_videos = []
    num_elements_per_pool = int(sys.argv[1]) if len(sys.argv) > 1 else cpu_count()

    for url in urls:
        playlist = Playlist(url)
        video_urls = playlist.video_urls

        with Pool(processes=num_elements_per_pool) as pool:
            pool.starmap(download_and_convert, [(video_url, "output") for video_url in video_urls])

    if failed_videos:
        print("Failed to process the following videos:")
        for video in failed_videos:
            print(video)
    else:
        print("All videos processed successfully without any errors.")
