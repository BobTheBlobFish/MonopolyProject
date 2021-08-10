import tkinter as tk
import tkinter.font as font
from tkinter import *
import os

root = tk.Tk()
root.title('Monopoly Credit Manager - 2021 Edition!')
logo = PhotoImage(file = r"C:\Users\ABC\Desktop\monopoly title.png")
cashbag = PhotoImage(file = r"C:\Users\ABC\Desktop\cashbag.png")

def CreatePlayer():
    root = tk.Tk()
    root.title('New Player Creator!')
    AvatarCanvas = tk.Canvas(root, height=50, width=320, bg= "Red")
    AvatarCanvas.create_text(150,30,fill="White", font = "Times 20  bold", text="Select the player Icon!")
    AvatarCanvas.pack()
    myFont = font.Font(size="200")

    AvatarBoat = Button(root, text = "⛵", padx = 30, pady = 30, command = BoatButton)
    AvatarBoat['font'] = myFont
    AvatarSnake = Button(root, text = "🐍", padx = 30, pady = 30, command = SnakeButton)
    AvatarSnake['font'] = myFont
    AvatarGun = Button(root, text = "🔫", padx = 30, pady = 30, command = GunButton)
    AvatarGun['font'] = myFont
    AvatarAirplane = Button(root, text = "🛦", padx = 30, pady = 30, command = AirplaneButton)
    AvatarAirplane['font'] = myFont

    AvatarBoat.pack(side=LEFT)
    AvatarGun.pack(side=LEFT)
    AvatarSnake.pack(side=RIGHT)
    AvatarAirplane.pack(side=RIGHT)


    root.mainloop()
    

canvas = tk.Canvas(root, height=700, width=700, bg= "Green")
canvas.pack(fill = "both", expand = "True")
canvas.create_image(150,-148, image = logo, anchor = "nw")
canvas.create_image(5,15, image = cashbag, anchor = "nw")
canvas.create_image(615,15, image = cashbag, anchor = "nw")

def BoatButton():
    # Make New player and give Avatar 'Boat' in MySQL for the given player under this
    pass #<--- this pass is temporary
def SnakeButton():
    # Make New player and give Avatar 'Snake' in MySQL for the given player under this
    pass #<--- this pass is temporary
def GunButton():
    # Make New player and give Avatar 'Gun' in MySQL for the given player under this
    pass #<--- this pass is temporary

def AirplaneButton():
    # Make New player and give Avatar 'Airplane' in MySQL for the given player under this
    pass #<--- this pass is temporary



frame = tk.Frame(root, bg = "white")
frame.place(relwidth= 0.8, relheight = 0.75, relx = 0.1, rely = 0.15)

newplayer = tk.Button(root, text="New Player!", padx=5, pady =5, fg = "white", bg = "red" , command =CreatePlayer)
newplayer.pack()

manage= tk.Button(root, text="Edit Existing Player!", padx=  10, pady = 5 , fg= "white" , bg = "red")
manage.pack()



root.mainloop()
