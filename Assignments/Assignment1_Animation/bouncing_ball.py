"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
# Announce as a global variable
click = 0


def main():
    """
    1. Make window
    2. Make a ball be showed at start position(START_X, START_Y)
    3. Click first one time on window => set up var, click to have first-time-click only
    to trigger below animation repeatedly(Fall => Rebound => Fall => Rebound...) till out of the window over 3 times.
    => use while loop
    1st biggest vertical moving distance = big height = window's height- START_Y

    Fall: use while loop to have ball move from top to the bottom.
    1) The biggest vertical moving distance
    2) Horizontal speed = Vx
    3) Vertical speed each time=0(original vertical speed)+ GRAVITY* n(Each time, vertical speed will be added GRAVITY)
    4) Record the accumulated moving distance:
    width = to know if out of window
    height => to know if the fall should be stopped, and the next biggest height should be plus REDUCE.
    5) Each time, ball is moved VX to the right, and moved vertical speed to the top.

    Rebound: use while loop to have ball move from bottom to the top.
    like fall but opposite direction.
    After out of the window over 3 times, ball backs to the start position.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(animation)


def animation(mouse):
    global click
    click += 1
    # only the first click could trigger the animation repeatedly.
    if click == 1:
        # calculate how many times that ball is out of the window.
        out_window_count = 0
        # Record the accumulated moving distance
        width = 0
        # the variation of the vertical speed via the Gravitational acceleration( n: fall / n2: rebound)
        n = 1
        # vertical speed
        vertical_speed = 0
        # The biggest vertical moving distance
        big_height = window.height - START_Y
        # Trigger animation repeatedly till out of window more than 3 times
        while out_window_count <= 3:
            # Record the accumulated moving distance
            height_rebound = 0
            height_fall = 0
            while height_fall <= big_height:
                # fall
                width += VX
                vertical_speed = GRAVITY * n
                height_fall += vertical_speed
                n += 1
                ball.move(VX, vertical_speed)
                pause(DELAY)
                if width >= window.width - START_X:
                    out_window_count += 1
                if out_window_count > 3:
                    window.add(ball, START_X, START_Y)
                    pause(DELAY)
                    break
            if out_window_count > 3:
                break
            # Biggest height will be changed (Reduce 10%)
            big_height *= REDUCE
            while height_rebound < big_height:
                # rebound
                width += VX
                vertical_speed -= GRAVITY
                height_rebound += vertical_speed
                ball.move(VX, -vertical_speed)
                pause(DELAY)
                if width >= window.width - START_X:
                    out_window_count += 1
                if out_window_count > 3:
                    window.add(ball, START_X, START_Y)
                    pause(DELAY)
                    break
            # Biggest height will be changed (Reduce 10%)
            big_height *= REDUCE
            # vertical speed is changed back to 0 for the usage of next falling.
            vertical_speed = 0
            n = 0
            if out_window_count > 3:
                break

        if out_window_count > 3:
            window.add(ball, START_X, START_Y)
            pause(DELAY)


if __name__ == "__main__":
    main()
