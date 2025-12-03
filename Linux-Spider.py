import tkinter
from PIL import Image, ImageTk
import random

root = tkinter.Tk()
root.attributes('-fullscreen', True)  # fullscreen
root.attributes('-topmost', True)     # সব উইন্ডোর উপরে
root.attributes('-alpha', 0.9)        # অর্ধস্বচ্ছ উইন্ডো (Linux-এ কাজ করে)

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

canvas = tkinter.Canvas(root, width=width, height=height,
                        bg='black', highlightthickness=0)
canvas.pack()

# Gost image
img = Image.open("gost.png")
gost_img = ImageTk.PhotoImage(img)

canvas.create_image(400, 400, image=gost_img)

def add_gost():
    x = random.randint(0, width)
    y = random.randint(0, height)
    canvas.create_image(x, y, image=gost_img)
    root.after(500, add_gost)

# enable window closing
root.protocol('WM_DELETE_WINDOW', root.destroy)

add_gost()
root.mainloop()
