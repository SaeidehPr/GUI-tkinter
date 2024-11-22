import tkinter as tk 

root = tk.Tk()
root.title("Entry Widget")

label = tk.Label(root, text = "Name: ")
entry = tk.Entry(root) #, state = "disabled")

entry.insert(0, "Thhe Metabrains!")
entry.config(state = "disabled")

label.pack()
entry.pack()

root.mainloop()