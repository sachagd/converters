import youtube_dl

input = open("input.txt",'r')
playlist = input.read()

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
    playlist_dict = ydl.extract_info(playlist, download=False)

playlist_entries = playlist_dict.get("entries", [])

for video in playlist_entries:
    with youtube_dl.YoutubeDL({'format':'bestaudio/best', 'keepvideo':False, 'outtmpl': "output\\"+video['title']+".mp3"}) as ydl:
        ydl.download([video['url']])
