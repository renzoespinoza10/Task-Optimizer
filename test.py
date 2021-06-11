import tkinter as tk
from tkinter import filedialog, Text
import os

# Set the root of the GUI
root = tk.Tk()
root.title("Task Optimizer")

global on_off
on_off = False


def add_program():
    programs = []
    file = filedialog.askopenfilename(initialdir="/", title="Select File",
                                      filetypes=(("executables", "*.exe"), ("all file types", "*.*")))
    programs.append(file)
    y_pos = 0.25
    for prog in programs:
        label = tk.Label(frame3, text=file, font=("Helvetica", 7), bg="grey")
        label.pack(side="top")
        program_button.place(relx=0.5, rely=y_pos, anchor="center")
        y_pos -= .03


def switch():
    global on_off
    if on_off == False:
        toggle.config(image=on)
        on_off = True
    else:
        toggle.config(image=off)
        on_off = False


canvas = tk.Canvas(root, height=600, width=500, bg='#47A3BF')
canvas.pack(expand=True, fill="both")

label1 = tk.Label(canvas, text="Task Optimizer", bg="#47A3BF")
label1.configure(font=("Times New Roman", 18, "bold"))
canvas.create_window(260, 20, window=label1)

frame1 = tk.Frame(canvas, bg="white")
frame1.place(relwidth=0.9, relheight=0.7, relx=0.05, rely=0.2)

frame2 = tk.Frame(frame1, bg="orange")
frame2.place(relwidth=0.5, relheight=0.6)
label2 = tk.Label(frame2, text="Enter the \n execution \ntime", bg="orange")
label2.pack(side="left")
time_entry = tk.Entry(frame2)
time_entry.pack(side="right")
print(time_entry)

frame3 = tk.Frame(frame1, bg="green")
frame3.place(relwidth=0.5, relheight=0.6, relx=0.5)
program_button = tk.Button(frame3, text="Enter the Program", command=add_program)
program_button.place(relx=0.5, rely=0.8, anchor="center")

add = tk.Button(frame1, text="Submit \n Event", padx=4, pady=2)
add.place(relx=0.5, rely=0.7, anchor="center")

label4 = tk.Label(canvas, text="Use Google Calendar Schedule?")
label4.pack(side="top")
on = tk.PhotoImage(file="on2.png")
off = tk.PhotoImage(file="off2.png")
toggle = tk.Button(canvas, image=off, command=switch, bd=0)
toggle.pack()


root.mainloop()
