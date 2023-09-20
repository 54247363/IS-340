import tkinter

class sharon():
  def __init__(self):
    self.main_window = tkinter.Tk()
    self.main_window.title('feedback')


    feedback = 'I learned how to properly utilize terminal (mac) to install and uninstall items and found out how satisfying it is when my code works'

    self.label1 = tkinter.Label(text= feedback)

    self.label1.pack()

if __name__ == '__main__':
    my_gui = sharon()

