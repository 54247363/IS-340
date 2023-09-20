import tkinter
from tkinter import *


class MyGUI:
    def __init__(self):
        self.__price = 0
        self.main_window = tkinter.Tk()
        self.main_window.title('Automotive')
        x = IntVar()
        def total():
            total = 0
            for var in (CheckVar1, CheckVar2, CheckVar3, CheckVar4, CheckVar5, CheckVar6, CheckVar7):
                total += var.get()
                self.label2.config(text="${}.00".format(total))
        #
        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()
        CheckVar4 = IntVar()
        CheckVar5 = IntVar()
        CheckVar6 = IntVar()
        CheckVar7 = IntVar()

        self.check_button1 =tkinter.Checkbutton(text="Oil Change -$30.00",
                                                onvalue=30,
                                                offvalue=0,
                                                command= total,
                                                variable = CheckVar1)
        self.check_button2 =tkinter.Checkbutton(text="Lube Job -$20.00",
                                                onvalue=20,
                                                offvalue=0,
                                                command= total,
                                                variable = CheckVar2)
        self.check_button3 =tkinter.Checkbutton(text="Radiator Flush -$40.00",
                                                onvalue=40,
                                                offvalue=0,
                                                command= total,
                                                variable = CheckVar3)
        self.check_button4 =tkinter.Checkbutton(text="Transmission Flush -$100.00",
                                                onvalue=100,
                                                offvalue=0,
                                                command= total,
                                                variable = CheckVar4)
        self.check_button5 =tkinter.Checkbutton(text="Inspection -$35.00",
                                                onvalue=35,
                                                offvalue=0,
                                                command= total,
                                                variable = CheckVar5)
        self.check_button6 =tkinter.Checkbutton(text="Muffler Replacement -$200.00",
                                                onvalue=200,
                                                offvalue=0,
                                                command= total,
                                                variable = CheckVar6)
        self.check_button7 =tkinter.Checkbutton(text="Tire rotation -$20.00",
                                                onvalue=20,
                                                offvalue=0,
                                                command= total,
                                                variable = CheckVar7)
        self.label1 = tkinter.Label(text= "Total:")
        self.label2 = tkinter.Label(text= 0)
        
        # Pack 
        self.check_button1.pack()
        self.check_button2.pack()
        self.check_button3.pack()
        self.check_button4.pack()
        self.check_button5.pack()
        self.check_button6.pack()
        self.check_button7.pack()
        self.label1.pack()
        self.label2.pack()

        # Start the mainloop.
        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()
