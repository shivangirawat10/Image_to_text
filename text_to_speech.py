#%%

from tkinter import *
from gtts import gTTS
from playsound import playsound
from googletrans import Translator



root = Tk()


C = Canvas(root, bg="blue", height=400, width=400)
filename = PhotoImage(file = "Caribbean-beach.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)



root.title('Text To Speech')




Label(root, text = 'Translator' , font='Courier 25  bold underline' ).pack()



Label(root, text ='Enter Text:', font ='Courier 17 bold underline', ).place(x=20,y=60)

C.pack()

Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable=Msg, width ='60')
entry_field.place(x=20, y=103)




def Text_to_speech():
    Message = entry_field.get()
    translator = Translator()
    text_to_translate = translator.translate(Message,dest= 'es')
    speech = gTTS(text = text_to_translate.text)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')


   
def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button
Button(root, text = "PLAY" , font = 'Courier 15 bold italic', command = Text_to_speech, width =4,bg = 'blue').place(x=20, y=140)
Button(root,text = 'EXIT',font = 'Courier 15 bold italic' , command = Exit, bg = 'Red').place(x=96,y=140)
Button(root, text = 'RESET', font='Courier 15 bold italic', command = Reset,bg = 'yellow').place(x=172 , y =140)


#infinite loop to run program
root.mainloop()


# %%

# %%

# %%
