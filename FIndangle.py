import math
side_AB = int(input())

side_BC = int(input())

result = round(math.degrees(math.atan2(side_AB,side_BC)))

print(f"{result}\N{DEGREE SIGN}")
