import youtube_dl
from multiprocessing import Pool

def download_song(video):
    with youtube_dl.YoutubeDL({'format': 'bestaudio/best', 'keepvideo': False,
                               'outtmpl': "output\\" + video['title'].replace("/", " ") + ".mp3"}) as ydl:
        ydl.download([video['url']])

def download(n): # Specify the number of processes you want to run concurrently
    input_file = open("input.txt", 'r')
    playlist_url = input_file.read()

    ydl_opts = {
        "ignoreerrors": True,
        "quiet": True,
        "extract_flat": "in_playlist",
        "extract_flat_opts": {
            "force_generic_extractor": True,
            "in_playlist": True,
            "video_select": "title,webpage_url"
        }
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        playlist_dict = ydl.extract_info(playlist_url, download=False)

    playlist_entries = playlist_dict.get("entries", [])

    with Pool(n) as pool:
        pool.map(download_song, playlist_entries)
