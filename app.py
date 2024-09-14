import tkinter as tk
from tkinter import simpledialog
import cv2 as cv
import os
import PIL.Image, PIL.ImageTk
import camera

class App:

    def __init__(self, window=tk.Tk(), window_title="Camera Classifier"):
        self.window = window
        self.window_title = window_title

        self.counters = [1,1]

        #self.model =

        self.auto_predict = False

        self.camera = camera.Camera() 

        #self.init gui()

        self.delay = 15

        #self.update()

        self.window.attributes('-topmost', True)
        self.window.mainloop()

    def init_gui(self):
        self.canvas = tk.Canvas(self.window,)

    def auto_predict_toggle(self):
        self.auto_predict = not self.auto_predict