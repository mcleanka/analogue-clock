try:
    import Tkinter
except:
    import tkinter as Tkinter

import math
import time


class AnalogueClock(Tkinter.Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.sticks = []
        self.canvas = Tkinter.Canvas(self, bg='black')
        self.background_image = Tkinter.PhotoImage(file='clock.gif')
        self.x = 150  # Center Point x
        self.y = 150  # Center Point
        self.length = 50  # Stick Length
        self.creating_all_function_trigger()

    def creating_all_function_trigger(self):
        self.create_canvas_for_shapes()
        self.creating_background_()
        self.creating_sticks()
        return

    def creating_background_(self):
        self.canvas.create_image(self.x, self.y, image=self.background_image)
        return

    def create_canvas_for_shapes(self):
        self.canvas.pack(expand='yes', fill='both')
        return

    def creating_sticks(self):
        for i in range(3):
            store = self.canvas.create_line(self.x, self.y, self.x + self.length, self.y + self.length, width=2,
                                            fill='#333')
            self.sticks.append(store)
        return

    def update_class(self):
        now = time.localtime()
        t = time.strptime(str(now.tm_hour), "%H")
        hour = int(time.strftime("%I", t)) * 5
        now = (hour, now.tm_min, now.tm_sec)
        # Changing Stick Coordinates
        for n, i in enumerate(now):
            x, y = self.canvas.coords(self.sticks[n])[0:2]
            cr = [x, y, self.length * math.cos(math.radians(i * 6) - math.radians(90)) + self.x,
                  self.length * math.sin(math.radians(i * 6) - math.radians(90)) + self.y]
            self.canvas.coords(self.sticks[n], tuple(cr))
        return


# Main Function Trigger
if __name__ == '__main__':
    root = AnalogueClock()

while True:
    root.update()
    root.update_idletasks()
    root.update_class()
