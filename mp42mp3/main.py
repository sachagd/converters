import os
import subprocess
import sys
from multiprocessing import Pool, cpu_count

def process_file(file):
    input_folder = "input"
    output_folder = "output"

    input_path = os.path.join(input_folder, file)
    safe_input_path = f'"{input_path}"'

    # Extract the number of audio tracks using FFmpeg
    cmd = f'ffprobe -loglevel error -select_streams a -show_entries stream=index -of csv=p=0 {safe_input_path}'
    audio_tracks = subprocess.check_output(cmd, shell=True).decode().splitlines()
    
    for track_index in audio_tracks:
        output_filename = f"{os.path.splitext(file)[0]}_audio_track_{track_index}.mp3"
        output_path = os.path.join(output_folder, output_filename)
        safe_output_path = f'"{output_path}"'

        # FFmpeg command to extract the audio track and convert it to mp3
        cmd = f'ffmpeg -i {safe_input_path} -map 0:a:{track_index} -acodec libmp3lame {safe_output_path}'
        subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"

    input_files = [file for file in os.listdir(input_folder)]

    # Determine the number of processes to run concurrently
    if len(sys.argv) > 1:
        num_elements_per_pool = int(sys.argv[1])
    else:
        num_elements_per_pool = cpu_count()

    # Create a pool of processes
    with Pool(num_elements_per_pool) as p:
        p.map(process_file, input_files)

    print("Audio extraction and conversion completed.")
