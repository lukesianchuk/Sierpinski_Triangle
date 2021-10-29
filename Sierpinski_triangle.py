import tkinter as tk
import random

class Application:
    def __init__(self,master):
        self.master = master
        master.title("Sierpinksi Triangles")
        
        self.canvas = tk.Canvas(master,width=400,height=400,background="#ccc")
        self.canvas.pack()
        # Initialize points and introductory text
        self.draw_points([200,113],[100,287],[300,287])
        self.draw_text()
        # Create GUI buttons
        self.chaos_button = tk.Button(master, text="Draw Fractals", command=self.create_fractals)
        self.chaos_button.pack(fill=tk.X)
        self.xy_button = tk.Button(master, text="Reset", command=self.clear_button)
        self.xy_button.pack(fill=tk.X)
        # Initialize dragging variables
        self._drag_data = {"x": 0, "y": 0, "item": None}
        # Binding for drag and drop. Objects use tag 'token'
        self.canvas.tag_bind("token", "<ButtonPress-1>", self.on_token_press)
        self.canvas.tag_bind("token", "<ButtonRelease-1>", self.on_token_release)
        self.canvas.tag_bind("token", "<B1-Motion>", self.on_token_motion)
        
    def draw_points(self,a,b,c):
        self.x = self.canvas.create_oval(a[0]-8,a[1]-8,a[0]+8,a[1]+8,fill="#f00",tags="token")
        self.y = self.canvas.create_oval(b[0]-8,b[1]-8,b[0]+8,b[1]+8,fill="#f00",tags="token")
        self.z = self.canvas.create_oval(c[0]-8,c[1]-8,c[0]+8,c[1]+8,fill="#f00",tags="token")
 
    def create_fractals(self):
        # Algorithm to generate points
        point = [0,0]
        for i in range(10000):
            roll = random.randint(1,3)
            if roll == 1:
                point[0] = (point[0]+((self.canvas.coords(self.x)[0]))+8)/2
                point[1] = (point[1]+((self.canvas.coords(self.x)[1]))+8)/2
            if roll == 2:
                point[0] = (point[0]+((self.canvas.coords(self.y)[0]))+8)/2
                point[1] = (point[1]+((self.canvas.coords(self.y)[1]))+8)/2
            if roll == 3:
                point[0] = (point[0]+((self.canvas.coords(self.z)[0]))+8)/2
                point[1] = (point[1]+((self.canvas.coords(self.z)[1]))+8)/2
            self.canvas.create_line(point[0],point[1],point[0]+1,point[1],fill="#00f")
        
    def draw_text(self):
        self.canvas.create_text(200,20,fill="black",font="Times 12",text="Move the points and generate fractals!")

    def create_token(self, coord, color):
        #Create a token at the given coordinate in the given color
        (x,y) = coord
        self.canvas.create_oval(x-25, y-25, x+25, y+25, outline=color, fill=color, tags="token")

    def on_token_press(self, event):
        '''Begining drag of an object'''
        # Record the item and its location
        self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def on_token_release(self, event):
        '''End drag of an object'''
        # Reset the drag information
        self._drag_data["item"] = None
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def on_token_motion(self, event):
        '''Handle dragging of an object'''
        # Compute how much the mouse has moved
        delta_x = event.x - self._drag_data["x"]
        delta_y = event.y - self._drag_data["y"]
        # move the object the appropriate amount
        self.canvas.move(self._drag_data["item"], delta_x, delta_y)
        # Record the new position
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y
    
    def clear_button(self):
        self.canvas.delete("all")
        self.draw_points([200,113],[100,287],[300,287])
        

    
        
root = tk.Tk()
root.resizable(width=False, height=False)
my_app = Application(root)

root.mainloop()