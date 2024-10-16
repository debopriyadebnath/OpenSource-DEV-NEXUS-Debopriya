import time
from datetime import datetime

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}. Waiting...")
    
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")  # Get current time
        if current_time == alarm_time:
            print("Wake up! It's time!")
            break
        time.sleep(1)  # Wait for 1 second before checking again

if __name__ == "__main__":
    alarm_input = input("Set the alarm time (HH:MM:SS): ")
    try:
        # Ensure input format is correct (this simple check expects exactly this format)
        datetime.strptime(alarm_input, "%H:%M:%S")
        set_alarm(alarm_input)
    except ValueError:
        print("Invalid time format. Please enter in HH:MM:SS format.")
