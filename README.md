# 👻 Ghost-Hacked

A fun fullscreen **Ghost Overlay Animation** built with **Python**, **Tkinter**, and **Pillow (PIL)**. This project creates a spooky effect by spawning multiple ghosts randomly across the screen. Works on both **Windows** and **Linux (Ubuntu)**.

---

## 🚀 Features

* Fullscreen overlay window
* Random ghost movement
* Windows & Linux support
* Transparent background on Windows
* Semi-transparent alpha mode on Linux
* Ghost image rendered using Pillow
* Topmost window (always stays above all apps)

---

## 🖥️ Platform Support

### ✔️ Windows

* Uses `-transparentcolor` to remove background
* Perfect for fullscreen pranks or overlays

### ✔️ Linux / Ubuntu

* Uses `-alpha` transparency
* Keeps black background but adds ghost effects smoothly

---

## 📂 Project Structure

```
Ghost-Hacked/
├── WINDOW-Spider.py     # Windows version (transparent overlay)
├── Linux-Spider.py      # Linux/Ubuntu version (alpha overlay)
├── ghost.png            # Ghost image used in the animation
└── README.md            # Project documentation
```

---

## 🛠️ Requirements

Install the required packages:

```bash
pip install pillow
```

Tkinter comes preinstalled on most systems, but on Ubuntu you may need:

```bash
sudo apt install python3-tk
```

---

## ▶️ How to Run

### **Windows**

```bash
python WINDOW-Spider.py
```

### **Linux / Ubuntu**

```bash
python3 Linux-Spider.py
```

---

## 🎨 Customize

You can replace **ghost.png** with your own PNG image.
Recommended size: **200×200** or **transparent PNG** for best results.

---

## ⚙️ Code Highlights

### Random Ghost Spawning

```python
x = random.randint(0, width)
y = random.randint(0, height)
canvas.create_image(x, y, image=ghost_img)
```

### Auto Animation Loop

```python
root.after(500, add_ghost)
```

---

## ⚠️ Disclaimer

This project is for **fun and educational purposes only**.
Do not use it to scare or disturb people without consent.

---

## ⭐ Give a Star

If you like this project, please give it a ⭐ on GitHub to support development!

---

## 📧 Contact

Created by **Kashif Mustari**
Feel free to fork, modify, and experiment!
