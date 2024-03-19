from atexit import register
from calendar import c
from select import select
from tabnanny import check
from tkinter import *
import tkinter as tk
from tkinter import ttk
from unicodedata import name

root = tk.Tk()
root.geometry('650x850')
root.title("Registration Form")
root.configure(bg="gray")

name_label = Label(root,text=" Name :",width=15,height=3,padx=7,pady=7)
name_entry = Entry(root,width=18,font=("Arial",35))

name_label.grid(row=1,column=0,padx=7,pady=7)
name_entry.grid(row=1,column=1,padx=7,pady=7)

age_label = Label (root,text="Age :",width=15,height=3,padx=7,pady=7)
age_var = StringVar()
age_list = ["17","18","19","20","21","22","23","24","25","26","27"
,"28","29","30","31","32","33","34","35","36"]
age_combo = ttk.Combobox(root, textvariable= age_var, value=age_list,width=18,font=("Arial",35))

age_label.grid(row=2,column=0,padx=7,pady=7)
age_combo.grid(row=2,column=1,padx=7,pady=7)

sex_label = Label (root,text="Sex : ",width=15,height=3,padx=7,pady=7)
sex_var = StringVar()
male_button = Radiobutton(root,text="MALE",value="Male Selected",variable=sex_var,font=("Arial",10))
female_button = Radiobutton(root,text="FEMALE",value="Female Selected",variable=sex_var,font=("Arial",10))

sex_label.grid(row=3,rowspan=2,column=0,padx=7,pady=7)
male_button.grid(row=3,column=1,padx=7,pady=7,sticky=W)
female_button.grid(row=4,column=1,padx=7,pady=7,sticky=W)

course_label = Label(root,text="Course : ",width=15,height=3,padx=7,pady=7)
selected_course = []
def addtolist (any_var,checkbutton):
    if any_var == 1 :
        dtext = checkbutton.cget("text")
        selected_course.append(dtext)
        print(checkbutton,"CHECKED")
        print(selected_course)
    if any_var == 0 :
        dtext = checkbutton.cget("text")
        if dtext in selected_course:
            selected_course.remove(dtext)
            print("UNCHECKED")
            print(selected_course)

course_var = IntVar()
math = Checkbutton (root,text="Mathematics",variable=course_var,command=lambda:addtolist(course_var.get(),math))
course_var2 = IntVar()
physics = Checkbutton (root,text="Physics",variable=course_var2,command=lambda:addtolist(course_var2.get(),physics))
course_var3 = IntVar()
program = Checkbutton (root,text="Programming",variable=course_var3,command=lambda:addtolist(course_var3.get(),program))

course_label.grid(row=6,column=0,padx=7,pady=7)
math.grid(row=6,column=1,padx=7,pady=7,sticky=NW)
physics.grid(row=6,column=1,padx=7,pady=7,sticky=W)
program.grid(row=6,column=1,padx=7,pady=7,sticky=SW)

department_label = Label(root,text="Department :",width=15,height=3,padx=7,pady=7)
department_var = StringVar()
department_list = ["BSIT","BSE","BSPA"]
department_combo = ttk.Combobox(root,textvariable=department_var,value=department_list,width=18,font=("Arial",35))

department_label.grid(row=7,column=0,padx=7,pady=7)
department_combo.grid(row=7,column=1,padx=7,pady=7)

year_label = Label(root,text="YEAR :",width=15,height=3,padx=7,pady=7)
year_var = StringVar()
year_list = ["2019","2020","2021","2022","2023"]
year_combo = ttk.Combobox(root,textvariable=year_var,value=year_list,width=18,font=("Arial",35))

year_label.grid(row=8,column=0,padx=7,pady=7)
year_combo.grid(row=8,column=1,padx=7,pady=7)

address_label = Label(root,text="Address :",width=15,height=3,padx=7,pady=7)
address_text = Text(root,width=55,height=3,padx=7,pady=7)

address_label.grid(row=9,column=0,padx=7,pady=7)
address_text.grid(row=9,column=1,padx=7,pady=7)

phone_label = Label(root,text="Phone :",width=15,height=3,padx=7,pady=7)
phone_text = Text(root,width=55,height=3,padx=7,pady=7)

phone_label.grid(row=10,column=0,padx=7,pady=7)
phone_text.grid(row=10,column=1,padx=7,pady=7)

description_label = Label(root,text="Description :",width=15,height=3,padx=7,pady=7)
description_text = Text(root,width=55,height=3,padx=7,pady=7)

description_label.grid(row=11,column=0,padx=7,pady=7)
description_text.grid(row=11,column=1,padx=7,pady=7)

register_button = Button(root,text="REGISTER",width=15,height=3,padx=7,pady=7)

register_button.grid(row=12,column=1,padx=7,pady=7,sticky=W)



root.mainloop()