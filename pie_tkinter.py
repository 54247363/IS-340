import tkinter

# init tk
root = tkinter.Tk()

# create canvas
myCanvas = tkinter.Canvas(root, bg="white", height=400, width=400)

# draw arcs
coord = 75, 75, 325, 325
Sports = myCanvas.create_arc(coord, start=0, extent=108, fill="red")
VideoGames = myCanvas.create_arc(coord, start=108, extent=36, fill="blue")
Partying = myCanvas.create_arc(coord, start=144, extent=162, fill="yellow")
Programming = myCanvas.create_arc(coord, start=306, extent=18, fill="purple")
NoIdea = myCanvas.create_arc(coord, start=324, extent=36, fill="green")

# labels
myCanvas.create_text(200, 50, text='HOBBY SURVEY', fill="black")
myCanvas.create_text(325, 125, text='Sports', fill="black")
myCanvas.create_text(75, 100, text='Video Games', fill="black")
myCanvas.create_text(75, 300, text='Partying', fill="black")
myCanvas.create_text(325, 300, text='Programming', fill="black")
myCanvas.create_text(350, 225, text='No Idea', fill="black")

# add to window and show
myCanvas.pack()
root.mainloop()
