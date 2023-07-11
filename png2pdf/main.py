from PIL import Image
import os

png_folder = r'C:\Users\33613\Desktop\convertisseurs\png2pdf\png'
pdf_folder = r'C:\Users\33613\Desktop\convertisseurs\png2pdf\pdf' 


for i in os.listdir(pdf_folder):
    os.remove(os.path.join(pdf_folder,i))
image = [Image.open(os.path.join(png_folder, i)).convert('RGB') for i in os.listdir(png_folder)]
image[0].save(os.path.join(pdf_folder, 'output.pdf'), save_all=True, append_images=image[1:len(image)])


b = input("veux-tu supprimer les png ? (o/n)")
for i in image:
    i.close()
if b == "o":
    for i in os.listdir(png_folder):
        os.remove(os.path.join(png_folder,i))
