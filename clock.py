"""A simple analog clock with a digital HH:MM:SS display."""

import math
import tkinter as tk
from datetime import datetime


WINDOW_SIZE = 400
CENTER = WINDOW_SIZE // 2
RADIUS = 170


def draw_clock() -> None:
    """Draw the clock face and update its hands and digital time."""
    now = datetime.now()
    canvas.delete("hands")
    canvas.delete("digital_time")

    # The hour hand also moves gradually as the minutes pass.
    hour = (now.hour % 12) + now.minute / 60
    minute = now.minute + now.second / 60
    second = now.second + now.microsecond / 1_000_000

    hands = (
        (hour, 12, 75, "red", 7),
        (minute, 60, 110, "blue", 5),
        (second, 60, 140, "green", 2),
    )

    for value, units, length, color, width in hands:
        angle = math.radians(value / units * 360 - 90)
        end_x = CENTER + length * math.cos(angle)
        end_y = CENTER + length * math.sin(angle)
        canvas.create_line(
            CENTER,
            CENTER,
            end_x,
            end_y,
            fill=color,
            width=width,
            capstyle=tk.ROUND,
            tags="hands",
        )

    canvas.create_text(
        CENTER,
        CENTER + 85,
        text=now.strftime("%H:%M:%S"),
        font=("Arial", 18, "bold"),
        tags="digital_time",
    )
    root.after(100, draw_clock)


root = tk.Tk()
root.title("Analog Clock")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=WINDOW_SIZE,
    height=WINDOW_SIZE,
    background="white",
    highlightthickness=0,
)
canvas.pack()

canvas.create_oval(
    CENTER - RADIUS,
    CENTER - RADIUS,
    CENTER + RADIUS,
    CENTER + RADIUS,
    outline="black",
    width=3,
)

for number in range(1, 13):
    angle = math.radians(number / 12 * 360 - 90)
    x = CENTER + (RADIUS - 25) * math.cos(angle)
    y = CENTER + (RADIUS - 25) * math.sin(angle)
    canvas.create_text(x, y, text=str(number), font=("Arial", 14, "bold"))

draw_clock()
root.mainloop()