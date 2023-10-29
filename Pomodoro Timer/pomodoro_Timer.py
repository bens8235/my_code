from tkinter import *
import math

# Constants

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mark = ""
time = None
y = 0 # constant just to make different things happen depending on its value.

# Timer Reset


def reset_timer():
    global y
    window.after_cancel(time)
    timer.config(text="Timer", fg= GREEN)
    canvas.itemconfig(timer_text, text="0:00")
    tick.config(text="")
    global reps
    global mark
    mark = ""
    reps = 0
    y = 0

# Timer Mechanism, work every other timer session then long break every 4 work sessions.


def start_timer():
    global y
    if y == 1:
        resume_timer()
        y = 0
    else:
        global reps
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        reps += 1

        if reps % 2 == 1:
            timer.config(text="Work", fg=GREEN)
            count_down(work_sec)
        elif reps % 8 == 0:
            timer.config(text="Break",fg=RED)
            count_down(long_break_sec)
        else:
            timer.config(text="Break",fg=PINK)
            count_down(short_break_sec)

# Countdown mechanism.


def count_down(count):
    global mark
    global time
    global x

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
         
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.attributes('-topmost', 0)
        time = window.after(1000, count_down, count - 1)
        x = count
    else:
        window.attributes('-topmost', 1)
        start_timer()
        if reps % 2 == 0:
            mark += "✓"
        tick.config(text=mark)


def pause_timer():
    global y
    window.after_cancel(time)
    y = 1


def resume_timer():
    count_down(x)

# UI Setup

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row = 1)


timer = Label(text="Timer", font = (FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

start = Button(text="Start", font = (FONT_NAME, 10), command= start_timer, highlightthickness=0)
start.grid(column=0, row = 2)

reset = Button(text="Reset", font = (FONT_NAME, 10), command=reset_timer, highlightthickness=0)
reset.grid(column=2, row = 2)

tick = Label(font = (FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
tick.grid(column=1, row= 3)

pause = Button(text="Pause", font = (FONT_NAME, 10), command= pause_timer, highlightthickness=0)
pause.grid(column=2, row = 3)

resume = Button(text="Resume", font = (FONT_NAME, 10), command= resume_timer, highlightthickness=0)
resume.grid(column=0, row = 3)

window.mainloop()