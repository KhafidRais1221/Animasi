from tkinter import *
import time

LEBAR = 900
TINGGI = 800
xSpeed = 5
ySpeed = 5
window = Tk()

canvas = Canvas(window,width=LEBAR,height=TINGGI)
canvas.pack()

background_image = PhotoImage(file='Angkasa.png')
background = canvas.create_image(0,0, image=background_image, anchor=NW)

photo_image = PhotoImage(file='ufo.png')
my_image = canvas.create_image(0,0, image=photo_image, anchor=NW)

image_lebar = photo_image.width()
image_tinggi = photo_image.height()
while True:
    koordinat = canvas.coords(my_image)
    #print(koordinat)
    if(koordinat[0]>=(LEBAR-image_lebar) or koordinat[0]<0):
        xSpeed = -xSpeed
    if (koordinat[1] >= (TINGGI - image_tinggi) or koordinat[1] < 0):
        ySpeed = -ySpeed
    canvas.move(my_image,xSpeed,ySpeed)
    window.update()
    time.sleep(0.01)



window.mainloop()