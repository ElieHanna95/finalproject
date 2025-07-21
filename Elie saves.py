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





