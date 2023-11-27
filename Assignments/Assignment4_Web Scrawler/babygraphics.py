"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    distance_between = (width - 2*GRAPH_MARGIN_SIZE)/len(YEARS)
    x = GRAPH_MARGIN_SIZE + distance_between*year_index
    return x


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # Draw upper line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    # Draw bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, CANVAS_HEIGHT, x, 0, width=LINE_WIDTH)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    # survey name list
    for i in range(len(lookup_names)):
        # each name => find its year: rank in name_data.
        length = CANVAS_HEIGHT - 2*GRAPH_MARGIN_SIZE
        name = lookup_names[i]
        # keep each point's x and y position.
        x_position = []
        y_position = []
        # this name's year:rank dictionary
        year_rank = name_data[name]
        # sort the YEARS
        sort_year = sorted(YEARS)
        rank =[]
        # survey each YEARS from past to now to find the rank for each year as the y position.
        for j in range(len(sort_year)):
            x = get_x_coordinate(CANVAS_WIDTH, j)
            #  if the year has rank, y is not on the bottom.
            if str(sort_year[j]) in year_rank:
                y = (length/1000)*int(year_rank[str(sort_year[j])]) + GRAPH_MARGIN_SIZE
                x_position += [x]
                y_position += [y]
                rank += [year_rank[str(sort_year[j])]]
                # if the year has not rank, y is on the bottom.
            else:
                # y = the bottom one
                y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                x_position += [x]
                y_position += [y]
                rank += '*'
        # two points will draw a line => find out two continuous points to make a line.
        # one name one color
        color = COLORS[i]
        for k in range(len(x_position)-1):
            canvas.create_line(x_position[k], y_position[k], x_position[k+1], y_position[k+1], width=LINE_WIDTH,
                               fill=color)
        # show the text of name and rank beside each point.
        for a in range(len(rank)):
            canvas.create_text(x_position[a] + TEXT_DX, y_position[a], text=name + ' ' + rank[a], anchor=tkinter.SW,
                               fill=color)



























# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
