from pytube import Playlist, YouTube
from bs4 import BeautifulSoup
from multiprocessing import Pool, cpu_count
import requests
import sys

def get_complete_video_title(video_url):
    try:
        # Fetch the HTML content of the video page
        response = requests.get(video_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the video title from the HTML
        title_tag = soup.find("title")
        complete_title = title_tag.text.strip()

        # Remove the "- YouTube" suffix from the title
        if complete_title.endswith(" - YouTube"):
            complete_title = complete_title[:-10]

        return complete_title
    except Exception:
        return None


def download_audio(video_url, output_path):
    complete_title = get_complete_video_title(video_url)
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    output_filename = f"{complete_title}.mp4".replace("\"","'").replace("|","-").replace("/","-")
    audio_stream.download(output_path=output_path, filename=output_filename)
    print(f"Audio of '{complete_title}' downloaded successfully.")
        
if __name__ == "__main__":
    input_file = open("input.txt", 'r')
    urls = input_file.read().splitlines()

    if len(sys.argv) > 1:
        num_elements_per_pool = int(sys.argv[1])
    else:
        num_elements_per_pool = cpu_count()

    for url in urls:
        playlist = Playlist(url)
        video_urls = playlist.video_urls

        with Pool(processes=num_elements_per_pool) as pool:
            pool.starmap(download_audio, [(video_url, "output") for video_url in video_urls])
