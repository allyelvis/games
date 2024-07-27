import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Maze Game")

# Create a turtle player
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.goto(-200, 200)

# Create the maze walls
walls = [
    (-250, 250), (-250, 200), (-250, 150), (-250, 100),
    (-250, 50), (-250, 0), (-250, -50), (-250, -100),
    (-200, -100), (-150, -100), (-100, -100), (-50, -100),
    (0, -100), (50, -100), (100, -100), (150, -100),
    (200, -100), (200, -50), (200, 0), (200, 50),
    (200, 100), (200, 150), (200, 200), (200, 250)
]

for wall in walls:
    wall_turtle = turtle.Turtle()
    wall_turtle.shape("square")
    wall_turtle.color("black")
    wall_turtle.penup()
    wall_turtle.goto(wall)
    wall_turtle.stamp()

# Function to move the player
def move_up():
    x, y = player.position()
    player.sety(y + 50)

def move_down():
    x, y = player.position()
    player.sety(y - 50)

def move_left():
    x, y = player.position()
    player.setx(x - 50)

def move_right():
    x, y = player.position()
    player.setx(x + 50)

# Keyboard bindings
wn.listen()
wn.onkey(move_up, "Up")
wn.onkey(move_down, "Down")
wn.onkey(move_left, "Left")
wn.onkey(move_right, "Right")

# Main game loop
while True:
    wn.update()
