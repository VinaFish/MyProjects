"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

1. generate object to call class
2.Only 1st click to trigger the function, animation.
3.Function, animation:
 1) Paddle could follow mouse to move.
 2) Get random horizontal speed and initial vertical speed
 3) while loop => have ball move continuously
    (check point)
    * If out of the right/left window, change X direction.
    * If out of the top window, change y direction.
    * if out of the bottom window, stop while loop and then ball backs to the start place.
     When happened over num_lives times, terminate => Game over. show the score
    *If hit objects:
    Hit paddle => Change direction
    Hit brick => Change direction and remove that brick. Moreover, calculate the count of the removed bricks.
    When remove all bricks => Terminate . SHow Win+ Score
    (move)
    ball move(Vx, Vy)
    (modify value)
    n: about vertical speed variable.
4) out of the while loop, count of  click backs to 0



3. Animation
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmouseclicked

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics(FRAME_RATE, NUM_LIVES)
    onmouseclicked(graphics.set_trigger)





       


if __name__ == '__main__':
    main()
