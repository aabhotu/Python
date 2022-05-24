
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox

window = tk.Tk()
window.title('my window')
window.geometry("800x800")

# them label1
lb1 = tk.Label(window, text="Hello everybody", fg="red", font=("Arial", 50))
lb1.grid(column=0, row=0)

# them Textbox
txt1 = Entry(window, width=20)
txt1.grid(column=0, row=1)


def handleButton():
    lb1.config(text="Hi, " + txt1.get())
    return


# them Button
btn1 = Button(window, text="Click me!", command=handleButton)
btn1.grid(column=1, row=1)

# them ComboBox


def handleButton2():
    lb1.config(text="Hi, " + combo.get())
    # messagebox.showinfo("Hi, " + combo.get())
    return


combo = Combobox(window)
combo['value'] = ("Ban 1", "Ban 2", "Ban 3")
combo.current(0)
combo.grid(column=0, row=2)

btn2 = Button(window, text="Click me!", command=handleButton2)
btn2.grid(column=1, row=2)

window.mainloop()
