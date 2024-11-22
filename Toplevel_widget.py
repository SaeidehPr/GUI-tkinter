import tkinter as tk 


root = tk.Tk()
root.title("My Toplevel Application")
root.minsize(300, 200)

# tk.Toplevel() # For instance, you can use them for Cookies in your web page

def agree():
    tk.Label(root, text = "Good Choice!").pack()
    toplevel.destroy()

toplevel = None
def top():
    global toplevel
    toplevel = tk.Toplevel(root)
    label = tk.Label(toplevel, text = "Terms and Conditions!").pack()
    terms = tk.Message(toplevel, text = "This is an agreement that stands as the terms and conditions of" 
    "the metrabrains. Here you promise to learn consisitently in order to become a world" 
    "changing engineer tomorrow. Set yourself a daily goal to afvance step by step, this will be a forward"
    "move toward your dreams.", width = 300).pack()
    btn = tk.Radiobutton(toplevel, text = "I agree", command = agree, state = "normal", value = 1).pack()
    btn = tk.Radiobutton(toplevel, text = "I disagree", command = root.quit, state = "normal").pack()

btn = tk.Button(root, text = "Install", command = top).pack()

root.mainloop()