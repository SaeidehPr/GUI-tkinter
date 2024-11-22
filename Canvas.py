import tkinter as tk 

root = tk.Tk()
root.title("Drawing with Canvas")
root.minsize(300, 200)

canvas = tk.Canvas(root, bg= "blue", height = 500, width = 500)

rect = 10, 10, 100, 50 # Distance from the left edge, Distance from the top edge 
                       # The width, The height
canvas.create_rectangle(rect, fill="green")

sqr = 10, 10, 50, 50 
canvas.create_rectangle(sqr, fill="orange")

line = 20, 20, 150, 250, 100, 350 # Coordinate of the starting point 
                                  # Coordinate of the end point 
                                  # If you continue, you will have other lines
canvas.create_line(line, fill="red")

oval = 30, 30, 200, 100 # Coordinate of the left, top, bottom and right
canvas.create_oval(oval, fill="gray")

oval = 150, 150, 120, 200 # Coordinate of the left, top, bottom and right
canvas.create_oval(oval, fill="black")

coord = 50, 50, 200, 250 
canvas.create_arc(coord, start = 0, extent = 150, fill="purple")

pol = 150, 150, 200, 250, 100, 400 
canvas.create_polygon(pol, fill="pink")

canvas.pack()

root.mainloop()