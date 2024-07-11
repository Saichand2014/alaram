import tkinter as tk
from tkinter import messagebox
import time
import datetime
import threading

class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("ALARAM CLOCK")

        self.time_label = tk.Label(root, text="", font=("Helvetica", 48))
        self.time_label.pack()

        self.alarm_time = tk.StringVar()
        self.alarm_entry = tk.Entry(root, textvariable=self.alarm_time, font=("Helvetica", 24))
        self.alarm_entry.pack()

        self.set_alarm_button = tk.Button(root, text="Set Alarm", command=self.set_alarm, font=("Helvetica", 24))
        self.set_alarm_button.pack()

        self.update_time()

    def update_time(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=now)
        self.root.after(1000, self.update_time)

    def set_alarm(self):
        alarm_time = self.alarm_time.get()
        try:
            valid_time = time.strptime(alarm_time, "%H:%M")
            threading.Thread(target=self.check_alarm, args=(alarm_time,)).start()
            messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM format")

    def check_alarm(self, alarm_time):
        while True:
            now = datetime.datetime.now().strftime("%H:%M")
            if now == alarm_time:
                messagebox.showinfo("Alarm", "Time to wake up!")
                break
            time.sleep(30)

if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()
