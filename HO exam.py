import tkinter as tk

window = tk.Tk()
window.title("Gregorio_HO Exam")
window.geometry("500x200")
window.resizable(False,False)

def register():
    window = tk.Tk()
    window.geometry("300x300")
    window.configure(bg="Green")
    window.resizable(False,False)

    user = tk.Label(window,text="Username",bg="Green")
    user.grid(row=2,column=0,pady=25)

    user_entry = tk.Entry(window)
    user_entry.grid(row=2,column=1)

    passw = tk.Label(window,text="Password:",bg="Green")
    passw.grid(row=3,column=0)

    passw_entry = tk.Entry(window)
    passw_entry.grid(row=3,column=1)

    reg_button = tk.Button(window,text="Register")
    reg_button.grid(row=4,column=1)

    window.mainloop


def login():
    window = tk.Tk()
    window.geometry("300x300")
    window.configure(bg="Green")
    window.resizable(False,False)

    tiks = tk.Label(window,text="Log in",bg="Green",font=("Arial",20))
    tiks.grid(row=0,column=1)

    user = tk.Label(window,text="Username",bg="Green")
    user.grid(row=2,column=0,pady=25)

    user_entry = tk.Entry(window)
    user_entry.grid(row=2,column=1)

    passw = tk.Label(window,text="Password:",bg="Green")
    passw.grid(row=3,column=0)

    passw_entry = tk.Entry(window)
    passw_entry.grid(row=3,column=1)

    lugin_button = tk.Button(window,text="Log In")
    lugin_button.grid(row=4,column=1)

    window.mainloop

first = tk.Label(window,text="Welcome!",font=("arial",20))
first.grid(column=4,row=0,padx=170)

frstbutton = tk.Button(window,text="Register",bg="Blue",command=register)
frstbutton.grid(column=4,row=2,rowspan=100,padx=170,pady=10)

scndbutton = tk.Button(window,text="Log In",bg="Green",command=login)
scndbutton.grid(column=4,row=3,rowspan=100,padx=170,pady=10)

window.mainloop()
