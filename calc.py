import tkinter as tk

window = tk.Tk()

window.title("Simple calculator")
window.geometry("300x300")
window.resizable(False,False)



def lahat(operation):
    first = number_entry.get()
    second = number_entry2.get()

    if operation == "1":
        addsum = int(first) + int(second)
        operator = "+"
        update_text(first,second,operator,addsum)

    elif operation == "2":
        addsum = int(first) * int(second)
        operator = "x"
        update_text(first,second,operator,addsum)

    elif operation == "3":
        addsum = int(first) - int(second)
        operator = "-"
        update_text(first,second,operator,addsum)

    elif operation == "4":
        addsum = int(first) // int(second)
        operator = "%"
        update_text(first,second,operator,addsum)

    
    return


output = tk.Label(window, text="calc", fg="black",font= ("arial"))
output.grid(row=0,column=2,columnspan=10,padx=10,pady=10)

number = tk.Label(window,text="Enter 1st number:", fg="black")
number.grid(row=1,column=2,columnspan=3,padx=10,pady=20)

number2 = tk.Label(window,text="Enter 2nd number:", fg="black")
number2.grid(row=2,column=2,columnspan=3,padx=10,pady=20)

number_entry = tk.Entry(window)
number_entry.grid(row=1,column=5,columnspan=3,padx=1,pady=20)

number_entry2 = tk.Entry(window)
number_entry2.grid(row=2,column=5,columnspan=3,padx=1,pady=20)

button1 = tk.Button(window,text="addition",command=lambda:lahat("1"))
button1.grid(row=4,column=3,padx=30,pady=10)

button2 = tk.Button(window,text="multiply",command=lambda:lahat("2"))
button2.grid(row=5,column=3,padx=30,pady=10)

button3 = tk.Button(window,text="subtraction",command=lambda:lahat("3"))
button3.grid(row=4,column=5,padx=30,pady=10)

button4 = tk.Button(window,text="division",command=lambda:lahat("4"))
button4.grid(row=5,column=5,padx=30,pady=10)


def update_text(first,second,operator,addsum):
    output.configure(text=f"{first} {operator} {second} is {addsum}")


window.mainloop()
