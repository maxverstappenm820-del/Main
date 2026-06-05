#alarm clock.py
import time
import winsound
import datetime

def set_alarm(alarm_time):
    print("Alarm set for", alarm_time)
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Current time:", current_time, end="\r")
        if current_time == alarm_time:
            print("Alarm ringing!")
            winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 1 second
            is_running = False
        time.sleep(1)  # Check every 1 second
if __name__ == "__main__":
    alarm_time = input("Set the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)