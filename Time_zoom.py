import time
import subprocess
import pandas as pd
from datetime import datetime

# reading the meeting details
df = pd.read_csv('meetingschedule.csv')
# Check the current system time
ct = datetime.now().strftime("%H:%M")
dt = datetime.now().strftime("%m/%d/%Y")
print(ct)
print(dt)
# Check if the current time is mentioned in the Dataframe
while(True):
    ct = datetime.now().strftime("%H:%M")
    dt = datetime.now().strftime("%m/%d/%Y")
    if dt in df.Date.values:
        #print("Date is read correctly")
        if ct in df.Time.values:
            df_new = df[df['Time'].astype(str).str.contains(ct)]
            #print("Time is read correctly")
            print(df_new.iloc[0, 2])
        # Open the Zoom app
        #   subprocess.Popen("C:\\Users\\rezog\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
            # time.sleep(60)
