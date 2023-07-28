There are two versions of the code :

      - version 1 ensure that all mp3 file have the same name as the youtube video
      
      - version 2 is about 35% faster

The two versions use multiprocessing to download multiple songs at a time, 
you can choose the number of video download concurrently by adding it to the executing command of main.py
By default it choose the number of core in your CPU

You need to write the playlist url (and only that) in input.txt and then execute main.py
