#------------------------use this code to read pdf from scratch to end-----------------------

#import PyPDF2

#path = input("Enter the path of pdf file:")
# pdfReader = PyPDF2.PdfFileReader(open(f'{path}','rb'))

#import pyttsx3


##speaker=pyttsx3.init()
#for page_num in range(pdfReader.numPages()):

 #   text=pdfReader.getPage(page_num).extractText()
 #   speaker.say(text)
 #   speaker.runAndWait()
#speaker.stop()
#speaker.save_to_file(text,"audio.mp3")
#speaker.runAndWait()


#--------------------------------use this code to read the pdf in chapterwise-----------------
import PyPDF2
path = input("Enter the path of pdf file:")
pdfReader = PyPDF2.PdfFileReader(open(f'{path}','rb'))

import pyttsx3

speaker=pyttsx3.init()
Tota_page = pdfReader.numPages
print(f'Toatl pages in this pdf is:{Tota_page}')
page = int(input("Enter the Page Number from which you want to read:"))
page2 = int(input("Enter the Page Number till which you want to read this pdf"))
for page_num in range(page-1,page2):

    text=pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
speaker.save_to_file(text,"audio.mp3")
speaker.runAndWait() 



