import tkinter as tk

root = tk.Tk()
root.title("The Scale Like Thermometer")
root.minsize(300,200)

def scaleColor(value):
    if (int(value) <= 20):
        scale.config(bg = "lightblue")
    elif(20 < int(value) <= 30):
        scale.config(bg = "lightgreen")
    elif(30 < int(value) <= 40):
        scale.config(bg = "yellow") 
    elif(40 < int(value) <= 60):
        scale.config(bg = "orange")  
    else:
        scale.config(bg = "red")


scale = tk.Scale(root, length= 250, from_ = 0, to = 100, 
                tickinterval = 15, 
                orient = "horizontal",
                command = scaleColor)
scale.set(30)

scale.pack()

root.mainloop()