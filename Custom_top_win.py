import tkinter as tk
import CustomTitleBar
import pick

class App:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry("500x360+20+20")
        self.root.configure(background="#3e2742")

        CustomTitleBar.CustomTitleBar(self.root)

        # the color palet
        self.frame = tk.Frame(self.root,background="#3e2742",height=270,width=500,highlightthickness=0)
        self.frame.pack()

        cl = [("#e72dfc",0,0),("#c828b4",0,1),("#281e14",0,2),("#ef62bb",0,3)]

        for data in cl:
            color,x,y = data

            self.cl1 = tk.Frame(self.frame,background=color,height=285,width=500/4).grid(column=y,row=x,pady=(20,0))


app = App()
app.root.mainloop()