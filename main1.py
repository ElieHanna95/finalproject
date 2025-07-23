import os
import sys
import time
import pytest
from functools import wraps

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
        with open(self._filename, 'r') as file:
            for line in file:
                yield line.rstrip('\n')
    @staticmethod
    def count_lines(filename):
        with open(filename, 'r') as f:
            return sum(1 for _ in f)
    @classmethod
    def from_string(cls, content, outfilename):
        with open(outfilename, 'w') as f:
            f.write(content)
        return cls(outfilename)
    def __str__(self):
        lines = []
        with open(self._filename, 'r') as f:
            for i, line in enumerate(f):
                if i >= 3:
                    break
                lines.append(line.rstrip('\n'))
        return "\n".join(lines)
    def __add__(self, other):
        new_file = f"{self._filename}_plus_{other._filename}.txt"
        with open(new_file, 'w') as fout, open(self._filename, 'r') as f1, open(other._filename, 'r') as f2:
            fout.writelines(f1.readlines() + f2.readlines())
        return FileReader(new_file)
    def __add__(self, other):
        base1 = os.path.basename(self._filename)
        base2 = os.path.basename(other._filename)
        dir1 = os.path.dirname(self._filename)
        new_file = os.path.join(dir1, f"{base1}_plus_{base2}.txt")
        with open(new_file, 'w') as fout, open(self._filename, 'r') as f1, open(other._filename, 'r') as f2:
            fout.writelines(f1.readlines() + f2.readlines())
        return FileReader(new_file)
    def concat_files(self, *filenames):
        with open(self._filename, 'a') as fout:
            for fname in filenames:
                with open(fname, 'r') as fin:
                    fout.write(fin.read())
    def line_generator(self):
        with open(self._filename, 'r', encoding='utf-8') as file:
            for line in file:
                yield line.rstrip('\n')
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
        def line_generator(self):
            with open(self._filename, 'r', encoding='utf-8') as file:
                for line in file:
                    yield line.rstrip('\n').upper()
    class UpperCaseFileReader(FileReader):
        def line_generator(self):
            with open(self._filename, 'r', encoding='utf-8') as file:
                for line in file:
                    yield line.rstrip('\n').upper()
        def __str__(self):
            with open(self._filename, 'r', encoding='utf-8') as f:
                return f.read().upper()