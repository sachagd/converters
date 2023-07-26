import os
import subprocess

input_folder = "input"
output_folder = "output" 

# Get a list of all files in the input folder with the ".mp4" extension
input_files = [file for file in os.listdir(input_folder)]

for input_file in input_files:
    # Prepare the output filename for each track
    output_file_1 = os.path.join(output_folder, f"{os.path.splitext(input_file)[0]}_track1.mp3")
    output_file_2 = os.path.join(output_folder, f"{os.path.splitext(input_file)[0]}_track2.mp3")

    # Use ffmpeg to extract the audio tracks as separate MP3 files
    cmd = f"ffmpeg -i {os.path.join(input_folder, input_file)} -map 0:a:0 {output_file_1} -map 0:a:1 {output_file_2}"
    subprocess.run(cmd, shell=True)
