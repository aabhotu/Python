from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
import cv2

window = Tk()
window.title('my window')

video = cv2.VideoCapture(0)
# ret, frame = video.read()
# cv2.inshow("W", frame)
canvas_w = video.get(cv2.CAP_PROP_FRAME_WIDTH) // 2
canvas_h = video.get(cv2.CAP_PROP_FRAME_HEIGHT) // 2

canvas = Canvas(window, width=canvas_w, height=canvas_h, bg="red")
canvas.pack()

window.mainloop()
