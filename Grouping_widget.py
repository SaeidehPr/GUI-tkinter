import tkinter as tk 

root = tk.Tk()
root.title("Grouping Widget with Labelframe")
root.minsize(300,200)

labelframe = tk.LabelFrame(root, text='login')
labelframe.pack()

label_email = tk.Label(labelframe, text='Email: ')
email_entry = tk.Entry(labelframe)

label_password  = tk.Label(labelframe, text='Password: ')
password_entry = tk.Entry(labelframe)

label_email.grid(column=0, row=0)
email_entry.grid(column=1, row=0)
label_password.grid(column=0, row=1)
password_entry.grid(column=1, row=1)

root.mainloop()