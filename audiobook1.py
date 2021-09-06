#------------------------use this code to read pdf from scratch to end-----------------------

import PyPDF2

path = input("Enter the path of pdf file:")
pdfReader = PyPDF2.PdfFileReader(open(f'{path}','rb'))

import pyttsx3


speaker=pyttsx3.init()
for page_num in range(pdfReader.numPages):

    text=pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
speaker.save_to_file(text,"audio.mp3")
speaker.runAndWait()