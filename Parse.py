
class CSVParser():
    def __init__(self, file_name):
        self.file_name=file_name
    def Read_Two_Column_File():
        with open(file_name, 'r') as data:
            x = []
            y = []
            for line in data:
                p = line.split()
                x.append(float(p[0]))
                y.append(float(p[1]))

        return x, y
