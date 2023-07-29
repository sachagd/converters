from PyPDF2 import PdfMerger
import os

input_folder = r'input'
output_folder = r'output' 

merger = PdfMerger()

for root, dirs, file_names in os.walk(input_folder):
    for file_name in file_names:
        merger.append(os.path.join(input_folder,file_name))

merger.write(os.path.join(output_folder,"output.pdf"))
merger.close()

b = input("veux-tu supprimer l'input (les pdf) ? (o/n)")
if b == "o":
    for i in os.listdir(input_folder):
        os.remove(os.path.join(input_folder,i))