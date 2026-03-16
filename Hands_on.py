
import tkinter as tk

window = tk.Tk()
window.title("Profile Builder")
window.resizable(False,False)
window.geometry("700x300")
window.configure(bg="Light Green")

window = tk.Label(window,text="Profile Builder",font=("arial"),bg="Light Green")
window.grid(column=5,row=0,rowspan=2,padx=300)

nemu = tk.Label(window,text="First Name",font=("Italic"),bg="Light Green")
nemu.grid(row=3,column=2,pady=50,padx=10)

first = tk.Entry(window)
first.grid(column=0,row=2,rowspan=2,pady=50)



window.mainloop()
