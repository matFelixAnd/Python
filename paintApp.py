import tkinter as tk

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.color = "black"
        self.pen_width = 2
        self.is_drawing = False
        self.last_x, self.last_y = 0, 0

    def start_drawing(self, event):
        self.is_drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.is_drawing:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.color, width=self.pen_width)
            self.last_x, self.last_y = event.x, event.y

    def change_color(self, new_color):
        self.color = new_color

    def change_pen_width(self, new_width):
        self.pen_width = new_width

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Paint")
    paint_app = PaintApp(root)

    color_frame = tk.Frame(root)
    color_frame.pack(pady=10)

    colors = ["black", "red", "blue", "green", "yellow"]
    for color in colors:
        color_btn = tk.Button(color_frame, bg=color, width=3, command=lambda c=color: paint_app.change_color(c))
        color_btn.pack(side="left", padx=3)

    width_frame = tk.Frame(root)
    width_frame.pack(pady=5)

    widths = [1, 2, 3, 4, 5]
    for width in widths:
        width_btn = tk.Button(width_frame, text=str(width), width=2, command=lambda w=width: paint_app.change_pen_width(w))
        width_btn.pack(side="left", padx=2)

    clear_btn = tk.Button(root, text="Clear Canvas", command=paint_app.clear_canvas)
    clear_btn.pack(pady=10)

    root.mainloop()
