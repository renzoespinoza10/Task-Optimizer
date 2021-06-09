import time
import subprocess


# functions to format date, time
def format_date(x):
    date_list = x.split(sep="-")
    return list(map(int, date_list))

def format_time(x):
    time_list = x.split(sep="-")
    return list(map(int, time_list))

def given_datetime(given_date, given_time):

    # YY, MM, DD, HH, MM
    return datetime.datetime(given_date[2], given_date[1], given_date[0], given_time[0], given_time[1], given_time[2])

# join the meeting

def join_meeting(meeting_date, meeting_time):

    meeting_date_x = format_date(meeting_date)
    meeting_time_x = format_time(meeting_time)
    required_datetime = given_datetime(meeting_date_x, meeting_time_x)

    # time difference between current and meeting time
    wait_time = (required_datetime - datetime.datetime.now().replace(microsecond=0)).total_seconds()
    
    print("Your ZOOM meeting starts in" + str(wait_time/60) + " min")
    
    time.sleep(wait_time)

    subprocess.Popen("C:\\Users\\rezog\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")


def zoom(meeting_date,given_time):
    join_meeting(meeting_date, given_time);

    
