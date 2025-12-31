import time
from datetime import datetime

def alarm_clock():
    print("----- DIGITAL ALARM CLOCK -----")
    alarm_time = input("Set alarm time (HH:MM:SS, 24-hour format): ")

    print(f"Alarm set for {alarm_time}...\n")

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")

        if current_time == alarm_time:
            print("⏰ WAKE UP! ALARM RINGING ⏰")
            break

        time.sleep(1)

alarm_clock()
