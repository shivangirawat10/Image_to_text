#%%

from typing import Text
import cv2 
import pytesseract
from googletrans import Translator

#%%

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

# %%

img=cv2.imread("testocr.png")

# %%

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
Text_extracted=pytesseract.image_to_string(img)
print(Text_extracted)
cv2.imshow('Result',img)
cv2.waitKey(0)

# %%

hImg,wImg,_=img.shape
boxes=pytesseract.image_to_data(img)
print(boxes)

# %%

for x,b in enumerate(boxes.splitlines()):
    if(x!=0):
        b=b.split()
        if(len(b)==12):
            x=int(b[6])
            y=int(b[7])
            w=int(b[8])
            h=int(b[9])
            cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),2)


# %%

cv2.imshow('Result',img)
cv2.waitKey(0)

# %%

def language_conversion(input_text,destination):
    translator = Translator()
    text_to_translate = translator.translate(input_text,dest= destination)
    print('The Text has been converted to '+destination+' language'+'\n')

    return text_to_translate.text
              
# %%
print(language_conversion(Text_extracted,"hi"))

# %%
