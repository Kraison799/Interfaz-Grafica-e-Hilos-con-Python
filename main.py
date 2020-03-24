"""
##################################################################

Instituto Tecnológico de Costa Rica
Área Académica de Ing. en Computadores

Taller de Interfaz Gráfica con Tkinter
Tallerista: Víctor I. Castrillo Muñoz - 2017110244

Main file

##################################################################
"""

# LIBRARIES #
import tkinter as Tk
import random, time
from threading import Thread

# COLOR RGB VALUES #
White = "#FAFAFA"
Black = "#000000"
Light_Blue = "#81BEF7"
Orange = "#FAAC58"
Dark_Blue = "#084B8A"
Light_Green = "#9AFE2E"
Light_Red = "#FE2E2E"
Purple = "#642EFE"

Colors = [Light_Blue, Orange, Dark_Blue, Light_Green, Purple]

# BOUNCING BALL #
class bouncing_ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 0
        self.y = random.randint(0, 200)
        self.r = random.randint(5, 12)
        self.speed = random.randint(2, 5)
        self.falling = True
        self.top_y = self.y+100
        self.oval = canvas.create_oval(self.x, self.y, self.x+2*self.r, self.y+2*self.r, fill=random.choice(Colors))

    def move(self):
        while self.x < 525:
            # Bouncing effect
            if self.y >= 446 - self.r*2 and self.falling:
                self.falling = False
            elif self.y <= self.top_y and not self.falling:
                self.falling = True
                self.top_y = self.y+100

            # Movement
            if self.falling:
                self.y += self.r
                self.canvas.move(self.oval, self.speed, self.r)
            else:
                self.y -= self.r
                self.canvas.move(self.oval, self.speed, -self.r)
            self.x += self.speed

            time.sleep(0.05)

# MAIN FUNCTION #
def main():
    # Window settings
    window = Tk.Tk()
    window.title("Taller de Interfaz Gráfica")
    window.geometry("800x450")
    window.iconbitmap("icon.ico")
    window.resizable(False, False)

    # Canvas settings
    pannel_canvas = Tk.Canvas(window, width=274, height=446, borderwidth=0, highlightthickness=0, bg="#606060")
    pannel_canvas.place(x=0, y=2)
    
    anim_canvas = Tk.Canvas(window, width=524, height=446, borderwidth=0, highlightthickness=0, bg="#CCCCFF")
    anim_canvas.place(x=276, y=2)

    # Function to create the bouncing balls
    def create_circle():
        circle = bouncing_ball(anim_canvas)
        circle_thread = Thread(target=circle.move)
        circle_thread.start()

    # Canvas components
    label = Tk.Label(pannel_canvas, text="Press to start the animation", font=("Haettenschweiler", 15), bg="#606060", fg=White)
    label.place(x=25, y=25)
    button = Tk.Button(pannel_canvas, text="Animation", command=create_circle)
    button.place(x=25, y=100)

    # The window we are working with must be selected as main loop
    window.mainloop()

# EXECUTE THE MAIN #
main()
