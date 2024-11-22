import tkinter as tk 

root = tk.Tk()
root.title("Scrolling through a List")
root.minsize(300, 200)

frame = tk.Frame(root, height = 7, width = 10)

l = tk.Listbox(frame, width = 15, height = 10, justify = "right",
               selectbackground = "blue", selectmode="single")

scroll = tk.Scrollbar(frame, command = l.yview)

l.config(yscrollcommand = scroll.set)

scroll.pack(side = "left", fill = "y")

for item in range(20):
    l.insert("end", item)

l.pack()
frame.pack()

root.mainloop()