from tkinter import *
from Sub_pages import main2
from connection import messages
from connection import *
from Sub_pages import *

root=Tk()
root.title("Chat_page")
root.geometry("400x500+800+80")
root.configure(bg="white")
root.resizable(False,False)

main2(root)
root.mainloop()
