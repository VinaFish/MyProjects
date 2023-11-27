"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
# Announce as global variable.
original_spot_x = 0
original_spot_y = 0
click = 0
SIZE = 10
hallow_ball = GOval(SIZE*2, SIZE*2)


def main():
    """
    could process below repeatedly:

    the number of clicks:
    1) Odd:
    show hollow ball, and the click spot is the center of the ball.
    2) Even:
    draw line. (Need to know the previous mouse's position and the latest mouse's position)
    """
    onmouseclicked(ball_line)


def ball_line(mouse):
    global click, original_spot_x, original_spot_y
    click += 1
    if click % 2 != 0:
        # click even times => show hollow ball
        original_spot_x = mouse.x - SIZE
        original_spot_y = mouse.y - SIZE
        window.add(hallow_ball, original_spot_x, original_spot_y)
        hallow_ball.filled = False

    else:
        # click odd times => draw line
        line = GLine(original_spot_x+SIZE, original_spot_y+SIZE,  mouse.x, mouse.y)
        window.add(line)
        # original spot's hallow ball disappears
        window.remove(hallow_ball)


if __name__ == '__main__':
    main()

