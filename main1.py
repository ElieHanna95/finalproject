import sys
import time
from functools import wraps
ANSI_COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "cyan": "\033[96m",
    "magenta": "\033[95m",
    "reset": "\033[0m"
}

def deco(color):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(ANSI_COLORS.get(color, ""), end="")
            result = func(*args, **kwargs)
            print(ANSI_COLORS["reset"], end="")
            return result
        return wrapper
    return decorator
class UpperCaseFileReader(FileReader):
    def __init__(self, filename):
        self._filename = filename
    def line_generator(self):
        with open(self._filename, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.rstrip('\n').upper()

    def __str__(self):
        with open(self._filename, 'r', encoding='utf-8') as f:
            return f.read().upper()

@deco("cyan")
def show_countdown(seconds):
    for sec in range(seconds, -1, -1):
        if sec > 10:
            color = "cyan"
        elif sec > 5:
            color = "green"
        elif sec > 2:
            color = "yellow"
        else:
            color = "red"
        sys.stdout.write(f"{ANSI_COLORS[color]}Time left: {sec} seconds{ANSI_COLORS['reset']}\r")
        sys.stdout.flush()
        time.sleep(1)
    print(f"{ANSI_COLORS['magenta']}Time's up!{ANSI_COLORS['reset']}")
