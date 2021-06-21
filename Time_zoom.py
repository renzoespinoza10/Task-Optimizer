import pandas as pd
from datetime import datetime
import time
import subprocess

# read the excel file to get meeting details
df = pd.read_excel('meetingschedule.xlsx')
df_new = pd.DataFrame()

# This line here gets all the time values in the entire spreadsheet, it doesn't distinguish a specific one
# It returns it in this format : [datetime.time(13,42)]
print(df.Time.values)

# infinite loop that keeps on checking when to open zoom
while(True):
    # check current time ct
    ct = datetime.now().strftime("%H:%M")
    dt = datetime.now().strftime("%Y-%m-%d")
    # check if the current time and date in in the data DataFrame
    if ct in df.Time.values:
        print("Hello")

        df_new = df[df['Time'].astype(str).str.contains(ct)]
        # Open the Zoom app
        subprocess.Popen("C:\\Users\\rezog\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
