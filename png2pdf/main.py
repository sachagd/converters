from PIL import Image
import os

input_folder = 'input'
output_folder = 'output' 

image = [Image.open(os.path.join(input_folder, i)).convert('RGB') for i in os.listdir(input_folder)]
image[0].save(os.path.join(output_folder, 'output.pdf'), save_all=True, append_images=image[1:len(image)])

b = input("veux-tu supprimer les png ? (o/n)")
for i in image:
    i.close()
if b == "o":
    for i in os.listdir(input_folder):
        os.remove(os.path.join(input_folder,i))
