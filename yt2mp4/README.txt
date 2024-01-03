There are two versions of the code :

      - version 1 ensures that all mp3 files have the same name as the youtube video
      
      - version 2 is about 35% faster

Warning : for a reason too complex to be explained here, all mp4 files are only composed of audio, ie, there is no video. 

The two versions use multiprocessing to download multiple videos at a time, 
you can choose the number of video downloaded concurrently by adding it to the executing command of main.py
By default it chooses the number of cores in your CPU

Write the playlists urls, one per line, in input.txt and then execute main.py
