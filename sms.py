
from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

#Functionality part

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()

    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['Id','name','Mobile','Email','Address','Gender','DOB','Added date','Added time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Succes','Data is saved successfully')


def update_student():
    def update_data():
        query='update set name=%s,mobile=%s,email=%s,address=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(query,(NameEntry.get(),PhoneEntry.get(),EmailEntry.get(),AddressEntry.get(),DOBEntry.get(),date,currenttime,idEntry.get()))

        con.commit()
        messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=update_window)
        update_window.destroy()
        show_student()

    update_window = Toplevel()
    update_window.title('Update Student')
    update_window.grab_set()
    update_window.resizable(0, 0)

    idlabel = Label(update_window, text='Id', font=('times new roman', 20, 'bold'))
    idlabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    Namelabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'))
    Namelabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    NameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    NameEntry.grid(row=1, column=1, pady=15, padx=10)

    Phonelabel = Label(update_window, text='Phone', font=('times new roman', 20, 'bold'))
    Phonelabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    PhoneEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    PhoneEntry.grid(row=2, column=1, pady=15, padx=10)

    Emaillabel = Label(update_window, text='Email', font=('times new roman', 20, 'bold'))
    Emaillabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    EmailEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    EmailEntry.grid(row=3, column=1, pady=15, padx=10)

    Addresslabel = Label(update_window, text='Address', font=('times new roman', 20, 'bold'))
    Addresslabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    AddressEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    AddressEntry.grid(row=4, column=1, pady=15, padx=10)

    Genderlabel = Label(update_window, text='Gender', font=('times new roman', 20, 'bold'))
    Genderlabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    GenderEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    GenderEntry.grid(row=5, column=1, pady=15, padx=10)

    DOBlabel = Label(update_window, text='DOB', font=('times new roman', 20, 'bold'))
    DOBlabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    DOBEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    DOBEntry.grid(row=6, column=1, pady=15, padx=10)

    update_student_button = ttk.Button(update_window, text='Update Student',command=update_data)
    update_student_button.grid(row=7, columnspan=2, pady=15)

    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    listdata=content['values']

    idEntry.insert(0,listdata[0])
    NameEntry.insert(1,listdata[1])
    PhoneEntry.insert(2,listdata[2])
    EmailEntry.insert(3,listdata[3])
    AddressEntry.insert(4,listdata[4])
    GenderEntry.insert(5,listdata[5])
    DOBEntry.insert(6,listdata[6])




def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)



def delete_student():
    indexing=studentTable.focus()

    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'The id {content_id} is deleted successfully ')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

