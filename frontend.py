from tkinter import *
from backend import Database

database=Database("books.db")

def get_selected_row(event): 
    if len(list1.curselection()) > 0:       # or apply try catch
        global selected_tuple  # defining global var
        print(list1.curselection())
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)  # from the listbox get the tuple with index xy
        print(selected_tuple)
        e1.delete(0, END) 
        e1.insert(END, selected_tuple[1])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[2])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[3])   
        e4.delete(0, END) 
        e4.insert(END, selected_tuple[4])
    else:
        pass
        
def view_command():
    list1.delete(0, END) # clear all from idx 0 to the END (last row)
    for i in database.view():
        list1.insert(END, i)  # after the last row

def search_command():   # we use GET because title_input is sctring object, not a pure string. Get() will fetch the object value
    list1.delete(0, END)
    for i in database.search(title_input.get(), author_input.get(), year_input.get(), isbn_input.get()):
        list1.insert(END, i)

def add_entry_command(): 
    database.add_entry(title_input.get(), author_input.get(), year_input.get(), isbn_input.get())
    list1.insert(END, "Entry added succesfully: ", title_input.get(), author_input.get(), year_input.get(), isbn_input.get())

def update_command(): 
    database.update(selected_tuple[0],title_input.get(), author_input.get(), year_input.get(), isbn_input.get())
    list1.insert(END, "Entry was updated.")

def delete_command(): 
    database.delete(selected_tuple[0])
    list1.insert(END, "Entry was deleted")       

window=Tk()
window.wm_title("Book Storage")         # names the window

l1=Label(window, text="Title")
l1.grid(row=0, column=0)
title_input=StringVar()
e1=Entry(window, textvariable=title_input)
e1.grid(row=0, column=1)

l2=Label(window, text="Year")
l2.grid(row=1, column=0)
year_input=IntVar()
e2=Entry(window, textvariable=year_input)
e2.grid(row=1, column=1)

l3=Label(window, text="Author")
l3.grid(row=0, column=2)
author_input=StringVar()
e3=Entry(window, textvariable=author_input)
e3.grid(row=0, column=3)

l4=Label(window, text="ISBN")
l4.grid(row=1, column=2)
isbn_input=IntVar()
e4=Entry(window, textvariable=isbn_input)
e4.grid(row=1, column=3)

list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
sb1=Scrollbar(window) # sb=scrollbar
sb1.grid(row=2, column=2, rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>', get_selected_row) # return type event

b1=Button(window, text="View all", height=1, width=10, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search entry", height=1, width=10, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add entry", height=1, width=10, command=add_entry_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update", width=10, command=update_command)  # default value to width&height are 1, so only one is passed 
b4.grid(row=5, column=3)

b5=Button(window, text="Delete", height=1, width=10, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", height=1, width=10, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()

