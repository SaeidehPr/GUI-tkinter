import tkinter as tk 

root = tk.Tk()
root.title("Displaying a list of items")
root.minsize(300, 200)

l = tk.Listbox(root, width = 15, height = 15, justify = "right",
               selectbackground = "blue", selectmode="single")

for item in range(15):
    l.insert("end", item)

l.pack()

root.mainloop()