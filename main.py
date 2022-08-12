import os
from PyPDF2 import PdfMerger
def get_files(dir):
    merger = PdfMerger()
    for file in os.listdir(dir):
        print(file.split(' - ')[0])
        merger.append(f'{dir}/{file}')
    merger.write(f'{dir}/result.pdf')
    merger.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dir = "folder"
    get_files(dir)
