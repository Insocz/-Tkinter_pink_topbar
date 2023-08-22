import tkinter as tk

class CustomTitleBar:

    def __init__(self,root = tk.Tk):
        self.root = root

        self.root.overrideredirect(True)

        self.build()

    def build(self):

        self.topbar = tk.Canvas(self.root,background="#e72dfc",border=0,highlightthickness=0,height=30)
        self.topbar.pack(fill="both")

        #replace this for custom top bar

        r = 200
        g = 40
        b = 180

        for num in range(200):

            color = "#%02x%02x%02x" % (int(r),int(g),int(b))

            self.topbar.create_rectangle(0+num*2,0,500,32,fill=color,outline=color)

            r -= 0.8
            g -= 0.05
            b -= 0.8


        self.topbar.create_line((0,30),(500,30),width=5,fill="#ef62bb")

        self.topbar.create_line((0,2),(500,2),width=5,fill="#ef62bb")
        self.topbar.create_line((0,16),(500,16),width=5,fill="#ef62bb")

        for num in range(10):
            
            self.topbar.create_rectangle(1+num*50,16-6,15+1+num*50,16+6,fill="#ef62bb",outline="#ef62bb")
            self.topbar.create_rectangle(1+num*50+2,16-6+2,15+1+num*50-2,16+6-2,fill="#efaad6",outline="#efaad6")
        
        self.topbar.create_line((457,0),(457,35),fill="#ef62bb",width=5)
        self.topbar.create_line((2,0),(2,35),fill="#ef62bb",width=5)

        #-------------------------------

        self.close_button = tk.Button(self.topbar,height=0, text='X', bg="#ef62bb", fg='white', relief='flat', command=self.root.destroy,highlightthickness=0,font=("Silkscreen"))
        self.close_button.pack(side='right')

        self.topbar.bind('<ButtonPress-1>', self.start_move)
        self.topbar.bind('<ButtonRelease-1>', self.stop_move)       
        self.topbar.bind('<B1-Motion>', self.on_move)

    def start_move(self, event):
        self.root._offsetx = event.x
        self.root._offsety = event.y

    def stop_move(self, event):
        del self.root._offsetx
        del self.root._offsety

    def on_move(self, event):
        x = self.root.winfo_x() + event.x - self.root._offsetx
        y = self.root.winfo_y() + event.y - self.root._offsety
        self.root.geometry(f'+{x}+{y}')