import graphics
import time
import random
import math

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 600
PADDLE_Y = CANVAS_HEIGHT - 30
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
INITIAL_VELOCITY = 15
BALL_RADIUS = 10
START_X = CANVAS_WIDTH / 2-BALL_RADIUS
START_Y = CANVAS_HEIGHT / 2-BALL_RADIUS

BRICK_GAP = 5
BRICK_WIDTH = (CANVAS_WIDTH-BRICK_GAP*9) / 10
BRICK_HEIGHT = 10
dx = 10
DELAY = 0.1
    
def create_bricks(canvas):
    bricks = []
    for row in range(5):
        for col in range(10):
            x = col * (BRICK_WIDTH + BRICK_GAP)
            y = row * (BRICK_HEIGHT + BRICK_GAP)
            brick = canvas.create_rectangle(x, y, x + BRICK_WIDTH, y + BRICK_HEIGHT,get_brick_color(row))
            bricks.append(brick)
    return bricks
    
def get_brick_color(row):
    colors = ["red", "orange", "yellow", "green", "cyan"]
    return colors[row % len(colors)]
    
def changedirection(canvas):
    key = canvas.get_last_key_press()
    if key == 'ArrowLeft':
        return "left"
    elif key == 'ArrowRight':
        return "right"
    else:
        return None
        
def check_collision(canvas, ball, bricks,paddle):
    left_x_ball = canvas.get_left_x(ball)
    top_y_ball = canvas.get_top_y(ball)
    right_x_ball = left_x_ball +BALL_RADIUS*2
    bottom_y_ball = top_y_ball +BALL_RADIUS*2
    objs = canvas.find_overlapping(left_x_ball, top_y_ball, right_x_ball, bottom_y_ball)
    for obj in objs:
        if obj and obj!=ball and obj!=paddle:
            canvas.delete(obj)
            bricks.remove(obj)
            return True
    return False

def main():
    canvas = graphics.Canvas(CANVAS_WIDTH,CANVAS_HEIGHT)
    # TODO: your code here
    # Create paddle
    paddle = canvas.create_rectangle(CANVAS_WIDTH / 2 - PADDLE_WIDTH / 2, PADDLE_Y,CANVAS_WIDTH / 2 + PADDLE_WIDTH / 2, PADDLE_Y + PADDLE_HEIGHT)

    # Create bricks
    bricks = create_bricks(canvas)
    
    # Create ball
    ball_x = START_X
    ball_y = START_Y
    x_velocity = INITIAL_VELOCITY
    y_velocity = INITIAL_VELOCITY
    ball = canvas.create_oval(ball_x, ball_y,
                              ball_x + BALL_RADIUS,
                              ball_y + BALL_RADIUS,
                              'blue')
    # Game loop
    while True:
        # Move paddle with key
        '''
        current_direction = changedirection(canvas)
        if current_direction == "right":
            canvas.move(paddle, dx, 0)
        elif current_direction == "left":
            canvas.move(paddle, -dx, 0)
        '''
        # Move paddle with mouse
        paddle_x = canvas.get_mouse_x()
        canvas.moveto(paddle, paddle_x-PADDLE_WIDTH/2, PADDLE_Y + PADDLE_HEIGHT)
        
        # Move ball
        if (ball_x < 0) or (ball_x + BALL_RADIUS >= CANVAS_WIDTH):
            x_velocity = -x_velocity
        if ball_y + BALL_RADIUS >= CANVAS_HEIGHT-PADDLE_HEIGHT and ball_x>paddle_x-PADDLE_WIDTH/2 and ball_x<paddle_x+PADDLE_WIDTH/2:
            y_velocity = -y_velocity
        if (ball_y < 0):
            y_velocity = -y_velocity
        if (ball_y + BALL_RADIUS >= CANVAS_HEIGHT):
            canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, text='Game Over',color = 'red')
            break
        ball_x += x_velocity
        ball_y += y_velocity
        canvas.moveto(ball, ball_x, ball_y)
        # Check for collisions and remove brick
        if check_collision(canvas, ball, bricks,paddle):
            # Handle collision here (e.g., change ball direction)
            y_velocity = -y_velocity
        if len(bricks) == 0:
            canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, text='You win',color = 'red')
            break
        # Sleep
        time.sleep(DELAY)


if __name__ == '__main__':
    main()
