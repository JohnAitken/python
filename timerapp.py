import tkinter as tk
import time

class CountdownTimer:
    def __init__(self, minutes, app):
        self.minutes = minutes
        self.seconds = self.minutes * 60
        self.running = False
        self.app = app

    def start(self):
        self.running = True
        start_time = time.time()
        while self.running:
            elapsed_time = time.time() - start_time
            remaining_time = max(self.seconds - elapsed_time, 0)
            if remaining_time == 0:
                self.app.timer_label.config(text="Time's up!")
                break
            else:
                minutes = remaining_time // 60
                seconds = remaining_time % 60
                self.app.timer_label.config(text=f"{minutes:02.0f}:{seconds:02.0f}")
                time.sleep(1)

class TimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer")

        self.timer_label = tk.Label(master, text="Select a timer:")
        self.timer_label.pack()

        self.five_minute_button = tk.Button(master, text="5 minutes", command=self.start_five_minute_timer)
        self.five_minute_button.pack()

        self.ten_minute_button = tk.Button(master, text="10 minutes", command=self.start_ten_minute_timer)
        self.ten_minute_button.pack()

        self.fifteen_minute_button = tk.Button(master, text="15 minutes", command=self.start_fifteen_minute_timer)
        self.fifteen_minute_button.pack()

        self.thirty_minute_button = tk.Button(master, text="30 minutes", command=self.start_thirty_minute_timer)
        self.thirty_minute_button.pack()

    def start_five_minute_timer(self):
        self.start_timer(5)

    def start_ten_minute_timer(self):
        self.start_timer(10)

    def start_fifteen_minute_timer(self):
        self.start_timer(15)

    def start_thirty_minute_timer(self):
        self.start_timer(30)

    def start_timer(self, minutes):
        self.timer_label.config(text=f"{minutes:02d}:00")
        timer = CountdownTimer(minutes, self)
        timer.start()

root = tk.Tk()
app = TimerApp(root)
root.mainloop()
