"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GRect, GOval, GArc, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Piece and Happy
    Enjoy the moment
    Big World
    """
    window = GWindow(800, 400)
    window.filled = True
    ball = GOval(100, 100, x=350, y=150)
    eye_left = GOval(10,10, x=375, y=170)
    eye_right = GOval(10,10, x=415, y=170)
    frame = GRect(400, 200, x=200, y=100)
    smile = GArc(50, 50, 180, 180)
    eye_right.filled = True
    eye_left.filled = True
    ball.filled = True
    frame.filled = True
    ball.fill_color = 'yellow'
    frame.fill_color = 'beige'
    eye_right.fill_color = 'black'
    eye_left.fill_color = 'black'
    window.add(frame)
    window.add(ball)
    window.add(eye_left)
    window.add(eye_right)
    window.add(smile, x=375, y=200)
    word = GLabel('Smile', x=220, y=150)
    window.add(word)








if __name__ == "__main__":
    main()
