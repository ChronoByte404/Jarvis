import curses
import time
import random
from colorama import init, Fore, Back, Style
import os

init(autoreset=True)

class NeuralHologram:
    def __init__(self):
        self.title = ""

    def switch_to_blue(self):
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)

    def switch_to_yellow(self):
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    def display(self, stdscr):
        # Clear screen
        stdscr.clear()

        # Set font and color
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        stdscr.attron(curses.color_pair(1))
        stdscr.attron(curses.A_BOLD)


        # Loop to animate hologram
        while True:
            display = [    "         ▄▄███████▄▄",     "      ▄██▀░░░░░░░▀██▄",    "     ██░░░░░░░░░░░░░██",    "   ▄██░░░░░░░░░░░░░░░██▄",    "  ██░░░░░░░░░░░░░░░░░░░██",    " ██░░░░░░░░░░░░░░░░░░░░░██",    " ██░░░░░░░░░░░░░░░░░░░░░██", f" ██░░░░░░░{self.title}░░░░░░░░░░░██",    " ██░░░░░░░░░░░░░░░░░░░░░██",    "  ██░░░░░░░░░░░░░░░░░░██",    "   ▀██░░░░░░░░░░░░░░██▀",    "     ▀██▄░░░░░░░░░▄██▀",    "        ▀▀███████▀▀"]

            # Clear screen
            stdscr.clear()

            # Get size of terminal
            max_y, max_x = stdscr.getmaxyx()

            # Calculate center of screen
            center_x = int((max_x - len(display[0])) / 2)
            center_y = int((max_y - len(display)) / 2)

            # Display hologram
            for i in range(len(display)):
                stdscr.addstr(center_y+i, center_x, display[i], curses.color_pair(1))

            # Randomly select characters to highlight
            highlight_chars = random.sample(range(len(display[0])), len(display[0])//2)

            # Highlight characters
            for i in range(len(display)):
                for j in range(len(display[i])):
                    which = random.choice([1, 2])
                    if which == 1:
                        color = curses.COLOR_CYAN
                        stdscr.addstr(center_y+i, center_x+j, display[i][j], curses.color_pair(color))
                    else:
                        stdscr.addstr(center_y+i, center_x+j, display[i][j], curses.color_pair(1))

            # Refresh screen
            stdscr.refresh()

            # Sleep for a short time
            time.sleep(0.1)

    def activate(self):
        curses.wrapper(self.display)

if __name__ == "__main__":
    Hologram = NeuralHologram()
    Hologram.activate()
