import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input')

lines_a = tuple(open(filename, "r"))
lines_b = tuple(open(filename, "r"))
lines_c = tuple(open(filename, "r"))

def find_product():
    for line_a in lines_a:
        int_line_a = int(line_a)
        for line_b in lines_b:
            int_line_b = int(line_b)
            for line_c in lines_c:
                int_line_c = int(line_c)
                if (int_line_a + int_line_b + int_line_c == 2020):
                    print(int_line_a)
                    print(int_line_b)
                    print(int_line_c)
                    print(int_line_a * int_line_b * int_line_c)
                    return

find_product()
