import tkinter as tk 

root = tk.Tk()
root.title("Button Widget")

btn = tk.Button(root, text = "Click me!", relief = "raised", state = "disabled").pack()
# btn = tk.Button(root, text = "Click me!", relief = "sunken").pack()
# btn = tk.Button(root, text = "Click me!", relief = "flat").pack()
# btn = tk.Button(root, text = "Click me!", relief = "ridge").pack()
# btn = tk.Button(root, text = "Click me!", relief = "groove").pack()
# btn = tk.Button(root, text = "Click me!", relief = "solid").pack()

root.mainloop()