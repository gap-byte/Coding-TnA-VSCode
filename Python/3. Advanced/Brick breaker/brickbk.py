import tkinter as tk
import random

# -------------------------------
# Game setup
# -------------------------------
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BALL_SIZE = 20
BRICK_ROWS = 5
BRICK_COLUMNS = 8
BRICK_WIDTH = 80
BRICK_HEIGHT = 30

# Create window
root = tk.Tk()
root.title("Brick Breaker")
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
canvas.pack()

# -------------------------------
# Paddle setup
# -------------------------------
paddle = canvas.create_rectangle(
    (WINDOW_WIDTH - PADDLE_WIDTH) / 2,
    WINDOW_HEIGHT - 40,
    (WINDOW_WIDTH + PADDLE_WIDTH) / 2,
    WINDOW_HEIGHT - 40 + PADDLE_HEIGHT,
    fill="white"
)

# -------------------------------
# Ball setup
# -------------------------------
ball = canvas.create_oval(
    (WINDOW_WIDTH - BALL_SIZE) / 2,
    WINDOW_HEIGHT / 2,
    (WINDOW_WIDTH + BALL_SIZE) / 2,
    WINDOW_HEIGHT / 2 + BALL_SIZE,
    fill="red"
)

ball_dx = 3   # x-direction speed
ball_dy = -3  # y-direction speed

# -------------------------------
# Bricks setup
# -------------------------------
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]

for row in range(BRICK_ROWS):
    for col in range(BRICK_COLUMNS):
        x1 = col * BRICK_WIDTH + 5
        y1 = row * BRICK_HEIGHT + 5
        x2 = x1 + BRICK_WIDTH - 10
        y2 = y1 + BRICK_HEIGHT - 10
        brick = canvas.create_rectangle(x1, y1, x2, y2, fill=colors[row % len(colors)], width=2)
        bricks.append(brick)

# -------------------------------
# Paddle movement functions
# -------------------------------
def move_left(event):
    x1, y1, x2, y2 = canvas.coords(paddle)
    if x1 > 0:  # keep paddle inside screen
        canvas.move(paddle, -20, 0)

def move_right(event):
    x1, y1, x2, y2 = canvas.coords(paddle)
    if x2 < WINDOW_WIDTH:  # keep paddle inside screen
        canvas.move(paddle, 20, 0)

canvas.bind("<Left>", move_left)
canvas.bind("<Right>", move_right)
canvas.focus_set()


# -------------------------------
# Ball movement + collision
# -------------------------------
def move_ball():
    global ball_dx, ball_dy

    canvas.move(ball, ball_dx, ball_dy)
    x1, y1, x2, y2 = canvas.coords(ball)

    # Bounce off left/right walls
    if x1 <= 0 or x2 >= WINDOW_WIDTH:
        ball_dx = -ball_dx

    # Bounce off top
    if y1 <= 0:
        ball_dy = -ball_dy

    # Bounce off paddle
    paddle_x1, paddle_y1, paddle_x2, paddle_y2 = canvas.coords(paddle)
    if (y2 >= paddle_y1 and y1 <= paddle_y2 and x2 >= paddle_x1 and x1 <= paddle_x2):
        ball_dy = -ball_dy  # bounce upward

    # Ball falls below paddle = Game Over
    if y2 >= WINDOW_HEIGHT:
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text="GAME OVER", fill="white", font=("Arial", 30))
        return  # stop moving ball

    # Check collision with bricks
    hit_brick = None
    for brick in bricks:
        bx1, by1, bx2, by2 = canvas.coords(brick)
        if (x2 >= bx1 and x1 <= bx2 and y2 >= by1 and y1 <= by2):
            hit_brick = brick
            break

    if hit_brick:
        canvas.delete(hit_brick)
        bricks.remove(hit_brick)
        ball_dy = -ball_dy  # bounce after hitting brick

        # Win condition
        if not bricks:
            canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text="YOU WIN!", fill="yellow", font=("Arial", 30))
            return

    # Keep the ball moving
    root.after(20, move_ball)

# -------------------------------
# Start the game
# -------------------------------
move_ball()
root.mainloop()
