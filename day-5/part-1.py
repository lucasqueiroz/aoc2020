import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'input')

input = open(filename, "r")


class Range:
    def __init__(self, start_col, end_col, start_row, end_row):
        self.columns = list(range(start_col, end_col))
        self.rows = list(range(start_row, end_row))

    def perform_operation(self, operation):
        if operation == "F":
            length = len(self.rows)
            self.rows = self.rows[:length//2]
        elif operation == "B":
            length = len(self.rows)
            self.rows = self.rows[length//2:]
        elif operation == "L":
            length = len(self.columns)
            self.columns = self.columns[:length//2]
        elif operation == "R":
            length = len(self.columns)
            self.columns = self.columns[length//2:]


highest_seat_id = None

for line in input.readlines():
    r = Range(0, 8, 0, 128)
    for c in line:
        r.perform_operation(c)
        row = r.rows[0]
        column = r.columns[0]
        seat_id = row * 8 + column
        if highest_seat_id is None or highest_seat_id < seat_id:
            highest_seat_id = seat_id

print(highest_seat_id)
