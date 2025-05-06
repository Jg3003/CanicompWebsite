# Coder: Jamie Mikhaell Haganta Setiawan X6/14
# Original: https://github.com/wynand1004/Projects/blob/master/Tetris/tetris.py
#Perbedaan resolusi, warna, dan penambahan grid line

import turtle
import time
import random

wn = turtle.Screen()
wn.title("TETRIS by @TokyoEdTech, Edited by Jamie")
wn.bgcolor("gray20")
wn.setup(width=500, height=600)
wn.tracer(0)

delay = 0.1

class Shape():
    def __init__(self):
        self.x = 6
        self.y = 0
        self.color = random.randint(1, 7)
        
        square = [[1,1],
                  [1,1]]

        horizontal_line = [[1,1,1,1]]

        vertical_line = [[1],
                         [1],
                         [1],
                         [1]]

        left_l = [[1,0,0],
                  [1,1,1]]
                   
        right_l = [[0,0,1],
                   [1,1,1]]
                   
        left_s = [[1,1,0],
                  [0,1,1]]
                  
        right_s = [[0,1,1],
                   [1,1,0]]
                  
        t = [[0,1,0],
             [1,1,1]]

        shapes = [square, horizontal_line, vertical_line, left_l, right_l, left_s, right_s, t]
        self.shape = random.choice(shapes)
        self.height = len(self.shape)
        self.width = len(self.shape[0])

    def move_left(self, grid):
        if self.x > 0 and grid[self.y][self.x - 1] == 0:
            self.erase_shape(grid)
            self.x -= 1
        
    def move_right(self, grid):
        if self.x < 16 - self.width and grid[self.y][self.x + self.width] == 0:
            self.erase_shape(grid)
            self.x += 1
    
    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    grid[self.y + y][self.x + x] = self.color
                
    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    grid[self.y + y][self.x + x] = 0
                    
    def can_move(self, grid):
        for x in range(self.width):
            if self.shape[self.height-1][x] == 1:
                if grid[self.y + self.height][self.x + x] != 0:
                    return False
        return True
    
    def rotate(self, grid):
        self.erase_shape(grid)
        rotated_shape = [[self.shape[y][x] for y in range(len(self.shape)-1, -1, -1)] for x in range(len(self.shape[0]))]
        if self.x + len(rotated_shape[0]) < len(grid[0]):
            self.shape = rotated_shape
            self.height = len(self.shape)
            self.width = len(self.shape[0])
            
grid = [[0]*16 for _ in range(26)]

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)

def draw_grid(pen, grid):
    pen.clear()
    top, left = 260, -160
    colors = ["black", "cyan", "blue", "orange", "yellow", "green", "purple", "red"]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            pen.color(colors[grid[y][x]])
            pen.goto(left + x * 20, top - y * 20)
            pen.stamp()

    pen.color("white")
    pen.penup()
    for x in range(len(grid[0]) + 1):
        x_pos = left + x * 20
        pen.goto(x_pos, top)
        pen.pendown()
        pen.goto(x_pos, top - len(grid) * 20)
        pen.penup()

    for y in range(len(grid) + 1):
        y_pos = top - y * 20
        pen.goto(left, y_pos)
        pen.pendown()
        pen.goto(left + len(grid[0]) * 20, y_pos)
        pen.penup()

def check_grid(grid):
    global score
    y = len(grid) - 1
    while y > 0:
        if all(grid[y][x] != 0 for x in range(len(grid[0]))):
            score += 10
            draw_score(pen, score)
            for copy_y in range(y, 0, -1):
                grid[copy_y] = grid[copy_y - 1][:]
        else:
            y -= 1

def draw_score(pen, score):
    pen.color("white")
    pen.hideturtle()
    pen.goto(-75, 350)
    pen.write("Score: {}".format(score), align="left", font=("Arial", 24, "normal"))

def draw_text(pen, text, x, y, size=18):
    pen.color("white")
    pen.goto(x, y)
    pen.write(text, align="left", font=("Arial", size, "bold"))

shape = Shape()
grid[shape.y][shape.x] = shape.color
wn.listen()
wn.onkeypress(lambda: shape.move_left(grid), "a")
wn.onkeypress(lambda: shape.move_right(grid), "d")
wn.onkeypress(lambda: shape.rotate(grid), "space")
score = 0
draw_score(pen, score)

draw_text(pen, "Welcome to TETRIS!", -75, 380, 24)
draw_text(pen, "Controls:", -250, 350)
draw_text(pen, "A - Move Left", -250, 330)
draw_text(pen, "D - Move Right", -250, 310)
draw_text(pen, "Space - Rotate", -250, 290)

while True:
    wn.update()
    if shape.y == len(grid) - shape.height:
        shape = Shape()
        check_grid(grid)
    elif shape.can_move(grid):
        shape.erase_shape(grid)
        shape.y += 1
        shape.draw_shape(grid)
    else:
        shape = Shape()
        check_grid(grid)
    draw_grid(pen, grid)
    draw_score(pen, score)
    time.sleep(delay)

wn.mainloop()

