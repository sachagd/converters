import os
import subprocess

input_folder = "input"
output_folder = "output" 

input_files = [file for file in os.listdir(input_folder)]

for input_file in input_files:
    input_path = os.path.join(input_folder, input_file)
    
    # Use ffprobe to get information about the audio streams
    ffprobe_cmd = f"ffprobe -v error -select_streams a:0 -show_entries stream=nb_streams -of default=noprint_wrappers=1:nokey=1 {input_path}"
    num_audio_streams = int(subprocess.check_output(ffprobe_cmd, shell=True).decode().strip())
    
    for i in range(num_audio_streams):
        output_file = os.path.join(output_folder, f"{os.path.splitext(input_file)[0]}_track{i+1}.mp3")
        
        cmd = f"ffmpeg -i {input_path} -map 0:a:{i} {output_file}"
        subprocess.run(cmd, shell=True)
