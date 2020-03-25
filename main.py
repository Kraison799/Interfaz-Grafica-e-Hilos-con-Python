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
import tkinter as tk
import random
import time
from threading import Thread

# COLOR RGB VALUES #

bubbleGum = "#FFBED2"
magicMint = "#B5EAD7"
frenchSkyBlue = "#82B3FF"
lightYellow = "#FFFFD8"
lightSalmonPink = "#FF9AA2"
lightPastelPurple = "#B399D4"
charmPink = "#E18AAA"

colors = [magicMint, frenchSkyBlue, lightYellow, lightSalmonPink, lightPastelPurple, charmPink]


# BOUNCING BALL CLASS #
class BouncingBall:
    def __init__(self, canvas):  # BouncingBall class constructor
        self.canvas = canvas
        self.x = 0
        self.y = random.randint(0, 200)
        self.r = random.randint(5, 12)
        self.speed = random.randint(2, 5)
        self.falling = True
        self.top_y = self.y + 100
        self.oval = canvas.create_oval(self.x, self.y, self.x + 2*self.r, self.y + 2*self.r, fill=random.choice(colors))

    def move(self):            # Move method of the BouncingBall class
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
    window = tk.Tk()
    window.title("Taller de Interfaz Gráfica")
    window.geometry("800x450")
    window.iconbitmap("icon.ico")
    window.resizable(False, False)

    # Canvas settings
    pannel_canvas = tk.Canvas(window, width=274, height=446, borderwidth=0, highlightthickness=0, bg="#606060")
    pannel_canvas.place(x=0, y=2)

    anim_canvas = tk.Canvas(window, width=524, height=446, borderwidth=0, highlightthickness=0, bg="#CCCCFF")
    anim_canvas.place(x=276, y=2)

    # Function to create the bouncing balls
    def create_circle():
        circle = BouncingBall(anim_canvas)
        circle_thread = Thread(target=circle.move)
        circle_thread.daemon = True
        circle_thread.start()

    # Label creation
    label1 = tk.Label(pannel_canvas, text="Press", font=("Haettenschweiler", 30), bg="#606060", fg=bubbleGum)
    label2 = tk.Label(pannel_canvas, text="to", font=("Haettenschweiler", 30), bg="#606060", fg=magicMint)
    label3 = tk.Label(pannel_canvas, text="start", font=("Haettenschweiler", 30), bg="#606060", fg=bubbleGum)
    label4 = tk.Label(pannel_canvas, text="the", font=("Haettenschweiler", 30), bg="#606060", fg=magicMint)
    label5 = tk.Label(pannel_canvas, text="animation", font=("Haettenschweiler", 30), bg="#606060", fg=bubbleGum)

    # Button creation
    button = tk.Button(pannel_canvas, text="Animation", font=("fixedsys", "15"), bg=frenchSkyBlue, command=create_circle)

    # Label positioning
    label1.place(x=35, y=45)
    label2.place(x=70, y=85)
    label3.place(x=90, y=125)
    label4.place(x=48, y=160)
    label5.place(x=70, y=200)

    # Button positioning
    button.place(x=75, y=300)

    # The window we are working with must be selected as the main loop
    window.mainloop()


# EXECUTE THE MAIN #
main()
