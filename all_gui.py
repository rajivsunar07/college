from tkinter import *
from tkinter import ttk




def registerwindow():
    new = Toplevel()
    new.geometry('470x450+450+100')
    new.title('Registration Form')
    new.resizable(False,False)




    Headinglbl = Label(new, text='Registration Form', bg='Gray', width = 50 )
    Headinglbl.grid(columnspan=2, padx=4, pady=8)

    def commandbtn():
        id_info =  id.get()
        id_info1 = str(id_info)
        name_info = name.get()
        age_info = age.get()
        age_info1 = str(age_info)
        address_info = address.get()
        contact_info = contact.get()
        contact_info1 = str(contact_info)

        print(id_info1, name_info, age_info1, address_info, contact_info1)

        file = open('assignment.txt', 'w')
        file.write(id_info1, end='')
        file.write(name_info, end='')
        file.write(age_info1, end='')
        file.write(address_info, end='')
        file.write(contact_info1, end='')
        file.close()

    def programfunc():
        program = Toplevel()
        program.geometry('500x500+450+100')
        program.title('Program Form')

        program_code_option = ['120COM', '121ETH']
        program_name_option = ['BSc. (Hons) Computing', 'BSc. (Hons) Ethical Hacking and Cybersecurity']



        formlbl = Label(program, text = 'Program Form', bg ='Gray', width = 55)
        formlbl.grid(columnspan = 2, padx=4, pady=8)

        programcodelbl =Label(program, text = 'Program Code')
        programcodeentry = ttk.Combobox(program, values=program_code_option , width=35)
        programcodeentry.set('-Enter the program code-')

        programnamelbl = Label(program, text = 'Program Name')
        programnameentry = ttk.Combobox(program, values=program_name_option, width=35)
        programnameentry.set('-Enter the program name-')

        submitbtn1 = ttk.Button(program, text='Submit')
        resetbtn1 = ttk.Button(program, text='Reset')

        programcodelbl.grid(row = 1, column = 0, padx =4, pady=4)
        programcodeentry.grid(row =1, column = 1, padx =4, pady=4)
        programnamelbl.grid(row = 2, column=0, padx =4, pady=4)
        programnameentry.grid(row = 2, column =1, padx =4, pady=4)
        submitbtn1.grid(row = 3, columnspan=2, padx=4, pady=4)
        resetbtn1.grid(row=4, columnspan=2, padx =4, pady=4)



    def reset_func():
        identry.delete(0,END)
        nameentry.delete(0,END)
        ageentry.delete(0,END)
        addressentry.delete(0,END)
        contactentry.delete(0,END)


    id = IntVar()
    name = StringVar()
    age = IntVar()
    address = StringVar()
    contact = IntVar()

    idlbl = Label(new, text='ID')
    identry = Entry(new, textvariable=id )

    namelbl = Label(new, text='Name')
    nameentry = Entry(new, textvariable = name)

    agelbl = Label(new, text='Age')
    ageentry = Entry(new, textvariable = age)

    addresslbl = Label(new, text='Address')
    addressentry = Entry(new, textvariable = address)

    contactlbl = Label(new, text='Contact')
    contactentry = Entry(new, textvariable = contact)

    programlbl = Label(new, text='Programme Form')
    programbtn = ttk.Button(new, text = 'Enter Program information', command = programfunc )

    submitbtn = ttk.Button(new, text = 'SUBMIT', width = 15, command = commandbtn)
    resetbtn = ttk.Button(new, text = 'RESET', width = 15, command =reset_func)
    gobackbtn = ttk.Button(new, text = 'Go Back', width = 10, command=new.destroy)

    idlbl.grid(row = 1, column = 0, sticky= E,padx=4, pady=4)
    identry.grid(row = 1, column = 1,padx=4, pady=4)
    namelbl.grid(row = 2, column = 0, sticky= E, padx=4, pady=4)
    nameentry.grid(row = 2, column = 1,padx=4, pady=4)
    agelbl.grid(row = 3, column = 0, sticky= E,padx=4, pady=4)
    ageentry.grid(row = 3, column = 1,padx=4, pady=4)
    addresslbl.grid(row = 4, column = 0, sticky= E,padx=4, pady=4)
    addressentry.grid(row = 4, column = 1,padx=4, pady=4)
    contactlbl.grid(row = 5, column = 0, sticky= E,padx=4, pady=4)
    contactentry.grid(row = 5, column = 1,padx=4, pady=4)
    programlbl.grid(row = 6, column = 0, sticky = E,  padx=4, pady=4)
    programbtn.grid(row = 6, column =1, padx =4, pady=4)
    submitbtn.grid(row = 7, columnspan=2, padx=4, pady=4)
    resetbtn.grid(row =8, columnspan = 2, padx=4, pady=4)
    gobackbtn.grid(row=9, columnspan =2,  padx=4, pady=4)

    identry.delete(0, END)
    nameentry.delete(0, END)
    ageentry.delete(0, END)
    addressentry.delete(0, END)
    contactentry.delete(0, END)

root = Tk()
root.title('Student Management System')
root.geometry('1500x1500+450+180')


Headinglbl = Label(root, text = 'Student Management System', bg = 'Gray', fg = 'White', width=50)
Headinglbl.grid(row = 0, column = 3, padx = 4, pady=4)

Registerbtn = ttk.Button(root, text = 'Register', width = 15, command = registerwindow )
Registerbtn.grid(row = 2, column = 3, padx=4, pady=4)

Viewbtn = ttk.Button(root, text = 'View', width = 15)
Viewbtn.grid(row = 4, column = 3, padx=4, pady=4)

Quitbtn = ttk.Button(root, text = 'Quit', width = 10, command= root.destroy)
Quitbtn.grid(row = 7, column = 3, padx=4, pady=4)



root.mainloop()
