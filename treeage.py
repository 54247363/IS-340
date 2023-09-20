
import tkinter

class MyGUI:
    def __init__(self):
    # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title('Treeage')

        # Create the Canvas widget.
        self.canvas = tkinter.Canvas(self.main_window,
                width=210,height=210)

        # treerings
        self.canvas.create_oval(90, 90, 120, 120)
        self.canvas.create_oval(70, 70, 140, 140)
        self.canvas.create_oval(50, 50, 160, 160)
        self.canvas.create_oval(30, 30, 180, 180)
        self.canvas.create_oval(10, 10, 200, 200)
        
        #texts
        self.canvas.create_text(125, 105, text='1')
        self.canvas.create_text(145, 105, text='2')
        self.canvas.create_text(165, 105, text='3')
        self.canvas.create_text(185, 105, text='4')
        self.canvas.create_text(205, 105, text='5')
        
        # Pack the canvas.
        self.canvas.pack()

        # Start the mainloop.
        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()
