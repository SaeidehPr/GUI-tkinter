import tkinter as tk 

root = tk.Tk()
root.title("Message Widget")
root.minsize(300, 200)

tk.Label(root, text = "ndkh jhfl skh kij.lkjm.kjj;km/ isligj lj ojlsjkidjgj oisudjglk[pyo xdjksh,kn uh h.khkj.lk jj ja  j .ljfj", bg = "pink").pack()

tk.Message(root, text = "ndkh jhfl skh kij.lkjm.kjj;km/ isligj lj ojlsjkidjgj oisudjglk[pyo xdjksh,kn uh h.khkj.lk jj ja  j .ljfj", 
           bg = "gray",
           width = 300, 
           justify= "center", 
           relief= "raised").pack()

root.mainloop()