import tkinter as tk
from PIL import Image, ImageTk

image = Image.open("pexels.jpg")
image = image.resize((300,500))

root = tk.Tk()

img = ImageTk.PhotoImage(image) # To convert Image into a photo image object
                                # then it will be useable in our application.

label = tk.Label(root, image = img)
label.pack()

root.mainloop()