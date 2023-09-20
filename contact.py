from tkinter import *
from tkinter import ttk


class app:
    def __init__(self, master):
        self.master = master
        self.master.geometry("200x200")
        self.login()
    
    def login(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.f_name = Entry(root, width =30)
        self.f_name.grid(row = 0, column = 1, padx = 20)
        self.f_name_label = Label(root, text = "First Name")
        self.f_name_label.grid(row = 0, column = 0)

        self.l_name = Entry(root, width =30)
        self.l_name.grid(row = 1, column = 1, padx = 20)
        self.l_name_label = Label(root, text = "Last Name")
        self.l_name_label.grid(row = 1, column = 0)

        self.address = Entry(root, width =30)
        self.address.grid(row = 2, column = 1, padx = 20)
        self.address_label = Label(root, text = "Address")
        self.address_label.grid(row = 2, column = 0)

        self.phone = Entry(root, width =30)
        self.phone.grid(row = 3, column = 1, padx = 20)
        self.phone_label = Label(root, text = "Phone")
        self.phone_label.grid(row = 3, column = 0)
    
    def register(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame2 = Frame(self.master, width=300, height=300)
        self.frame2.pack()
        self.reg_txt2 = ttk.Label(self.frame2, text='register')
        self.reg_txt2.pack()
        self.login_btn = ttk.Button(self.frame2, text="Go to Login", command=self.login)
        self.login_btn.pack()

root = Tk()
app(root)
root.mainloop()
