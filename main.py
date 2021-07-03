import tkinter as tk
import ctypes

user32 = ctypes.windll.user32


class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_ulong), ("y", ctypes.c_ulong)]


class XY(tk.Tk):
    transparent = "black"
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes("-transparentcolor", self.transparent)
        self.configure(bg="magenta")
        self.canvas = tk.Canvas(self, bg=self.transparent, highlightbackground=self.transparent)
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        
        self.canvas.pack(fill="both")
        self.canvas.create_text(60, 20, text = "XY", fill="white", font="aril 20", tag="text")
        self.after(10, self.loop)
        self.mainloop()
    
    def loop(self):
        point = POINT()
        user32.GetCursorPos(ctypes.byref(point))
        self.canvas.itemconfigure("text", text=str(point.x) + " | " + str(point.y))
        self.after(10, self.loop)


XY()