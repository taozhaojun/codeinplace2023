from graphics import Canvas
import time
import random

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20
DELAY = 0.1

def main():
    # Set up the world
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, 'blue')
    target = create_random_target(canvas)

    current_direction = "right"

    # Animation loop
    while True:
        # Update the world for one heartbeat
        current_direction = changedirection(canvas, current_direction)

        if current_direction == "right":
            canvas.move(player, SIZE, 0)
        elif current_direction == "left":
            canvas.move(player, -SIZE, 0)
        elif current_direction == "up":
            canvas.move(player, 0, -SIZE)
        elif current_direction == "down":
            canvas.move(player, 0, SIZE)

        # Check for out of bounds
        player_x = canvas.get_left_x(player)
        player_y = canvas.get_top_y(player)
        if player_x < 0 or player_x >= CANVAS_WIDTH or player_y < 0 or player_y >= CANVAS_HEIGHT:
            game_over(canvas)
            break

        # Check for collision with the goal
        if check_collision(canvas, player, target):
            canvas.delete(target)
            target = create_random_target(canvas)

        # Sleep
        time.sleep(DELAY)

def changedirection(canvas, current_direction):
    key = canvas.get_last_key_press()
    if key == 'ArrowLeft' and current_direction != "right":
        return "left"
    elif key == 'ArrowRight' and current_direction != "left":
        return "right"
    elif key == 'ArrowUp' and current_direction != "down":
        return "up"
    elif key == 'ArrowDown' and current_direction != "up":
        return "down"
    else:
        return current_direction

def create_random_target(canvas):
    rand_x = random.randint(0, CANVAS_WIDTH - SIZE)
    rand_y = random.randint(0, CANVAS_HEIGHT - SIZE)
    while rand_x % SIZE != 0:
        rand_x = random.randint(0, CANVAS_WIDTH - SIZE)
    while rand_y % SIZE != 0:
        rand_y = random.randint(0, CANVAS_HEIGHT - SIZE)
    return canvas.create_rectangle(rand_x, rand_y, rand_x + SIZE, rand_y + SIZE, 'orange')

def check_collision(canvas, obj1, obj2):
    obj1_leftx = canvas.get_left_x(obj1)
    obj1_topy = canvas.get_top_y(obj1)
    obj2_leftx = canvas.get_left_x(obj2)
    obj2_topy = canvas.get_top_y(obj2)
    return (obj1_leftx == obj2_leftx and obj1_topy==obj2_topy)

def game_over(canvas):
    canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, text='Game Over',color = 'red')

if __name__ == '__main__':
    main()
