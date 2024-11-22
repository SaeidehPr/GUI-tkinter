import tkinter as tk
from PIL import Image, ImageTk

image = Image.open("pexels.jpg")
image = image.resize((250,400))


root = tk.Tk()
root.title("Text Widget")
root.minsize(300,200)

img = ImageTk.PhotoImage(image)

text = tk.Text(root)
text.insert("insert", "The first line in the Text widget ... .\n")
text.insert("end", "The second line in the Text widget ... .\n")
text.image_create("end", image = img)

text.pack()

text.tag_add("here", "1.0", "1.40")
text.tag_add("next", "2.0", "2.45")
text.tag_config("here", background = "orange", font = "times")
text.tag_config("next", background = "yellow", font = "calibri")

root.mainloop()