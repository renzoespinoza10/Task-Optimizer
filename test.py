import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os
import pandas as pd
import webbrowser

# Set the root of the GUI
root = tk.Tk()
root.title("Task Optimizer")

global on_off
global input_web
on_off = False
global programs
global websites
programs = []
websites = []


def into_excel():
    """
    path = "meetingschedule.xlsx"
    data = pd.read_excel(path)
    dates = data["Date"]
    times = data["Time"]
    programas = data["Programs"]
    print(len(programas))
    time_val = pd.Series(time_entry.get())
    date_val = pd.Series(time_entry2.get())
    programs_val = pd.Series(programs)
    progs_list = programs_val.tolist()
    print(progs_list)
    dates = dates.append(date_val)
    times = times.append(time_val)
    programas = programas.append(pd.DataFrame(progs_list))
    print(len(programas), len(dates), len(times))
    data2 = pd.DataFrame({"Date": dates, "Time": times, "Programs": programas})
    data2.to_excel(path, index=False)
    """
    web_progs = programs + websites
    data = pd.DataFrame(
        {"Date": time_entry2.get(), "Time": time_entry.get(), "Programs and Websites": [web_progs]})
    write_to_excel = pd.ExcelWriter("meetingschedule.xlsx", engine="xlsxwriter")
    data.to_excel(write_to_excel, sheet_name="Sheet 1")
    write_to_excel.save()
    # when the event is executed we need to remove it from the spreadsheet

def openNewWindow():
    global input_web
    # Toplevel object which will
    # be treated as a new window
    newWindow = tk.Toplevel(root)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Add Websites")

    # sets the geometry of toplevel
    newWindow.geometry("300x100")

    # A Label widget to show in toplevel
    intro = tk.Label(newWindow, text="Add your websites here (USE FULL URL)")
    intro.pack()
    input_web = tk.Entry(newWindow)
    input_web.pack()

    sub_web = tk.Button(newWindow, text="Submit Websites", command=add_website)
    sub_web.pack()


def add_website():
    global websites
    for label in frame3.winfo_children():
        if label["text"] in websites:
            label.destroy()
    url = input_web.get()
    print(url)
    if "http" in url:
        websites.append(url)
    else:
        messagebox.showerror("Error", "Please use full URL")
    # print(websites)
    for webs in websites:
        label = tk.Label(frame3, text=webs, font=("Helvetica", 7), bg="grey")
        label.pack()


def add_program():
    for label in frame3.winfo_children():
        if label["text"] in programs:
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
    for webs in websites:
        webbrowser.open(webs, new=0)


def submission():
    global programs
    global websites
    alarm = time_entry.get()
    ttime = tk.Label(frame1, text=('Event is registered at', alarm),  pady=20, bg='#ffbf00')
    ttime.pack()
    # run()
    into_excel()
    time_entry.delete(0, "end")
    time_entry2.delete(0, "end")
    for label in frame3.winfo_children():
        label.destroy()
    programs = []
    websites = []
    root.update()
    root.after(2000, ttime.destroy())


def switch():
    global on_off
    if on_off == False:
        run()
        run_button.config(text="Deactivate Events")
        on_off = True
    else:
        run_button.config(text="Activate Events")
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
# print(time_entry)

# Program and website submissions
frame3 = tk.Frame(frame1, bg="green")
frame3.place(relwidth=0.5, relheight=0.6, relx=0.5)
frame4 = tk.Frame(canvas, bg="green")
frame4.place(relwidth=0.23, relheight=0.1, rely=0.5, relx=0.62)
program_button = tk.Button(frame4, text="Add a Program", command=add_program)
program_button.pack()
website = tk.Button(frame4, text="Enter a Website", command=openNewWindow)
website.place(relwidth=0.8, relheight=0.4, relx=0.1, rely=0.6)

# Checkbutton for repititon of event
repeat_daily = tk.Checkbutton(frame1, text="Repeat daily")
repeat_daily.place(relx=0.35, rely=0.66, anchor="center")
repeat_monthly = tk.Checkbutton(frame1, text="Repeat monthly")
repeat_monthly.place(relx=0.65, rely=0.66, anchor="center")

# Submission button
add = tk.Button(frame1, text="Submit \n Event", padx=4, pady=2, command=submission)
add.place(relx=0.5, rely=0.8, anchor="center")

run_button = tk.Button(frame1, text="Activate Events", command=switch)
run_button.place(relx=0.49, rely=0.9, anchor="center")

label4 = tk.Button(canvas, text="Use Google Calendar Schedule?")
label4.place(relx=0.35, rely=0.1)


# Google calendar toggle widget


root.mainloop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
