import time

def alarm_clock():
    alarm_time = input("Set alarm (HH:MM:SS): ")
    print("Alarm set for", alarm_time)

    while True:
        current = time.strftime("%H:%M:%S")
        print("Current Time:", current, end="\r")

        if current == alarm_time:
            print("\nAlarm ringing!")

            snooze = input("Type 'snooze' to delay 10 seconds or 'stop': ").lower()

            if snooze == "snooze":
                print("Snoozing...")
                time.sleep(10)
            else:
                print("Alarm stopped.")
                break

        time.sleep(1)

alarm_clock()