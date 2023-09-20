import tkinter

    
class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Latin-English Translator')
        self.top_frame = tkinter.Frame(height = 200, width = 200)
        self.bottom_frame = tkinter.Frame(height = 50, width = 200)

        def left():
            self.label3.configure (text ='left')
        def right():
            self.label3.configure (text ='right')
        def center():
            self.label3.configure (text ='center')
        
#English translations
        self.label2 = tkinter.Label(self.bottom_frame,
                                text='English Translation is:')
        self.label3 = tkinter.Label(self.bottom_frame,
                                text=" ")
        
# latin
        self.label1 = tkinter.Label(self.top_frame, text='Latin word is:')

        self.Button1 = tkinter.Button(self.top_frame,
                                text='sinister', command = left)
        self.Button2 = tkinter.Button(self.top_frame,
                                text='dexter', command = right)
        self.Button3 = tkinter.Button(self.top_frame,
                                text='medium', command = center)
        
#packing
        self.label1.pack(side='left')
        self.label2.pack(side='left')
        self.label3.pack(side='left')
        self.Button1.pack(side='left')
        self.Button2.pack(side='left')
        self.Button3.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()
    
        tkinter.mainloop()
if __name__ == '__main__':
    my_gui = MyGUI()
