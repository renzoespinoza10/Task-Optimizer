import tkinter as tk
from tkinter import filedialog, Text
import os
import pandas as pd
import webbrowser

# Set the root of the GUI
root = tk.Tk()
root.title("Task Optimizer")

global on_off
on_off = False
programs = []


def into_excel():
    path = "meetingschedule.xlsx"
    data = pd.read_excel(path)
    dates = data["Date"]
    times = data["Time"]
    programas = data["Programs"]
    time_val = pd.Series(time_entry.get())
    date_val = pd.Series(time_entry2.get())
    programs_val = pd.Series(programs)
    dates = dates.append(date_val)
    times = times.append(time_val)
    programas = programas.append(programs_val)
    data2 = pd.DataFrame({"Date": dates, "Time": times, "Programs": programas})
    data2.to_excel(path, index=False)


def add_program():
    for label in frame3.winfo_children():
        label.destroy()
    file = filedialog.askopenfilename(initialdir="/", title="Select File",
                                      filetypes=(("executables", "*.exe"), ("all file types", "*.*")))
    programs.append(file)

    for prog in programs:
        label = tk.Label(frame3, text=prog, font=("Helvetica", 7), bg="grey")
        label.pack()


def run():
    for prog in programs:
        os.startfile(prog)


def submission():
    alarm = time_entry.get()
    ttime = tk.Label(frame1, text=('Event is registered at', alarm),  pady=20, bg='#ffbf00')
    ttime.pack()
    run()
    into_excel()
    time_entry.delete(0, "end")
    time_entry2.delete(0, "end")
    root.update()
    root.after(2000, ttime.destroy())


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
label3 = tk.Label(frame2, text="Enter the \n execution \ndate", bg="orange")
label3.place(rely=0.75)
time_entry = tk.Entry(frame2)
time_entry.insert(-1, "HH:MM (Military)")
time_entry.pack(side="right")
time_entry2 = tk.Entry(frame2)
time_entry2.insert(-1, "DD/MM/YYYY")
time_entry2.place(relx=0.45, rely=0.75)
print(time_entry)

frame3 = tk.Frame(frame1, bg="green")
frame3.place(relwidth=0.5, relheight=0.6, relx=0.5)
frame4 = tk.Frame(canvas, bg="green")
frame4.place(relwidth=0.23, relheight=0.1, rely=0.5, relx=0.62)
program_button = tk.Button(frame4, text="Add a Program", command=add_program)
program_button.pack()
# program_button.place(relx=0.5, rely=0.8, anchor="center")

website = tk.Button(frame4, text="Enter a Website")
website.place(relwidth=0.8, relheight=0.4, relx=0.1, rely=0.6)


add = tk.Button(frame1, text="Submit \n Event", padx=4, pady=2, command=submission)
add.place(relx=0.5, rely=0.7, anchor="center")

label4 = tk.Label(canvas, text="Use Google Calendar Schedule?")
label4.place(relx=0.35, rely=0.1)
"""
on = tk.PhotoImage(file="on3.png")
off = tk.PhotoImage(file="off3.png")
toggle = tk.Button(canvas, image=off, command=switch, bd=0, bg='#47A3BF')
toggle.pack()
"""

root.mainloop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
