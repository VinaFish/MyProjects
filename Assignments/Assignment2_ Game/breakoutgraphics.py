"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.gui.events.timer import pause

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
over_bottom = 0


class BreakoutGraphics:

    def __init__(self, frame_rate, num_lives, vy=INITIAL_Y_SPEED, vx=MAX_X_SPEED, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.window2 = GRect(200, 200, x=window_width/2-100, y=window_height/2-100)
        # Game Over Words
        self.window2.filled = True
        self.window2.fill_color = 'black'
        self.label_terminate = GLabel('', x=self.window2.x+30, y=self.window2.y+100)
        self.label_terminate.color = 'white'
        self.label_terminate.font = '-30'
        # The rate of pause
        self.frame_rate = frame_rate
        # Remaining lives
        self.mum_lives = num_lives
        self.lives_label = GLabel("Life :"+str(self.mum_lives), x=10, y=self.window.height)
        self.lives_label.color = 'black'
        self.lives_label.font = '-20'
        self.window.add(self.lives_label)
        # Score
        self.calculate_brick = 0
        self.score_label = GLabel('Score= '+str(self.calculate_brick), x=10, y=self.window.height-20)
        self.score_label.color = 'black'
        self.score_label.font = '-20'
        self.window.add(self.score_label)
        # Create a paddle
        self. paddle = GRect(paddle_width, paddle_height, x=window_width/2-paddle_width/2,
                             y=window_height-paddle_height-paddle_offset)
        self. paddle.filled = True
        self.paddle.fill_color = 'midnightblue'
        self.window.add(self.paddle)
        self.paddle_offset = paddle_offset
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'blue'
        self.window.add(self.ball)
        self.ball_radius = ball_radius
        # Default initial velocity for the ball
        self.__vx = vx
        self.__vy = vy
        # Initialize our mouse listeners
        self.click = 0
        # Draw bricks
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_row = brick_rows
        self.brick_cols = brick_cols
        self.brick_spacing = brick_spacing
        self.brick_offset = brick_offset
        self.brick_height = brick_height
        self.make_brick()

    def make_brick(self):
        for i in range(self.brick_cols):
            for j in range(self.brick_row):
                brick = GRect(self.brick_width, self.brick_height)
                brick.filled = True
                brick.fill_color = 'lightsteelblue'
                self.window.add(brick, x=+self.brick_width*j+self.brick_spacing*j,
                                y=self.brick_offset+self.brick_height*i+self.brick_spacing*i)

    def set_trigger(self, mouse):
        self.click += 1
        if self.click == 1:
            onmousemoved(self.paddle_move)
            self.ball_move()

    def paddle_move(self, mouse):
        if self.window.width-self.paddle.width/2>= mouse.x >= self.paddle.width/2:
            if 0 < mouse.y < self.window.height:
                self.paddle.x = mouse.x - self.paddle.width / 2
                self.paddle.y = self.window.height - self.paddle_offset - self.paddle.height

    def get_random_vx(self):
        vx = random.randint(-self.__vx, self.__vx)
        if vx != 0:
            return vx
        else:
            vx += 1
            return vx

    def get_vy(self):
        return self.__vy

    def ball_move(self):
        # Ball moves randomly and repeatedly.
        vx = self.get_random_vx()
        vy = self.get_vy()
        global over_bottom
        while True:
            # 1) over the left and right of the window => change direction
            if self.ball.x <= 0 or self.ball.x >= self.window.width:
                vx *= -1
            # 2) over the top of the window=> change direction
            if self.ball.y <= 0:
                vy *= -1
            # 3) over the bottom of the window => back to start place => wait for user to click to start again.
            if self.ball.y >= self.window.height-self.ball.height:
                # out of the window over specific number => Terminate: Game Over
                over_bottom += 1
                self.ball.x = self.window.width/2-self.ball_radius
                self.ball.y = self.window.height/2-self.ball_radius
                self.paddle.x = self.window.width/2-self.paddle.width/2
                self.paddle.y = self.window.height-self.paddle.height - self.paddle_offset
                if over_bottom == self.mum_lives:
                    self.window.add(self.window2)
                    self.label_terminate.text = 'Game Over!\n'+'Score= '+str(self.calculate_brick)
                    self.window.add(self.label_terminate)
                remaining_lives = self.mum_lives - over_bottom
                self.lives_label.text = 'chance= ' + str(remaining_lives)
                self.lives_label.color = 'red'
                break
            # 4) Hit brick  or paddle:
            # Hit Paddle => change direction(rebound)
            if self.window.height/2 < self.ball.y < self.window.height-self.paddle_offset-self.ball_radius and vy > 0:
                left_bottom = self.window.get_object_at(self.ball.x, self.ball.y+self.ball_radius*2)
                right_bottom = self.window.get_object_at(self.ball.x+self.ball_radius*2, self.ball.y+self.ball_radius*2)
                if left_bottom is not None and right_bottom is not None:
                    vy *= -1
                else:
                    if left_bottom is not None:
                        vy *= -1
                    if right_bottom is not None:
                        vy *= -1

            # Hit bricks => change direction(rebound) & have that brick disappear
            if self.ball.y <= self.brick_offset+self.brick_height*self.brick_cols+self.brick_spacing*(self.brick_row-1):
                # ball moves up to hit bricks => rebound & have that brick disappear
                if vy < 0:
                    left_top = self.window.get_object_at(self.ball.x, self.ball.y)
                    right_top = self.window.get_object_at(self.ball.x + self.ball_radius * 2, self.ball.y)
                    if left_top is not None and right_top is not None:
                        self.window.remove(right_top)
                        self.calculate_brick += 1
                        vy *= -1
                    else:
                        if left_top is not None:
                            self.window.remove(left_top)
                            self.calculate_brick += 1
                            vy *= -1
                        if right_top is not None:
                            self.window.remove(right_top)
                            self.calculate_brick += 1
                            vy *= -1
                    self.score_label.text = 'Score= ' + str(self.calculate_brick)
                    if self.calculate_brick == self.brick_row * self.brick_cols:
                        self.ball.x = self.window.width / 2 - self.ball_radius
                        self.ball.y = self.window.height / 2 - self.ball_radius
                        self.paddle.x = self.window.width / 2 - self.paddle.width / 2
                        self.paddle.y = self.window.height - self.paddle.height - self.paddle_offset
                        self.window.add(self.window2)
                        self.label_terminate.text = \
                            'Winner!\n' + 'Score= ' + str(self.calculate_brick)
                        self.window.add(self.label_terminate)
                        self.score_label.text = 'Score= ' + str(self.calculate_brick)
                        break

            self.ball.move(vx, vy)
            pause(self.frame_rate)
            pause(self.frame_rate)
        if over_bottom < self.mum_lives and self.calculate_brick < (self.brick_row * self.brick_cols):
            self.click = 0
