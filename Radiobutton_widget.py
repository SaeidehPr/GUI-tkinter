import tkinter as tk 

root = tk.Tk()
root.title("The Checkbutton Widget")
root.minsize(300, 200)

for text, value in [("Apple", 1), ("Bnana", 2), ("Grape", 3), ("Strawberry", 4), 
                    ("Olive", 5)]:
    tk.Radiobutton(root, text = text, value = value, indicatoron = 0).pack()

# tk.Radiobutton(root, text = "Metabrains", value = 1).pack()

root.mainloop()