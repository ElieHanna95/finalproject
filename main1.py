import os
import sys
import time
import pytest
from functools import wraps


ANSI_COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "cyan": "\033[96m",
    "magenta": "\033[95m",
    "reset": "\033[0m",
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


class FileReader:
    def __init__(self, filename):
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    def line_generator(self):
        with open(self._filename, "r", encoding="utf-8") as file:
            for line in file:
                yield line.rstrip("\n")

    @staticmethod
    def count_lines(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return sum(1 for _ in f)

    @classmethod
    def from_string(cls, content, outfilename):
        with open(outfilename, "w", encoding="utf-8") as f:
            f.write(content)
        return cls(outfilename)

    def __str__(self):
        lines = []
        with open(self._filename, "r", encoding="utf-8") as f:
            for i, line in enumerate(f):
                if i >= 3:
                    break
                lines.append(line.rstrip("\n"))
        return "\n".join(lines)

    def __add__(self, other):
        base1 = os.path.basename(self._filename)
        base2 = os.path.basename(other._filename)
        dir1 = os.path.dirname(self._filename)
        new_file = os.path.join(dir1, f"{base1}_plus_{base2}.txt")
        with open(new_file, "w", encoding="utf-8") as fout, open(
            self._filename, "r", encoding="utf-8"
        ) as f1, open(other._filename, "r", encoding="utf-8") as f2:
            fout.writelines(f1.readlines() + f2.readlines())
        return FileReader(new_file)

    def concat_files(self, *filenames):
        with open(self._filename, "a", encoding="utf-8") as fout:
            for fname in filenames:
                with open(fname, "r", encoding="utf-8") as fin:
                    fout.write(fin.read())


class UpperCaseFileReader(FileReader):
    def line_generator(self):
        with open(self._filename, "r", encoding="utf-8") as file:
            for line in file:
                yield line.rstrip("\n").upper()

    def __str__(self):
        with open(self._filename, "r", encoding="utf-8") as f:
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
        sys.stdout.write(" " * 40 + "\r")  # clear old line
        sys.stdout.write(
            f"{ANSI_COLORS[color]}Time left: {sec} second{'s' if sec != 1 else ''}{ANSI_COLORS['reset']}\r"
        )
        sys.stdout.flush()
        time.sleep(1)
    print(f"{ANSI_COLORS['magenta']}Time's up!{ANSI_COLORS['reset']}")


if __name__ == "__main__":
    try:
        seconds = int(input("Enter countdown seconds: "))
        show_countdown(seconds)
    except ValueError:
        print(f"{ANSI_COLORS['red']}Invalid input!{ANSI_COLORS['reset']}")
