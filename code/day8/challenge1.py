# day8 - challenge1
import math


def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    # need to import math and use ceil func instead of round to always round UP to next int
    print(f"You'll need {number_of_cans} cans of paint for this wall")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
