import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.attributes('-fullscreen', True)              # fullscreen
root.attributes('-topmost', True)                 # সব উইন্ডোর উপরে
root.attributes('-transparentcolor', 'black')     # Windows-only

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

canvas = tkinter.Canvas(root, width=width, height=height,
                        bg='black', highlightthickness=0)
canvas.pack()

# load ghost image
img = Image.open("ghost.png")
ghost_img = ImageTk.PhotoImage(img)

# first ghost
canvas.create_image(400, 400, image=ghost_img)

def add_ghost():
    x = random.randint(0, width)
    y = random.randint(0, height)
    canvas.create_image(x, y, image=ghost_img)
    root.after(500, add_ghost)  # function call

# disable window closing
root.protocol('WM_DELETE_WINDOW', lambda: None)

# start the loop
add_ghost()
root.mainloop()
