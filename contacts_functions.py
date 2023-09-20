def find():
	
	Listbox.tag_remove('found', '1.0', END)
	ser = modify.get()
	if ser:
		idx = '1.0'
		while 1:
			idx = Listbox.search(ser, idx, nocase=1,
							stopindex=END)
			if not idx: break
			lastidx = '%s+%dc' % (idx, len(ser))
			
			Listbox.tag_add('found', idx, lastidx)
			idx = lastidx
		Listbox.tag_config('found', foreground='blue')
	modify.focus_set()
buttn.config(command=find)

scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

#display selected item
def Selected():
    return int(select.curselection()[0])

def Add():
    contactlist.append([FName.get(), LName.get(), Address.get(), Email.get(), Phone.get()])
    Select_set()
    #clear boxes after add
    reset()

def EDIT():
    contactlist[Selected()] = [FName.get(), LName.get(), Address.get(), Email.get(), Phone.get()]
    Select_set()


def DELETE():
    del contactlist[Selected()]
    Select_set()



def VIEW():
    FNAME, LNAME, ADDRESS, EMAIL, PHONE = contactlist[Selected()]
    FName.set(FNAME)
    LName.set(LNAME)
    Address.set(ADDRESS)
    Email.set(EMAIL)
    Phone.set(PHONE)

def reset():
    #clear text boxes
    FName.set('')
    LName.set('')
    Address.set('')
    Email.set('')
    Phone.set('')

def EXIT():
    root.destroy()

def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for lname, FName, address, email, phone in contactlist :
        select.insert (END, FName + ', ' + lname)
Select_set()