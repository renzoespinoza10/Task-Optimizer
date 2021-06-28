import time
import subprocess
import pandas as pd
import webbrowser
from datetime import datetime

# reading the meeting details
df = pd.read_csv('meetingschedule.csv')
# Check the current system time
ct = datetime.now().strftime("%H:%M")
dt = datetime.now().strftime("%m/%d/%Y")
print(ct)
print(dt)

#webbrowser.open(df.iloc[0, 3])
# Check if the current time is mentioned in the Dataframe
while(True):
    x = 0
    ct = datetime.now().strftime("%H:%M")
    dt = datetime.now().strftime("%m/%d/%Y")
    if dt in df.Date.values:
        print("Date is read correctly")
        if ct in df.Time.values:
            df_new = df[df['Time'].astype(str).str.contains(ct)]
            print("Time is read correctly")
            list_progswebs = df_new.iloc[x, 3].split(",")
            for num in list_progswebs:
                num = num.replace("'", "")
                if "[" or "]" in num:
                    num = num.replace("[", "")
                    num = num.replace("]", "")
                print(num)
                if ".exe" in num:
                    subprocess.Popen(num)
                else:
                    webbrowser.open(num, new=0)

            if repeat_daily.get() == 1:
                df.loc[x, "Date"] = dt + datetime.timedelta(days=1)
            elif repeat_monthly.get() == 1:
                df.loc[x, "Date"] = dt + datetime.tinedelta(days=30)

            x += 1
            time.sleep(60)
        # Open the Zoom app
        #   subprocess.Popen("C:\\Users\\rezog\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
            # time.sleep(60)
