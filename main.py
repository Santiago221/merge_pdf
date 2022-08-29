import os
from PyPDF2 import PdfMerger
from tkinter import *
from tkinter import filedialog

def askfile():
    """
        ask file function
    """

    files = filedialog.askopenfilenames(title = 'Escolha arquivos',filetypes = (("PDF","*.PDF"),("all files","*.*")))
    return files

def savefile():
    """
    Save file function
    """

    result = filedialog.askdirectory(title='Escolha diretório de destino')
    return result
def get_files():
    """
        get file function
    """

    merger = PdfMerger()
    files = askfile()
    result = savefile()
    print(result)
    resultfile = 'result.pdf'
    for file in files:
        print(file)
        merger.append(file)
    merger.write(f'{result}/{resultfile}')
    merger.close()

if __name__ == '__main__':
    get_files()
