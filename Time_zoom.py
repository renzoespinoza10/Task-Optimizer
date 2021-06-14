
import pandas as pd
from datetime import datetime
import time
import subprocess

# read the excel file to get meeting details
df = pd.read_excel('meetingschedule.xlsx')
df_new = pd.DataFrame()

# infinite loop that keeps on checking when to open zoom
while(True):
    # check current time ct
    ct = datetime.now().strftime("%H:%M")
    dt = datetime.now().strftime("%m/%d/%Y")

    # check if the current time and date in in the data DataFrame
    if dt in df.Date.values:
        if ct in df.Time.value:
            df_new = df[df['Time'].astype(str).str.contains(ct)]
            # Open the Zoom app
            subprocess.Popen("C:\\Users\\rezog\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")