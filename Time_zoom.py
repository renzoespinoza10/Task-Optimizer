import pandas as pd
from datetime import datetime
import time
import subprocess
import xlrd

# read the excel file to get meeting details
#workbook = xlrd.open_workbook('meetingschedule.xlsx')
#worksheet = workbook.sheet_by_name('Sheet1')
df = pd.read_excel('meetingschedule.xlsx')
df_new = pd.DataFrame()
#dt = datetime.now().strftime("%m/%d/%Y")
#print("dt", worksheet.cell(1, 0))
# print(datetime.now().strftime("%Y-%m-%d"))
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
