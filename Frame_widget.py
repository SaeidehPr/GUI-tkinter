import tkinter as tk 

root = tk.Tk()
root.title("Widget in Window with Frame")
root.minsize(200, 200)

frame = tk.Frame(root, bg = "pink", height = 400, width = 400)
label = tk.Label(frame, text = "label in Tkinter", 
                 bg = "lightblue",
                 font = "calibri",
                 wraplength = 100, padx = 20, pady = 20).pack()
for text, value in [("Apple", 1), ("Bnana", 2), ("Grape", 3), ("Strawberry", 4), 
                    ("Olive", 5)]:
    tk.Radiobutton(frame, text = text, value = value, indicatoron = 0, width = 10).pack()

frame.pack()

root.mainloop()