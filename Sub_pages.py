from tkinter import *
from tkinter import messagebox
import time as tm
from connection import *
from connection import messages
def sign_up2(root,frame):
    def sign_upto():
        if(entr1.get()!="" and entr2!="" and entr3!=""):
            if(entr2.get()==entr3.get()):
                add_user(entr1.get(),entr2.get())
                messagebox.showinfo("","You are inserted to database succesfully")
                f3.destroy()
                main2(root)
        elif(entr2.get()!=entr3.get()):
            messagebox.showerror("","Passwords are not equal")
        elif(entr1.get()=="" or entr2.get()=="" or entr3.get()==""):
            messagebox.showerror("","All blanks required!")
    def signto():
        main2(root)
    frame.destroy()
    f3=Frame(root,width=400,height=500,bg="white")
    f3.place(x=0,y=0)
    lab1=Label(f3,text="Sign up",font=("Microsoft Yahei UI Light",15,"bold"),bg="white",fg="blue")
    lab1.place(x=150,y=20)
    
    lab2=Label(f3,text="Username",bg="white",fg="black",font=("Klavika",10,"bold"))
    lab2.place(x=60,y=120)
    
    entr1=Entry(f3,width=40,border=0)
    entr1.place(x=60,y=150)
    f4=Frame(f3,width=300,bg="black",height=2)
    f4.place(x=60,y=170)

    lab3=Label(f3,text="password",bg="white",fg="black",font=("Klavika",10,"bold"))
    lab3.place(x=60,y=200)
    
    entr2=Entry(f3,width=40,border=0,show=".")
    entr2.place(x=60,y=230)
    f5=Frame(f3,width=300,bg="black",height=2)
    f5.place(x=60,y=250)

    lab4=Label(f3,text="password again",bg="white",fg="black",font=("Klavika",10,"bold"))
    lab4.place(x=60,y=280)
    
    entr3=Entry(f3,width=40,border=0,show=".")
    entr3.place(x=60,y=310)
    f6=Frame(f3,width=300,bg="black",height=2)
    f6.place(x=60,y=330)

    sign_up_btn=Button(f3,text="sign up",width=12,height=2,bg="#00aced",border=0,fg="white",command=sign_upto)
    sign_up_btn.place(x=160,y=350)

    lab5=Label(f3,text="Back to sign in?",bg="white",fg="black")
    lab5.place(x=160,y=430)
    
    sign2=Button(f3,text="Sign in",bg="white",fg="blue",border=0,command=signto)
    sign2.place(x=180,y=450)
def main2(root):
    def sign_in():
        username=enter1.get()
        password=enter2.get()
        control=False
        for i in get_user():
            if(i["name"]==username and i["password"]==password):
                chat_page(root,username)
                control=True
        if(control==False):
            messagebox.showerror("","There is no user on the system\n try to sign up")
    def sign_up():
        sign_up2(root,frame)
    frame=Frame(width=400,height=500,bg="white")
    frame.place(x=0,y=0)
    label1=Label(frame,text="Login page",font=("Microsoft Yahei UI Light",20,"bold"),bg="white",fg="blue")
    label1.place(x=110,y=50)
    
    label2=Label(frame,text="Username",bg="white",fg="black",font=("Klavika",10,"bold"))
    label2.place(x=60,y=120)
    
    enter1=Entry(frame,width=40,border=0)
    enter1.place(x=60,y=150)
    f1=Frame(frame,width=300,bg="black",height=2)
    f1.place(x=60,y=170)
    label3=Label(frame,text="password",bg="white",fg="black",font=("Klavika",10,"bold"))
    label3.place(x=60,y=200)
    
    enter2=Entry(frame,width=40,border=0,show=".")
    enter2.place(x=60,y=230)
    f2=Frame(frame,width=300,bg="black",height=2)
    f2.place(x=60,y=250)
    
    sign_in_btn=Button(frame,text="sign in",width=8,height=2,bg="#00aced",border=0,fg="white",command=sign_in)
    sign_in_btn.place(x=170,y=280)
    
    label4=Label(frame,text="Don't have a account?",bg="white",fg="black")
    label4.place(x=140,y=430)
    
    sign=Button(frame,text="Sign up",bg="white",fg="blue",border=0,command=sign_up)
    sign.place(x=175,y=450)
def calculate_time():
    year=str(tm.localtime().tm_year)
    month=str(tm.localtime().tm_mon)
    day=str(tm.localtime().tm_mday)
    hour=str(tm.localtime().tm_hour)
    minute=tm.localtime().tm_min
    if(len(month)==1):
        month="0"+month
    if(len(day)==1):
        day="0"+day
    if(len(hour)==1):
        hour="0"+hour
    return "{}/{}/{} ({}:{})".format(day,month,year,hour,minute)
def chat_page(root,username):
    def add_new_message():
        for i in get_message():
            lst=i
        text.insert(END,"{}: ".format(lst["username"])+lst["message"]+"---->{}\n".format(calculate_time()))
    def send_message():
        message=enter.get()
        if(message!=""):
            add_message(message,username,calculate_time())
    def sign_in():
        root1.destroy()
        root=Tk()
        root.title("Chat_page")
        root.geometry("400x500+800+80")
        root.configure(bg="white")
        root.resizable(False,False)
        main2(root)
    root1=Tk()
    root1.geometry("400x500+800+80")
    root1.title("Chat page")
    main_frame=Frame(root1,height=500,width=400,bg="white")
    main_frame.place(x=0,y=0)
    text=Text(main_frame,width=48,bg="white")
    text.place(x=10,y=20)
    if(get_control()!=None):
        for i in get_message():
            text.insert(END,"{}: ".format(i["username"])+i["message"]+"---->{}\n".format(i["date"]))
    enter=Entry(main_frame,width=50,bg="white")
    enter.place(x=35,y=430)
    btn=Button(main_frame,width=7,height=1,text="Send",bg="#00aced",fg="white",border=0,command=send_message)
    btn.place(x=320,y=430)
    Label(main_frame,text="Back to ",bg="white",fg="black").place(x=120,y=460)
    Button(main_frame,text="Sign in",bg="white",fg="#00aced",border=0,command=sign_in).place(x=180,y=460)
    root.destroy()
    length=get_len_of_messages()
    while True:
        len_now=get_len_of_messages()
        if(len_now!=length):
            add_new_message()
            length=len_now
        root1.update()

        
