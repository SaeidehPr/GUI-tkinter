import tkinter as tk 

root = tk.Tk() # This is our application and we can add atribiutes to it.
root.title("Label Widget")

label = tk.Label(root, text = "label in Tkinter", 
                 bg = "lightblue",
                 font = "calibri",
                 wraplength = 100, padx = 20, pady = 20)

label.pack()

root.mainloop()