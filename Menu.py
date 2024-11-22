import tkinter as tk

root = tk.Tk()
root.title("Let's make a Menu")
root.minsize(300, 200)

mainmenu = tk.Menu(root)

# File Menu starts here
filemenu = tk.Menu(mainmenu, tearoff = 0)

filemenu.add_command(label = "New Text File")
filemenu.add_command(label = "New File")
filemenu.add_command(label = "New Window")
filemenu.add_separator()
filemenu.add_command(label = "Open File")
filemenu.add_command(label = "Open Folder")

# Open Recent dropdown starts here
openrecent = tk.Menu(mainmenu)
openrecent.add_command(label = "File 1 12.1.24")
openrecent.add_command(label = "File 2 13.1.24")
openrecent.add_command(label = "File 3 14.1.24")
openrecent.add_command(label = "File 4 15.1.24")

filemenu.add_cascade(label = "Open recent", menu = openrecent)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = root.quit)

mainmenu.add_cascade(label = "File", menu = filemenu)

# Edit Menu starts here
editmenu= tk.Menu(mainmenu, tearoff = 0)

editmenu.add_command(label = "Undo")
editmenu.add_command(label = "Redo")
editmenu.add_separator()
editmenu.add_command(label = "Copy")
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Paste")
editmenu.add_separator()
editmenu.add_command(label = "Find")
editmenu.add_command(label = "Replace")

mainmenu.add_cascade(label = "Edit", menu = editmenu)

# View Menu starts here
viewmenu= tk.Menu(mainmenu, tearoff = 0)

viewmenu.add_checkbutton(label = "Terminal")
viewmenu.add_checkbutton(label = "Explorer")
viewmenu.add_separator()
viewmenu.add_radiobutton(label = "Menu")
viewmenu.add_radiobutton(label = "Panel")
viewmenu.add_radiobutton(label = "Output")
viewmenu.add_separator()
viewmenu.add_command(label = "Problems")
viewmenu.add_command(label = "Debug Consol")

mainmenu.add_cascade(label = "View", menu = viewmenu)

root.config(menu = mainmenu)

root.mainloop()
