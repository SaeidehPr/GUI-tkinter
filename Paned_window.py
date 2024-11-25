import tkinter as tk 

root = tk.Tk()
root.title("Dividing with panes")
root.minsize(300,200)

panewindow = tk.PanedWindow(root, bg='red', orient='vertical', width=200)

panewindow.pack()

l1 = tk.Label(panewindow, text='Pane 1')
panewindow.add(l1)
l2 = tk.Label(panewindow, text='Pane 2')
panewindow.add(l2)
l3 = tk.Label(panewindow, text='Pane 3')
panewindow.add(l3)

root.mainloop()