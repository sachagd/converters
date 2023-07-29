from pytube import Playlist, YouTube
from multiprocessing import Pool, cpu_count
import sys

def download_audio(video_url, output_path):
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download(output_path=output_path)
    print(f"Audio of '{yt.title}' downloaded successfully.")

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
