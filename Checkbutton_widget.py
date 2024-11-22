import tkinter as tk 

root = tk.Tk()
root.title("The Checkbutton Widget")
root.minsize(300, 200)

tk.Label(root, text = "Select your best fruit!").pack()

chkbtn = tk.Checkbutton(root, text = "Mango").pack()
chkbtn = tk.Checkbutton(root, text = "Banana").pack()
chkbtn = tk.Checkbutton(root, text = "Apple").pack()
chkbtn = tk.Checkbutton(root, text = "Grape").pack()
chkbtn = tk.Checkbutton(root, text = "Grapefruit").pack()
chkbtn = tk.Checkbutton(root, text = "Maetabrains", state = "disabled").pack()

# chkbtn = tk.Checkbutton(root, text = "Metabrains")
# chkbtn.pack()

root.mainloop()