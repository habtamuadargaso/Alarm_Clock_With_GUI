#                                        *Welcome to DataFlair Alarm Clock*
# Importing all the necessary libraries to form the alarm clock: from tkinter import *
import datetime
# Tkinter module belongs to standard library of graphic user interface in python.
# it helps to create dialog box  with any information  to provide or get from the user
from tkinter import *
# datetime and time modules in python help us to work the date and time of the current day when the user is operating.
import datetime
import time
# module import the basic sound playing
import winsound


# we define the function as alarm which takes the argument of  set_alarm_timer
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        # get current time using the function current_time which take argument  datetime.datetime.now
        current_time = datetime.datetime.now()
        # now is used to print the time by using the string conversion using utctime
        now = current_time.strftime("%H:%M:%S")
        # now is used to print the date by using the string conversion using utctime
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        # if the user input time set_alarm_timer matches with while loop time now,the message is printed as
        # "time to wake" else if the loop run until the set_alarm_equal = current time
        if now == set_alarm_timer:
            print("Time to Wake up")

            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            # then loop break
            break


# we need from the user the actual time to set the alarm which takes value from the user in the string format
# which is the same argument of (set_alarm_timer)

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


# to initial tkinter, we pass a command under the name clock as TK ()

clock = Tk()
# The dialog box has title as my name
clock.title("Habtamu Alarm Clock")
# the dialog box geometry
clock.geometry("400x200")

# we pass on the heading to mention the time format for 24 hours using time_format
Label(clock, text="Enter time in 24 hour format!", fg="red", bg="black", font="Arial").place(x=60, y=120)
# labeling to be hour min sec for input box
Label(clock, text="Hour  Min   Sec", font=60).place(x=110)

Label(clock, text="When to wake you up", fg="blue", relief="solid",
      font=("Helvetica", 7, "bold")).place(x=0, y=29)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

# Time required to set the alarm clock:
Entry(clock, textvariable=hour, bg="pink", width=15).place(x=110, y=30)
Entry(clock, textvariable=min, bg="pink", width=15).place(x=150, y=30)
Entry(clock, textvariable=sec, bg="pink", width=15).place(x=200, y=30)

# To take the time input by user:
Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time).place(x=110, y=70)

clock.mainloop()
# Execution of the window.
# git