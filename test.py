import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os
import pandas as pd
import webbrowser
import time
import subprocess
from datetime import datetime, timedelta, date
import threading
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
    web_progs = programs + websites
    data = pd.DataFrame(
        {"Date": time_entry2.get(), "Time": time_entry.get(), "Programs and Websites": [web_progs], "Repeat Daily": rep_int.get(), "Repeat Monthly": rep_int2.get()})
    # write_to_excel = pd.ExcelWriter("meetingschedule.csv", engine="xlsxwriter")
    data.to_csv("meetingschedule.csv")
    # write_to_excel.save()
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
    intro = tk.Label(newWindow, text="Add your websites here (USE FULL URL, '/' at end)")
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
    if "https" in url:
        websites.append(url)
    else:
        messagebox.showerror("Error", "Please use full URL")
    # print(websites)
    for webs in websites:
        label = tk.Label(frame3, text=webs, font=("Helvetica", 7), bg="grey")
        label.pack()
    input_web.delete(0, "end")


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
    # reading the meeting details
    df = pd.read_csv('meetingschedule.csv')
    # Check the current system time
    ct = datetime.now().strftime("%H:%M")
    dt = datetime.now().strftime("%m/%d/%Y")
    print(ct)
    print(dt)

    # webbrowser.open(df.iloc[0, 3])
    # Check if the current time is mentioned in the Dataframe
    while(True):
        x = 0
        ct = datetime.now().strftime("%H:%M")
        dt = datetime.now().strftime("%m/%d/%Y")
        if dt in df.Date.values:
            if ct in df.Time.values:
                df_new = df[df['Time'].astype(str).str.contains(ct)]
                print("Time is read correctly")
                list_progswebs = df_new.iloc[x, 3].split(",")
                for num in list_progswebs:
                    num = num.replace("'", "")
                    if "[" or "]" in num:
                        num = num.replace("[", "")
                        num = num.replace("]", "")
                    num = num.strip()
                    print(num)
                    if ".exe" in num:
                        subprocess.Popen(num)
                    else:
                        webbrowser.open(num, 0)

                if df_new.iloc[x, 4] == 1:
                    # print(df)
                    dt2 = datetime.now()
                    dt3 = datetime.now() + timedelta(days=1)
                    df.loc[x, "Date"] = dt3.strftime("%m/%d/%Y")
                    # print(df)
                    df.to_csv("meetingschedule.csv", index=False)
                elif df_new.iloc[x, 5] == 1:
                    dt2 = datetime.now()
                    dt3 = datetime.now() + timedelta(days=31)
                    df.loc[x, "Date"] = dt3.strftime("%m/%d/%Y")
                    # print(df)
                    df.to_csv("meetingschedule.csv", index=False)
                else:
                    df.set_index("Date", inplace=False)
                    df = df.drop(x)
                    df.to_csv("meetingschedule.csv")
                x += 1
                time.sleep(60)


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


def start():
    t1 = threading.Thread(target=run)
    t1.daemon = True
    t1.start()


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

# Checkbutton for repititon of event\
rep_int = tk.IntVar()
repeat_daily = tk.Checkbutton(frame1, text="Repeat Weekdays", variable=rep_int)
repeat_daily.place(relx=0.35, rely=0.66, anchor="center")
rep_int2 = tk.IntVar()
repeat_monthly = tk.Checkbutton(frame1, text="Repeat monthly", variable=rep_int2)
repeat_monthly.place(relx=0.65, rely=0.66, anchor="center")

# Submission button
add = tk.Button(frame1, text="Submit \n Event", padx=4, pady=2, command=submission)
add.place(relx=0.5, rely=0.8, anchor="center")

run_button = tk.Button(frame1, text="Activate Events", command=start)
run_button.place(relx=0.49, rely=0.9, anchor="center")

#label4 = tk.Button(canvas, text="Use Google Calendar Schedule?")
#label4.place(relx=0.35, rely=0.1)


# Google calendar toggle widget


root.mainloop()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
