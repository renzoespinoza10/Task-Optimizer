import pandas as pd
from datetime import datetime
import time
import subprocess

# read the excel file to get meeting details
df = pd.read_excel('meetingschedule.xlsx')
df_new = pd.DataFrame()

# Check the current system time
ct = datetime.now().strftime("%H:%M")
dt = datetime.now().strftime("%m/%d/%Y")
print(ct)
print(dt)
# Check if the current time is mentioned in the Dataframe
while(True):
    if dt in df.Date.values:
        print("Date is read correctly from file")
        if ct in df.Time.values:
            df_new = df[df['Time'].astype(str).str.contains(ct)]
            print("opening zoom")
            # Open the Zoom app
            subprocess.Popen("C:\\Users\\rezog\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
            time.sleep(20)
