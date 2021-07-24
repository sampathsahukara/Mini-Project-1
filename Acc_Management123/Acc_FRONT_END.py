from tkinter import *
import acc_detail

window = Tk()
window.title("         !!!~~~~~~~~Account Management System by SAMPATH~~~~~~~~!!!")
width = 570
height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry("%dx%d+%d+%d" % (width, height, x, y))
window.resizable(0, 0)
window.config(bg="#eaf2f8")




def view_command():
    lb.delete(0, END)
    for row in acc_detail.viewall():
        lb.insert(END, row)


def search_command():
    lb.delete(0, END)
    for row in acc_detail.search(name=name.get(), user=user.get(), password=password.get(), category=category.get()):
        lb.insert(END, row)


def add_command():
    acc_detail.add(name.get(), user.get(), password.get(), category.get(), cdate.get(), mobile.get())
    lb.delete(0, END)
    lb.insert(END, name.get(), user.get(), password.get(), category.get(), cdate.get(), mobile.get())


def get_selected_row(event):
    try:
        global selected_tuple
        index = lb.curselection()[0]
        selected_tuple = lb.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
        e5.delete(0, END)
        e5.insert(END, selected_tuple[5])
        e6.delete(0, END)
        e6.insert(END, selected_tuple[6])

    except IndexError:
        pass


def update_command():
    acc_detail.update(selected_tuple[0], name.get(), user.get(), password.get(), category.get(), cdate.get(),mobile.get())
    view_command()


def delete_command():
    acc_detail.delete(selected_tuple[0])
    view_command()


def clear_command():
    lb.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)


l1 = Label(window, text="Name",bg="#f2d7d5")
l1.grid(row=0, column=0, columnspan=2)
l2 = Label(window, text="Username/Email",bg="#f9ebea")
l2.grid(row=1, column=0, columnspan=2)
l3 = Label(window, text="Password",bg="#ebdef0")
l3.grid(row=2, column=0, columnspan=2)
l4 = Label(window, text="Category",bg="#d4e6f1")
l4.grid(row=3, column=0, columnspan=2)
l5 = Label(window, text="Date",bg="#d1f2eb")
l5.grid(row=4, column=0, columnspan=2)
l6 = Label(window, text="Mobile Number",bg="#fdebd0")
l6.grid(row=5, column=0, columnspan=2)

name = StringVar()
e1 = Entry(window, textvariable=name, width=50)
e1.grid(row=0, column=0, columnspan=10)

user = StringVar()
e2 = Entry(window, textvariable=user, width=50)
e2.grid(row=1, column=0, columnspan=10)

password = StringVar()
e3 = Entry(window, textvariable=password, width=50)
e3.grid(row=2, column=0, columnspan=10)

category = StringVar()
e4 = Entry(window, textvariable=category, width=50)
e4.grid(row=3, column=0, columnspan=10)

cdate = StringVar()
e5 = Entry(window, textvariable=cdate, width=50)
e5.grid(row=4, column=0, columnspan=10)

mobile = StringVar()
e6 = Entry(window, textvariable=mobile, width=50)
e6.grid(row=5, column=0, columnspan=10)

b1 = Button(window, text="Add", width=12, command=add_command,bg="#fdfefe")
b1.grid(row=6, column=0)

b2 = Button(window, text="Update", width=12, command=update_command,bg="#fbfcfc")
b2.grid(row=6, column=2)

b3 = Button(window, text="Search", width=12, command=search_command,bg="#f5cba7")
b3.grid(row=6, column=3)

b4 = Button(window, text="View All", width=12, command=view_command,bg="#f9e79f")
b4.grid(row=6, column=1)

b5 = Button(window, text="Delete", width=12, command=delete_command,bg="#a3e4d7")
b5.grid(row=6, column=4)

b6 = Button(window, text="Cancel", width=12, command=window.destroy,bg="#aed6f1")
b6.grid(row=6, column=5)

b7 = Button(window, text="Clear All", width=12, command=clear_command,bg="#d7bde2")
b7.grid(row=0, column=5)

lb = Listbox(window, height=20, width=94)
lb.grid(row=7, column=0, columnspan=6)

sb = Scrollbar(window)
sb.grid(row=7, column=6, rowspan=6)

lb.configure(yscrollcommand=sb.set)
sb.configure(command=lb.yview)

lb.bind('<<ListboxSelect>>', get_selected_row)
window.mainloop()
