You need ffmpeg for this one (https://ffmpeg.org/download.html)

Put all mp4 files in the input folder, then execute main.py

The code use multiprocessing to convert multiple files at a time, 
you can choose the number of file converted concurrently by adding it to the executing command of main.py
By default it chooses the number of cores in your CPU
