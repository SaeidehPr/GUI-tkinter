import tkinter as tk

root = tk.Tk()
root.title("The Spinbox Application")
root.minsize(300,200)

tk.Spinbox(root, from_ = 0, to = 10).pack()

root.mainloop()
