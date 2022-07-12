import threading
from tkinter import *
import tkinter.font as font
from turtle import bgcolor, color, width
import pyqrcode
import jwt
import datetime


# Iniciar GUI
ws = Tk()
ws.title("Generador de QR")
ws.attributes("-fullscreen", True)
ws.config(background='#000')

# Methodos
def generate_QR():
    global qr,img
    encoded_jwt = jwt.encode({"exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=30)},"SECRET_KEY",algorithm="HS256")
    qr = pyqrcode.create('URL'+encoded_jwt)
    img = BitmapImage(data = qr.xbm(scale=8))
    try:
        display_code()
    except:
        pass

def display_code():
    img_lbl.config(image = img,background='#FFF')
    button.pack_forget()
    img_lbl.pack(expand=True)
    timer = threading.Timer(5, clear_code)
    timer.start()

def clear_code():
    img_lbl.config(image='',background='#000')
    img_lbl.pack_forget()
    button.pack(expand=True)


# Construccion de la GUI

f = font.Font(size=24)

button = Button(
    ws,
    text = "Generar QR",
    width=15,
    command = generate_QR,
    bg='#000',
    fg='#FFF',
    font=f
    )
button.pack(expand=True)

img_lbl = Label(
    ws,background='#000')
 
ws.mainloop()