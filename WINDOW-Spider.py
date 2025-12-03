import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.attributes('-transparentcolor', 'black')  # Windows-only

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

canvas = tkinter.Canvas(root, width=width, height=height,
                        bg='black', highlightthickness=0)
canvas.pack()

# load ghost image
img = Image.open("gost.png")
gost_img = ImageTk.PhotoImage(img)

# first ghost
canvas.create_image(400, 400, image=gost_img)

def add_gost():
    x = random.randint(0, width)
    y = random.randint(0, height)
    canvas.create_image(x, y, image=gost_img)
    root.after(500, add_gost)  # function call

# disable window closing
root.protocol('WM_DELETE_WINDOW', lambda: None)

# start the loop
add_gost()
root.mainloop()