def search_student():
    def search_data():
        query='select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
        mycursor.execute(query,(idEntry.get(),NameEntry.get(),EmailEntry.get(),PhoneEntry.get(),AddressEntry.get(),GenderEntry.get(),DOBEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END,values=data)

    search_window = Toplevel()
    search_window.title('Search Student')
    search_window.grab_set()
    search_window.resizable(0, 0)

    idlabel = Label(search_window, text='Id', font=('times new roman', 20, 'bold'))
    idlabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    Namelabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    Namelabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    NameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    NameEntry.grid(row=1, column=1, pady=15, padx=10)

    Phonelabel = Label(search_window, text='Phone', font=('times new roman', 20, 'bold'))
    Phonelabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    PhoneEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    PhoneEntry.grid(row=2, column=1, pady=15, padx=10)

    Emaillabel = Label(search_window, text='Email', font=('times new roman', 20, 'bold'))
    Emaillabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    EmailEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    EmailEntry.grid(row=3, column=1, pady=15, padx=10)

    Addresslabel = Label(search_window, text='Address', font=('times new roman', 20, 'bold'))
    Addresslabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    AddressEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    AddressEntry.grid(row=4, column=1, pady=15, padx=10)

    Genderlabel = Label(search_window, text='Gender', font=('times new roman', 20, 'bold'))
    Genderlabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    GenderEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    GenderEntry.grid(row=5, column=1, pady=15, padx=10)

    DOBlabel = Label(search_window, text='DOB', font=('times new roman', 20, 'bold'))
    DOBlabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    DOBEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    DOBEntry.grid(row=6, column=1, pady=15, padx=10)

    search_student_button = ttk.Button(search_window, text='Search Student', command=search_data)
    search_student_button.grid(row=7, columnspan=2, pady=15)


def add_student():
    def add_data():
        if idEntry.get()=='' or NameEntry.get()=='' or PhoneEntry.get()=='' or EmailEntry.get()=='' or AddressEntry.get()=='' or GenderEntry.get()=='' or DOBEntry.get()=='' :
            messagebox.showerror('Error','All fields are required',parent=add_window)

        else:

            try:
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(idEntry.get(),NameEntry.get(),PhoneEntry.get(),EmailEntry.get(),AddressEntry.get(),GenderEntry.get()
                                        ,DOBEntry.get(),date,currenttime))
                con.commit()
                result=messagebox.askyesno('Sucess','Data added Successfully. Do you want to clean the form?',parent=add_window)
                if result:
                    idEntry.delete(0, END)
                    NameEntry.delete(0, END)
                    PhoneEntry.delete(0, END)
                    AddressEntry.delete(0, END)
                    EmailEntry.delete(0, END)
                    GenderEntry.delete(0, END)
                    DOBEntry.delete(0, END)

                else:
                    pass

            except:
                messagebox.showerror('Error','Id cannot be repeated',parent=add_window)
                return

            query='select * from student'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children(()))
            for data in fetched_data:
                datalist=list(data)
                studentTable.insert('',END,values=datalist)




    add_window= Toplevel()
    add_window.grab_set()
    add_window.resizable(0,0)

    idlabel = Label(add_window,text='Id',font=('times new roman',20,'bold'))
    idlabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry = Entry(add_window,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    Namelabel = Label(add_window, text='Name', font=('times new roman', 20, 'bold'))
    Namelabel.grid(row=1, column=0, padx=30, pady=15,sticky=W)
    NameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    NameEntry.grid(row=1, column=1, pady=15, padx=10)

    Phonelabel = Label(add_window, text='Phone', font=('times new roman', 20, 'bold'))
    Phonelabel.grid(row=2, column=0, padx=30, pady=15,sticky=W)
    PhoneEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    PhoneEntry.grid(row=2, column=1, pady=15, padx=10)

    Emaillabel = Label(add_window, text='Email', font=('times new roman', 20, 'bold'))
    Emaillabel.grid(row=3, column=0, padx=30, pady=15,sticky=W)
    EmailEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    EmailEntry.grid(row=3, column=1, pady=15, padx=10)

    Addresslabel = Label(add_window, text='Address', font=('times new roman', 20, 'bold'))
    Addresslabel.grid(row=4, column=0, padx=30, pady=15,sticky=W)
    AddressEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    AddressEntry.grid(row=4, column=1, pady=15, padx=10)

    Genderlabel = Label(add_window, text='Gender', font=('times new roman', 20, 'bold'))
    Genderlabel.grid(row=5, column=0, padx=30, pady=15,sticky=W)
    GenderEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    GenderEntry.grid(row=5, column=1, pady=15, padx=10)

    DOBlabel = Label(add_window, text='DOB', font=('times new roman', 20, 'bold'))
    DOBlabel.grid(row=6, column=0, padx=30, pady=15,sticky=W)
    DOBEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    DOBEntry.grid(row=6, column=1, pady=15, padx=10)

    add_student_button=ttk.Button(add_window,text='Add Student',command=add_data)
    add_student_button.grid(row=7,columnspan=2,pady=15)

def connect_database():
    def connect():
        global mycursor,con
        try:
            con= pymysql.connect(host='localhost',user='root',password='1234')
            mycursor=con.cursor()
            messagebox.showinfo('Succes','Connection is successful',parent=connectWindow)
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
        try:
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query=('create table student(Id int not null primary key, name varchar(50),mobile varchar(10),'
                   'Email varchar(30),Address varchar(100),Gender varchar(20),DOB varchar(20),'
                   'date varchar(50),Time varchar(50))')
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database Connection is successful',parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        ShowstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.grab_set()#not allow to minimise or click somewhere else
    connectWindow.geometry('470x250+700+200')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnamelabel=Label(connectWindow,text='Host Name', font=('arial',20,'bold'))
    hostnamelabel.grid(row=0,column=0,padx=20)

    hostEntry = Entry(connectWindow,font=('roman',15,'bold'))
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernamelabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernamelabel.grid(row=1, column=0, padx=20)

    userEntry = Entry(connectWindow, font=('roman', 15, 'bold'))
    userEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordlabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordlabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'))
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton = ttk.Button(connectWindow,text='Connect',command=connect)
    connectButton.grid(row=3,columnspan=1)


count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)

def clock():
    global date,currenttime
    date=time.strftime(('%d/%m/%Y'))
    currenttime= time.strftime(('%H:%M:%S'))
    datetimeLabel.config(text=f'  Date:{date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)


#GUI Part
root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(False,False)
root.title('Student Management System')

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()


s = 'Student Management System'

sliderLabel = Label(root,text=s,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

connectButton=ttk.Button(root,text='Connect to database',command= connect_database)
connectButton.place(x=990,y=0)


# Table options
leftFrame = Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image= PhotoImage(file='student.png')
logolabel = Label(leftFrame,image=logo_image)
logolabel.grid(row=0,column=0)

addstudentButton = ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=add_student)
addstudentButton.grid(row=1,column=0,pady=10)

searchstudentButton = ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=search_student)
searchstudentButton.grid(row=2,column=0,pady=10)

deletestudentButton = ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=10)

updatestudentButton = ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=update_student)
updatestudentButton.grid(row=4,column=0,pady=10)

ShowstudentButton = ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
ShowstudentButton.grid(row=5,column=0,pady=10)

exportstudentButton = ttk.Button(leftFrame,text='Export Student',width=25,state=DISABLED,command=export_data)
exportstudentButton.grid(row=6,column=0,pady=10)

exitButton = ttk.Button(leftFrame,text='Exit',width=15,command=iexit)
exitButton.grid(row=7,column=0,pady=20)

#student data

rightFrame = Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)


studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email','Address',
                                 'Gender','DOB','Added Date','Added Time')
                          ,xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile',text='Mobile')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('DOB',text='DOB')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Mobile',width=200,anchor=CENTER)
studentTable.column('Address',width=250,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=20,font=('arial',12,'italic'),background='white',fieldbackground='white')

studentTable.config(show='headings')

root.mainloop()