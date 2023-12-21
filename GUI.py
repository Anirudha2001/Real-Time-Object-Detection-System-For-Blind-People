from tkinter import Tk
import tkinter as tk
import os

window = tk.Tk()
window.geometry("600x600")
window.title("Object Detection")

window.configure(background="lightblue")

Heading = tk.Label(window, text="Voice Based Object Detection for Blind Person",
                   fg="gray", font=("arial 12 bold underline"), bg="lightblue")
Heading.pack(side="top")


def exitbutton():
    exit()


def voice():
    os.system('python run.py')


def manual():
    os.system('python main.py')


button1 = tk.Button(window, text="Voice", font="arial 10 bold",
                    width=15, command=voice).place(x=20, y=50)

button2 = tk.Button(window, text="Manual",
                    font="arial 10 bold", width=15, command=manual).place(x=20, y=90)

button3 = tk.Button(window, text="Help", font="arial 10 bold",
                    width=15).place(x=20, y=130)

button4 = tk.Button(window, text="Exit", font="arial 10 bold",
                    width=15, command=exitbutton).place(x=20, y=170)


window.mainloop()
